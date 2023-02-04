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
    data = {}
    with open(file_path, 'r') as file:
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

example = """
HOA: 200
ComEd: $92
People gas: 8.7
ComEd: 120"""
print(f"\nExample of the format expected in the input file: {example}\n")

who = input("Enter the name of who paid for this: ")
file_path = input("Enter the path of the input file: ")
data = read_data(file_path)
filename = file_path.rsplit('/', 1)[-1].split('.')[0] + '.csv'
write_csv(data, filename, who)
print(f"Data has been written to {filename}")
