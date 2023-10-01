# Roblox Free Item Buyer

Originally made by [insaneinthamembrane](https://github.com/insaneinthamembrane/roblox-free-item-buyer)

## How to use ( local )

### Requirements
- Python 3.6 or higher
- pip
- git / zip
- Roblox Cookie ( `.ROBLOSECURITY` ) ( [How to get it](https://www.youtube.com/watch?v=O9iPTvXnpnU) )
- Place the Cookie ind the `cookie.txt` file

### Steps
1. Pull the repository
2. Install the dependencies with `pip install -r requirements.txt`
3. Run the script with `python main.py`
4. Wait for the script to finish

## How to use ( Docker )

### Requirements
- Docker
- Roblox Cookie ( `.ROBLOSECURITY` ) ( [How to get it](https://www.youtube.com/watch?v=O9iPTvXnpnU) )
- Place the Cookie ind the `cookie.txt` file

### Steps
1. Pull the repository
2. Build the image with `docker build -t roblox_itemBuyer .`
3. Run the image with `docker run -it --rm -v $(pwd):/app roblox_itemBuyer`
4. Wait for the script to finish
