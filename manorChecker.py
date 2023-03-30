import os

def print_dossier(manor_data):
    print("\n" + "=" * 50)
    print("Dossier for " + manor_data[0]["manor_name"])
    print("=" * 50 + "\n")
    for year_data in manor_data:
        print(f"Year: {year_data['year']}")
        print(f"Harvest Income: {year_data['harvest_income']}")
        print(f"Raid Income: {year_data['raid_income']}")
        print(f"Total Investment Costs: {year_data['total_investment_costs']}")
        print(f"Total Investment Income: {year_data['total_investment_income']}")
        print(f"Net Income: {year_data['net_income']}\n")

# Get manor name from user
manor_name = input("Enter the name of the manor: ")

# Load data from corresponding file
file_name = f"{manor_name}.py"
if os.path.exists(file_name):
    with open(file_name, "r") as f:
        manor_data_str = f.read()
    manor_data_list = eval(manor_data_str)
    net_income_sum = sum(year_data['net_income'] for year_data in manor_data_list)
    print_dossier(manor_data_list)
    print(f"Total Net Income: {net_income_sum}")
else:
    print(f"No data found for {manor_name}")
