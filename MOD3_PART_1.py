mealPrice = float(input("Please enter total price: $"))

mealTax = mealPrice * 0.07
mealTip = mealPrice * 0.18
total = mealPrice + mealTax + mealTip

print(f"Meal price: ${mealPrice:.2f}")
print(f"Tax (7%): ${mealTax:.2f}")
print(f"Tip (18%): ${mealTip:.2f}")
print(f"Total: ${total:.2f}")
