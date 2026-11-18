
import csv
import yfinance as yf


def get_current_price(symbol):
    try:
        stock = yf.Ticker(symbol)
        history = stock.history(period="1d")

        if history.empty:
            raise ValueError("Price not available")

        return float(history["Close"].iloc[-1])

    except Exception:
        print("Unable to fetch live price.")
        return float(input("Enter current stock price manually: "))


def track_portfolio():

    portfolio = []
    total_investment = 0
    total_current_value = 0

    print("\n================================")
    print("   STOCK PORTFOLIO TRACKER")
    print("================================")

    try:
        count = int(input("\nEnter number of stocks: "))

        if count <= 0:
            print("Please enter at least one stock.")
            return

        for i in range(count):

            print(f"\n--- Stock {i + 1} Details ---")

            symbol = input("Enter stock ticker: ").strip().upper()

            if not symbol:
                print("Ticker cannot be empty.")
                return

            buy_price = float(input("Enter buy price: "))
            quantity = int(input("Enter number of shares: "))

            if buy_price <= 0 or quantity <= 0:
                print("Price and quantity must be positive.")
                return

            current_price = get_current_price(symbol)

            if current_price <= 0:
                print("Invalid current price.")
                return

            investment = buy_price * quantity
            current_value = current_price * quantity

            profit_loss = current_value - investment
            gain_loss = (profit_loss / investment) * 100

            total_investment += investment
            total_current_value += current_value

            portfolio.append({
                "Symbol": symbol,
                "Buy Price": buy_price,
                "Quantity": quantity,
                "Current Price": current_price,
                "Investment": investment,
                "Current Value": current_value,
                "Profit/Loss": profit_loss,
                "Gain/Loss %": gain_loss
            })

        print("\n========== PORTFOLIO SUMMARY ==========")

        for stock in portfolio:

            print("\nStock:", stock["Symbol"])
            print("Investment: ₹", round(stock["Investment"], 2))
            print("Current Value: ₹", round(stock["Current Value"], 2))
            print("Profit/Loss: ₹", round(stock["Profit/Loss"], 2))
            print("Gain/Loss: ", round(stock["Gain/Loss %"], 2), "%")

        total_profit_loss = total_current_value - total_investment

        total_percentage = (
            total_profit_loss / total_investment
        ) * 100

        print("\n========== TOTAL PORTFOLIO ==========")
        print("Total Investment: ₹", round(total_investment, 2))
        print("Current Value: ₹", round(total_current_value, 2))
        print("Total Profit/Loss: ₹", round(total_profit_loss, 2))
        print("Overall Return: ", round(total_percentage, 2), "%")

        # Save portfolio into CSV file
        filename = "portfolio_summary.csv"

        with open(filename, "w", newline="") as file:

            writer = csv.DictWriter(
                file,
                fieldnames=portfolio[0].keys()
            )

            writer.writeheader()
            writer.writerows(portfolio)

        print("\nPortfolio saved successfully!")
        print("CSV File:", filename)

    except ValueError:
        print("\nInvalid input! Please enter valid numbers.")

    except Exception as error:
        print("\nError:", error)


if __name__ == "__main__":
    track_portfolio()
