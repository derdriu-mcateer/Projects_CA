# You work for a manufacturer, and have been asked to calculate the total profit made on the sales of a product. 
# You are given a dictionary containing the cost price per unit (in dollars), sell price per unit (in dollars), 
# and the starting inventory. Return the total profit made, rounded to the nearest dollar.

info = {
  "cost_price": 32.67,
  "sell_price": 45.00,
  "inventory": 1200
}

def profit():
   
    total_profit = round((info["inventory"]) * (info["sell_price"] - info["cost_price"]))
    

    print(total_profit)

profit()