from binance.client import Client
import logging

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)
        if testnet:
            self.client.API_URL = "https://testnet.binancefuture.com/fapi"

        logging.basicConfig(
            filename='bot.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )

    def place_market_order(self, symbol, side, quantity):
        try:
            response = self.client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type='MARKET',
                quantity=quantity
            )
            logging.info(f"Market Order Placed: {response}")
            return response
        except Exception as e:
            logging.error(f"Market Order Error: {e}")
            return {"error": str(e)}

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            response = self.client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type='LIMIT',
                quantity=quantity,
                price=price,
                timeInForce='GTC'
            )
            logging.info(f"Limit Order Placed: {response}")
            return response
        except Exception as e:
            logging.error(f"Limit Order Error: {e}")
            return {"error": str(e)}

    def place_stop_market_order(self, symbol, side, quantity, stop_price):
        try:
            response = self.client.futures_create_order(
                symbol=symbol,
                side=side.upper(),
                type='STOP_MARKET',
                stopPrice=stop_price,
                quantity=quantity,
                timeInForce='GTC'
            )
            logging.info(f"Stop Market Order Placed: {response}")
            return response
        except Exception as e:
            logging.error(f"Stop Market Order Error: {e}")
            return {"error": str(e)}
