# Roblox Free Item Buyer

Originally made by [insaneinthamembrane](https://github.com/insaneinthamembrane/roblox-free-item-buyer)


## What is this?
This is a script that will buy "all" the free items on the Roblox catalog.
There are some free items which need some requirements to be met before you can buy them, this script will not buy those items.

It uses a sqlite database to keep track of which items have been bought, so it will not buy the same item twice. Feel free to map the database to a specific location on your host machine if you want to keep the database after the docker pvc is deleted.

## How to use ( local 📍 )

### Requirements
- Python 3.6 or higher
- pip
- git / zip
- Roblox Cookie ( `.ROBLOSECURITY` ) ( [How to get it](https://www.youtube.com/watch?v=O9iPTvXnpnU) )
- Place the Cookie in the `.env` file
- Fill the Environment variables in `.env` if needed ( see [Environment variables](#environment-variables) )

### Steps
1. Pull the repository
2. Install the dependencies with `pip install -r requirements.txt`
3. Run the script with `python main.py`
4. Wait for the script to finish

## How to use ( Docker 🐬 )

### Requirements
- Docker
- Roblox Cookie ( `.ROBLOSECURITY` ) ( [How to get it](https://www.youtube.com/watch?v=O9iPTvXnpnU) )
- Place the Cookie as environment variable `COOKIE` ( see example below )
- Fill the Environment variables if needed ( see [Environment variables](#environment-variables) )

### Steps
1. Use Docker compose to build and run the container [docker-compose.yml](docker-compose.yml)
```yml
version: "3.9"
services:
  roblox_itembuyer:
    image: nottekks/roblox_itembuyer:latest
    container_name: roblox_itembuyer
    restart: unless-stopped
    volumes:
      - db:/app/db
    environment:
      - COOKIE=<YOUR COOKIE HERE> 
      - IDLE_TIME_BETWEEN_RUNS_IN_MIN=600
      - DEBUG=False

volumes:
  db:
```

## Environment variables
| Name | Description | Default | Options |
| --- | --- | --- | --- |
| `COOKIE` | Roblox Cookie String | `None` |
| `IDLE_TIME_BETWEEN_RUNS_IN_MIN` | Time between each run in minutes | `600` | `Any number` |
| `DEBUG` | Shows more information in the console | `False` | `True` / `False` |