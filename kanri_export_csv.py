import json
import csv
from itertools import zip_longest

def kanban_to_table_csv(json_file, csv_file):
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    board = {}
    for column in data.get("columns", []):
        title = column.get("title", "Unknown")
        names = [card.get("name", "").strip() for card in column.get("cards", [])]
        board[title] = names

    rows = zip_longest(*board.values(), fillvalue="")

    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(board.keys())
        writer.writerows(rows)

    print(f"CSV file saved as {csv_file}")

kanban_to_table_csv("C:\\kanri_export.json", "C:\\kanban_table.csv")
