import json
import random

def update_condition_list(data):
    for item in data:
        item["condition_list"] = "new" if random.random() > 0.5 else "old"
    return data

def main():
    input_file = "data.json"
    output_file = "output_file.json"

    with open(input_file, "r") as file:
        json_data = json.load(file)

    updated_data = update_condition_list(json_data)

    with open(output_file, "w") as file:
        json.dump(updated_data, file, indent=2)

if __name__ == "__main__":
    main()

