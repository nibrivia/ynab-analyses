import csv
import json

# TODO implement delta transactions

def import_txs(filename = "transactions.json"):
    with open(filename) as file:
        tx_response = json.load(file)
    return tx_response["data"]["transactions"]

def txs_to_csv(transactions, filename = "transactions.csv"):
    with open(filename, "w") as csv_file:
        writer = csv.writer(csv_file)
        keys = list(transactions[0].keys())

        # Headers
        writer.writerow(keys)
        # Rows
        for t in transactions:
            writer.writerow([t[k] for k in keys])


if __name__ == "__main__":
    transactions = import_txs("transactions.json")
    txs_to_csv(transactions = transactions, filename = "transactions.csv")
    print("done")

