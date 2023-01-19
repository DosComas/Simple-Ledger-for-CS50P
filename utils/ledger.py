import re
import csv
import json
from tabulate import tabulate


class Ledger:

    # --------------------------------------------------
    def __init__(self):
        with open(r'utils\ledger.json', 'r') as file:
            self.ledger = json.load(file)

    # --------------------------------------------------
    def __repr__(self):
        return f'<ledger {self.ledger}>'

    # --------------------------------------------------
    def save(self):
        with open(r'utils\ledger.json', 'w') as file:
            json.dump(self.ledger, file)

    # --------------------------------------------------
    def add_item(self, args):
        if match := re.match(r'^(.+): ?(\d+(?:\.?\d{1,2})?)$', args):
            key = match.group(1)
            val = -float(match.group(2))
            operation = round(self.ledger.get(key, 0) + val, 2)
            self.ledger[key] = operation
            return True
        return False

    # --------------------------------------------------
    def deposit(self, args):
        if match := re.match(r'^(\d+(?:\.?\d{1,2})?)$', args):
            val = float(match.group(1))
            operation = round(self.ledger.get('Cash', 0) + val, 2)
            self.ledger['Cash'] = operation
            return True
        return False

    # --------------------------------------------------
    def withdraw(self, args):
        if match := re.match(r'^(\d+(?:\.?\d{1,2})?)$', args):
            val = -float(match.group(1))
            operation = round(self.ledger.get('Cash', 0) + val, 2)
            self.ledger['Cash'] = operation
            return True
        return False

    # --------------------------------------------------
    def change_item(self, args):
        if match := re.match(r'^(.+): ?(.+)$', args):
            key_old = match.group(1)
            key_new = match.group(2)

            if key_old in self.ledger and key_new not in self.ledger:
                self.ledger[key_new] = self.ledger.pop(key_old)
                return True
            elif key_old in self.ledger and key_new in self.ledger:
                confirm_merge = input(
                    f'The Item {key_new} already exists. '
                    'Press Y to merge the Items or n to cancel[Y/n]: ')
                if confirm_merge.lower() == 'y':
                    amount = self.ledger[key_new] + self.ledger[key_old]
                    self.ledger[key_new] = amount
                    self.ledger.pop(key_old)
                return True
        return False

    # --------------------------------------------------
    def change_amount(self, args):
        if match := re.match(r'^(.+): ?(\d+(?:\.?\d{1,2})?)$', args):
            key_old = match.group(1)
            val_new = -float(match.group(2))
            if key_old in self.ledger:
                self.ledger[key_old] = val_new
                return True
        return False

    # --------------------------------------------------
    def remove_item(self, key):
        if key in self.ledger:
            confirm = input(
                'The Item will be permanently deleted. Confirm[Y/n]: ')
            self.ledger.pop(key) if confirm.lower() == 'y' else None
            return True
        return False

    # --------------------------------------------------
    def remove_all(self):
        confirm = input('All Items will be deleted. Confirm[Y/n]: ')
        self.ledger = {} if confirm.lower() == 'y' else None

    # --------------------------------------------------
    def list_items(self):
        items = {key: val for key, val in self.ledger.items() if val != 0}
        total = sum(items.values())
        headers = ('Items:', 'Amount:')

        if 'Cash' in items:
            cash = ("Cash", items.pop("Cash"))
            table = sorted(items.items())
            table.insert(0, cash)
        else:
            table = sorted(items.items())
        table.append(('Total Balance', total))

        print(tabulate(table, headers, floatfmt=".2f", tablefmt="github"))

    # --------------------------------------------------
    def balance(self):
        total = sum(self.ledger.values())
        if total < 0:
            total_balance = f'Debit of -${-total:.2f}'
        elif total > 0:
            total_balance = f'Credit of ${total:.2f}'
        else:
            total_balance = 'Account in Balance'
        print(total_balance)

    # --------------------------------------------------
    def export_to_csv(self):
        header = ['Items', 'Amounts']
        total = ['Balance', sum(self.ledger.values())]

        with open(r'ledger.csv', 'w', newline='') as file:
            writer = csv.writer(file, dialect='excel')
            writer.writerow(header)
            for row in self.ledger.items():
                writer.writerow(row)
            writer.writerow(total)

    # --------------------------------------------------
    def set_ledger_for_testing(self, data):
        self.ledger = data

    # --------------------------------------------------
    def get_ledger_for_testing(self):
        return self.ledger
