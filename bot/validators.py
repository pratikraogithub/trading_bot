VALID_SIDES = ["BUY", "SELL"]
VALID_TYPES = ["MARKET", "LIMIT"]

def validate_inputs(symbol, side, order_type, quantity, price=None):

    if side.upper() not in VALID_SIDES:
        raise ValueError("Side must be BUY or SELL")

    if order_type.upper() not in VALID_TYPES:
        raise ValueError("Order type must be MARKET or LIMIT")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

    if order_type.upper() == "LIMIT":
        if price is None:
            raise ValueError("Price required for LIMIT order")

        if price <= 0:
            raise ValueError("Price must be positive")