print("Average rainfall in inches calculator")

# prompt for number of years
years = int(input("Enter the number of years: "))

total_rainfall = 0
total_months = 0

# outer loop for each year
for year in range(1, years + 1):
    print(f"\nYear {year}")

    # inner loop, 12 months
    for month in range(1, 13):
        rainfall = float(input(f"Enter rainfall for month {month}: "))
        
        total_rainfall += rainfall
        total_months += 1

# calculate average rainfall
average_rainfall = total_rainfall / total_months

# display results
print("\n--- Rainfall Summary ---")
print(f"Total months: {total_months}")
print(f"Total rainfall: {total_rainfall} inches")
print(f"Average rainfall per month: {average_rainfall:.2f} inches")

