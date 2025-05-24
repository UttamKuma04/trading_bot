from bot import BasicBot

# Replace these with your valid Testnet API keys
API_KEY = "your_testnet_api_key"
API_SECRET = "your_testnet_api_secret"

bot = BasicBot(API_KEY, API_SECRET)

def main():
    symbol = input("Enter symbol (e.g., BTCUSDT): ").upper()
    side = input("Enter side (BUY or SELL): ").upper()
    order_type = input("Enter order type (market, limit, stop): ").lower()

    if side not in ["BUY", "SELL"]:
        print(" Invalid side. Must be BUY or SELL")
        return

    if order_type == "market":
        quantity = float(input("Enter quantity: "))
        result = bot.place_market_order(symbol, side, quantity)

    elif order_type == "limit":
        quantity = float(input("Enter quantity: "))
        price = float(input("Enter limit price: "))
        result = bot.place_limit_order(symbol, side, quantity, price)

    elif order_type == "stop":
        quantity = float(input("Enter quantity: "))
        stop_price = float(input("Enter stop price: "))
        result = bot.place_stop_market_order(symbol, side, quantity, stop_price)

    else:
        print(" Invalid order type. Choose from: market, limit, stop")
        return

    # Output result
    if "error" in result:
        print("Order Failed:", result["error"])
    else:
        print(" Order Placed:")
        print(f"Order ID: {result.get('orderId')}")
        print(f"Status: {result.get('status')}")

if __name__ == "__main__":
    main()
