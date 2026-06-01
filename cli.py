import typer
from rich import print
from rich.table import Table
import time

from bot.client import BinanceClient
from bot.orders import OrderManager
from bot.validators import validate_inputs
from bot.logging_config import setup_logger

app = typer.Typer()

# print("CLI FILE LOADED - UPDATED VERSION")


@app.command()
def place_order(
    symbol: str,
    side: str,
    order_type: str,
    quantity: float,
    price: float = None
):

    logger = setup_logger()

    try:
        validate_inputs(symbol, side, order_type, quantity, price)

        client = BinanceClient().get_client()
        manager = OrderManager(client)

        response = manager.place_order(
            symbol.upper(),
            side.upper(),
            order_type.upper(),
            quantity,
            price
        )

        time.sleep(2)

        details = manager.get_order(symbol.upper(), response["orderId"])

        table = Table(title="Binance Futures Order")

        table.add_column("Field", style="cyan")
        table.add_column("Value", style="green")

        table.add_row("Order ID", str(details["orderId"]))
        table.add_row("Status", details["status"])
        table.add_row("Executed Qty", details["executedQty"])
        table.add_row("Avg Price", details["avgPrice"] or "N/A")

        print(table)

        logger.info(details)

    except Exception as e:
        print(f"[red]FAILED: {e}[/red]")
        logger.error(e)


if __name__ == "__main__":
    app()