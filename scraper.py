import json
import random
from datetime import datetime

DATA_FILE = "data.json"

def update_prices():
    try:
        with open(DATA_FILE, "r") as f:
            items = json.load(f)

        today = datetime.now().strftime("%Y-%m-%d")
        updated = 0

        for item in items:
            # Price update logic: simulates monitoring retailer price fluctuations
            current_price = item.get("price", item.get("msrp", 500))
            # Simulates small daily floor price adjustments (-$15 to +$5)
            fluctuation = random.choice([-15, -10, -5, 0, 0, 5])
            new_price = max(30, current_price + fluctuation)
            
            item["price"] = new_price
            item["last_updated"] = today
            updated += 1

        with open(DATA_FILE, "w") as f:
            json.dump(items, f, indent=2)

        print(f"[{datetime.now()}] SpecFloor Engine: Updated prices for {updated} hardware listings.")

    except Exception as e:
        print(f"Error updating prices: {e}")

if __name__ == "__main__":
    update_prices()