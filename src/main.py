from dotenv import load_dotenv
from lib.client import client as client_discord
import os


if __name__ == '__main__':
    load_dotenv()

    client_discord.run(os.getenv('TOKEN'))
