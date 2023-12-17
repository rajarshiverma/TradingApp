from login import *

try:
    orderparams = {
        "variety": "NORMAL",
        "tradingsymbol": "SBIN-EQ",
        "symboltoken": "3045",
        "transactiontype": "BUY",
        "exchange": "NSE",
        "ordertype": "LIMIT",
        "producttype": "INTRADAY",
        "duration": "DAY",
        "price": "19500",
        "squareoff": "0",
        "stoploss": "0",
        "quantity": "1"
        }
    # Method 1: Place an order and return the order ID
    orderid = sma.placeOrder(orderparams)
    logger.info(f"PlaceOrder : {orderid}")
    # Method 2: Place an order and return the full response
    # response = sma.placeOrderFullResponse(orderparams)
    # logger.info(f"PlaceOrder : {response}")
except Exception as e:
    logger.exception(f"Order placement failed: {e}")