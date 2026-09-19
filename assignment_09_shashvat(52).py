import csv
import json
# Define input CSV file and output JSON file
input_file = "input.csv"
output_file = "output.json"
# Open the CSV file and read its contents
with open(input_file, "r") as file:
    reader = csv.DictReader(file)
    # Convert CSV data into a list of dictionaries
    data = list(reader)
# Write the list of dictionaries to a JSON file
with open(output_file, "w") as file:
    json.dump(data, file, indent=4)
print("CSV data successfully converted to JSON.")