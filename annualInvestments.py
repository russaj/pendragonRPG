import random
import os
import csv
import json

# Define the function to calculate net income for a single manor
def calculate_net_income(year, manor_name, harvest_income, raid_income, investments):
    total_investment_costs = 0
    total_investment_income = 0

    # Calculate the total investment costs and income
    for investment in investments:
        total_investment_costs += investment["annual_cost"]
        total_investment_income += random.randint(1, investment["dice_size"]) * investment["annual_income_per_unit"]

    # Calculate the net income
    net_income = harvest_income + raid_income + total_investment_income - total_investment_costs

    # Create a dictionary to store the results
    results = {
        "year": year,
        "manor_name": manor_name,
        "harvest_income": harvest_income,
        "raid_income": raid_income,
        "total_investment_costs": total_investment_costs,
        "total_investment_income": total_investment_income,
        "net_income": net_income
    }

    # Save the results to a file
    filename = manor_name + ".py"
    try:
        with open(filename, "a") as f:
            f.write(", " + str(results))
    except FileNotFoundError:
        with open(filename, "w") as f:
            f.write(str(results))
    return results

# Write the results to a CSV file
    fieldnames = ["year", "manor_name", "harvest_income", "raid_income", "total_investment_costs", "total_investment_income", "net_income"]
    if os.path.exists(filename + ".csv"):
        with open(filename + ".csv", "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writerow(results)
    else:
        with open(filename + ".csv", "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(results)

    # Write the results to a JSON file
    if os.path.exists(filename + ".json"):
        with open(filename + ".json", "a") as f:
            json.dump(results, f)
    else:
        with open(filename + ".json", "w") as f:
            json.dump(results, f)

# Define a function to get user input for a single investment
def get_investment():
    while True:
        try:
            investment_name = input("Enter investment name: ")
            annual_cost = float(input("Enter annual cost of investment: "))
            annual_income_per_unit = float(input("Enter annual income per unit of investment: "))
            dice_size = int(input("Enter dice size for investment income (e.g. 4 for a 4-sided die): "))
            break
        except ValueError:
            print("Invalid input. Please enter a number for the cost, income, and dice size.")
    investment = {
        "investment_name": investment_name,
        "annual_cost": annual_cost,
        "annual_income_per_unit": annual_income_per_unit,
        "dice_size": dice_size
    }
    return investment

# Define a function to get user input for multiple investments
def get_investments():
    investments = []
    while True:
        add_investment = input("Add an investment? (y/n): ")
        if add_investment.lower() == "n":
            break
        investment = get_investment()
        investments.append(investment)
    return investments

# Get user input for the year, manor name, and income sources
while True:
    try:
        year = int(input("Enter the year: "))
        break
    except ValueError:
        print("Invalid input. Please enter a whole number for the year.")
manors = []
while True:
    manor_name = input("Enter the name of a manor: ")
    while True:
        try:
            harvest_income = float(input("Enter the harvest income for the manor: "))
            raid_income = float(input("Enter the raid income for the manor: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number for the harvest and raid income.")

    investments = get_investments()
    manor = {
        "manor_name": manor_name,
        "harvest_income": harvest_income,
        "raid_income": raid_income,
        "investments": investments
    }
    manors.append(manor)
    add_manor = input("Add another manor? (y/n): ")
    if add_manor.lower() == "n":
        break

# Calculate net income for each manor and store results in a list of dictionaries
results = []
for manor in manors:
    result = calculate_net_income(year, manor["manor_name"], manor["harvest_income"], manor["raid_income"], manor["investments"])
    results.append(result)

# Print the results
for result in results:
    print(result)
