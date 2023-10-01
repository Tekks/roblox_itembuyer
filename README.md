# Roblox Free Item Buyer

Originally made by [insaneinthamembrane](https://github.com/insaneinthamembrane/roblox-free-item-buyer)

## How to use ( local )

### Requirements
- Python 3.6 or higher
- pip
- git / zip
- Roblox Cookie ( `.ROBLOSECURITY` ) ( [How to get it](https://www.youtube.com/watch?v=O9iPTvXnpnU) )
- Place the Cookie in the `cookie.txt` file

### Steps
1. Pull the repository
2. Install the dependencies with `pip install -r requirements.txt`
3. Run the script with `python main.py`
4. Wait for the script to finish

## How to use ( Docker )

### Requirements
- Docker
- Roblox Cookie ( `.ROBLOSECURITY` ) ( [How to get it](https://www.youtube.com/watch?v=O9iPTvXnpnU) )
- Place the Cookie as environment variable `COOKIE` ( see example below )

### Steps
1. Use Docker compose to build and run the container
```
version: "3.9"
services:
  roblox_itemBuyer:
    image: nottekks/roblox_itembuyer:latest
    container_name: rroblox_itembuyer
    restart: unless-stopped
    environment:
      - COOKIE=<YOUR COOKIE HERE>
```