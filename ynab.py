import csv
import json

# TODO implement delta transactions

def import_txs(filename):
    with open(filename) as file:
        tx_response = json.load(file)
    return tx_response["data"]["transactions"]

if __name__ == "__main__":
    transactions = import_txs("transactions.json")

    with open("transactions.csv", "w") as csv_file:
        csv_writer = csv.writer(csv_file)
        keys = list(transactions[0].keys())
        for t in transactions:
            csv_writer.writerow([t[k] for k in keys])

    print("done")

