import os
import csv

def write_csv(items, filename, who):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([who.upper(), ''])
        writer.writerow(['Item', 'Amount'])
        for item, amount in sorted(items.items()):
            writer.writerow([item, amount])
        writer.writerow(["TOTAL", sum(items.values())])

def read_data(file_path):
    validated_file_path = validate_file_path(file_path)
    data = {}
    with open(validated_file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            item, value = line.strip().split(':')
            item = item.strip().lower()
            value = float(value.strip().strip('$'))

            if item in data:
                data[item] += value
            else:
                data[item] = value
    return data


def validate_file_path(file_path):
    if os.path.isfile(file_path):
        return file_path
    elif os.path.isfile(os.path.join(os.getcwd(), file_path)):
        return os.path.join(os.getcwd(), file_path)
    else:
        raise ValueError("Invalid file path provided")

example = """
HOA: 200
ComEd: $92
People gas: 8.7
ComEd: 120"""
print(f"\nExample of the format expected in the input file: {example}\n")

file_path = input("Enter the path of the input file: ")
who = input("Enter the name of who paid for this: ")
data = read_data(file_path)
filename = file_path.rsplit('/', 1)[-1].split('.')[0] + '.csv'
write_csv(data, filename, who)
print(f"Data has been written to {filename}")
