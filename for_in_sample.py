fruits = ['Apples', 'Oranges', 'Bananas']
quantities = [5, 3, 4]
prices = [1.50, 2.25, 0.89]
i = 0
output = []
for fruit in fruits:
  temp_qty = quantities[i]
  temp_price = prices[i]
  output.append((fruit, temp_qty, temp_price))
  i += 1
print(output)