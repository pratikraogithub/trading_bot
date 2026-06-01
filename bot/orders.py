from binance.exceptions import BinanceAPIException
import logging

logger = logging.getLogger("trading_bot")


class OrderManager:

    def __init__(self, client):
        self.client = client

    def place_order(
        self,
        symbol,
        side,
        order_type,
        quantity,
        price=None
    ):

        try:

            logger.info(
                f"Request => {symbol} {side} {order_type} {quantity} {price}"
            )

            if order_type == "MARKET":

                response = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=order_type,
                    quantity=quantity
                )

            else:

                response = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=order_type,
                    quantity=quantity,
                    price=price,
                    timeInForce="GTC"
                )

            logger.info(f"Response => {response}")

            return response

        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e}")
            raise

        except Exception as e:
            logger.error(f"Unexpected Error: {e}")
            raise