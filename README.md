# Expense Tracker

A simple Python script that reads in an expenses data in text format and writes it to a CSV file.

## How to run the script

1. Make sure you have Python 3 installed on your machine.
2. Clone this repository to your machine.
3. Navigate to the repository's directory in the terminal/command prompt.
4. Run the following command: `python expense_tracker.py`
5. Enter the name of who paid for the expenses when prompted.
6. Enter the path of the input file that contains the expenses data. The format of the input file should be as follows:
    ```
    HOA: 200
    ComEd: $92
    People gas: 8.7
    ComEd: 120
    ```
7. The script will write the expenses data to a CSV file in the same directory as the input file.

## File structure

- `expense_tracker.py`: The main script that reads in expenses data and writes it to a CSV file.

## Dependencies

- `csv`: The built-in Python library for reading and writing CSV files.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
