import argparse

from bot.client import BinanceClient
from bot.orders import OrderManager
from bot.validators import validate_inputs
from bot.logging_config import setup_logger
import time


def main():

    setup_logger()

    parser = argparse.ArgumentParser()

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:

        validate_inputs(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        client = BinanceClient().get_client()

        manager = OrderManager(client)

        response = manager.place_order(
            symbol=args.symbol.upper(),
            side=args.side.upper(),
            order_type=args.type.upper(),
            quantity=args.quantity,
            price=args.price
        )

        time.sleep(2)

        details = manager.get_order(
            args.symbol.upper(),
            response["orderId"]
        )

        print("\nFULL RESPONSE:")
        print(response)

        print("\nORDER REQUEST")
        print("-" * 40)

        print(f"Symbol: {args.symbol}")
        print(f"Side: {args.side}")
        print(f"Type: {args.type}")
        print(f"Quantity: {args.quantity}")

        if args.price:
            print(f"Price: {args.price}")

        print("\nORDER RESPONSE")
        print("-" * 40)

        print(f"Order ID: {details['orderId']}")
        print(f"Status: {details['status']}")
        print(f"Executed Qty: {details['executedQty']}")
        print(f"Average Price: {details['avgPrice']}")

        print("\nSUCCESS")

        

    except Exception as e:

        print(f"\nFAILED: {e}")


if __name__ == "__main__":
    main()