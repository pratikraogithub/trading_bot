from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()

class BinanceClient:

    def __init__(self):
        self.client = Client(
            os.getenv("API_KEY"),
            os.getenv("API_SECRET")
        )

        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def get_client(self):
        return self.client