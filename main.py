import requests
import pathlib
import time
import sqlite3
import os
from rich.console import Console
from dotenv import load_dotenv

__version__ = '1.1.0'

# Env
load_dotenv()
cookie = os.getenv("COOKIE")
idleTimeBetweenRunsInMin = int(os.getenv("IDLE_TIME_BETWEEN_RUNS_IN_MIN"))
debug = bool(os.getenv("DEBUG") == "true" or os.getenv("DEBUG") == "True")


# DB Sqlite
con = sqlite3.connect("db/items.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS items (productId INTEGER PRIMARY KEY)")

# Session
session = requests.Session()
session.cookies.update({".ROBLOSECURITY": cookie})

console = Console(highlight=False)

def logInfo(color: str, type: str, content: str) -> None:
    console.print(f"[ [bold {color}]{type}[/] ] {content}")

def logDebug(color: str, type: str, content: str) -> None:
    if debug is False:
        return
    logInfo(color, type, content)

def fetch_items() -> None:
    result = {}
    cursor = ""

    while cursor is not None:
        req = session.get(f"https://catalog.roblox.com/v2/search/items/details?Category=1&Limit=30&MaxPrice=0&cursor={cursor}")
        res = req.json()

        if req.status_code == 429:
            logInfo("red", "X", "Roblox Rate-Limit reached. Waiting 20 seconds")
            time.sleep(20)
            continue

        for item in res.get("data", []):
            itemName = item.get("name")
            itemRestrictions = item.get("itemRestrictions")
            itemId = item.get("productId")
            if "Collectible" in item.get("itemRestrictions"):
                logDebug("red", "-", f"Item Limited: \"{itemId} :: {itemName}\"")
                continue

            cur.execute("SELECT * FROM items WHERE productId=?", (itemId,))
            if cur.fetchone() is not None:
                logDebug("red", "-", f"Item Already Purchased: \"{itemId} :: {itemName}\"")
                continue
            
            result[itemId] = { "name": itemName, "restrictions": itemRestrictions }
            logInfo("blue", "?", f"Item Found: \"{itemId} :: {itemName}\"")

        cursor = res.get("nextPageCursor")

    return result


def purchase(productName: str, productId: int) -> None:
    req = session.post("https://auth.roblox.com/v2/login")
    csrf_token = req.headers["x-csrf-token"]

    while True:
        req = session.post(
            f"https://economy.roblox.com/v1/purchases/products/{productId}",
            json={"expectedCurrency": 1, "expectedPrice": 0, "expectedSellerId": 1},
            headers={"X-CSRF-TOKEN": csrf_token},
        )

        if req.status_code == 429:
            logInfo("red", "X", "Roblox Rate-Limit reached. Waiting 60 seconds")
            time.sleep(60)
            continue

        # add id to db
        cur.execute("INSERT INTO items VALUES (?)", (productId,))
        con.commit()

        res = req.json()
        if "reason" in res and res.get("reason") == "AlreadyOwned":
            return "owned"
        return "purchased"


def main() -> None:
    logInfo("yellow", "!", "Roblox ItemBuyer v" + __version__)
    
    while True:
        freeItems = fetch_items()
        freeItems = { key: value for (key, value) in freeItems.items() if "Collectible" not in value["restrictions"] }
        logInfo("yellow", "!", f"Found {len(freeItems)} free items")
        
        currentItemCount = 0

        for productId, item in freeItems.items():
            currentItemCount += 1
            result = purchase(item["name"], productId)
            if result == "owned":
                logDebug("yellow", "-", f"{currentItemCount} / {len(freeItems)} :: Already purchased: \"{item['name']}\"")
            elif result == "purchased":
                logInfo("green", "+", f"{currentItemCount} / {len(freeItems)} :: Purchased: \"{item['name']}\"")
            time.sleep(2)

        formatedDate = time.strftime("%H:%M:%S %d/%m/%Y", time.localtime(time.time() + (idleTimeBetweenRunsInMin * 60)))
        logInfo("yellow", "!", f"Next run will be at {formatedDate}")
        time.sleep(idleTimeBetweenRunsInMin * 60)

main()