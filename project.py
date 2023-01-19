from utils.ledger import Ledger


# --------------------------------------------------
def main():
    ledger = Ledger()

    options_set_1 = {
        'help': {
            'arg_0': ['help', '-h'],
            'func': get_help,
        },
        'remove_all': {
            'arg_0': ['remove_all', '-ra'],
            'func': ledger.remove_all,
        },
        'list': {
            'arg_0': ['list', '-l'],
            'func': ledger.list_items,
        },
        'balance': {
            'arg_0': ['balance', '-b'],
            'func': ledger.balance,
        },
        'export': {
            'arg_0': ['export', '-e'],
            'func': ledger.export_to_csv,
        },
        'save': {
            'arg_0': ['save', '-s'],
            'func': ledger.save,
        }
    }

    options_set_2 = {
        'add': {
            'arg_0': ['add', '-a'],
            'func': ledger.add_item,
            'error': 'Error: must provide an Item and Amount (str: int/float)'
        },
        'deposit': {
            'arg_0': ['deposit', '-d'],
            'func': ledger.deposit,
            'error': 'Error: must provide an Amount (int/float)'
        },
        'withdraw': {
            'arg_0': ['withdraw', '-w'],
            'func': ledger.withdraw,
            'error': 'Error: must provide an Amount (int/float)'
        },
        'change_item': {
            'arg_0': ['change_item', '-ci'],
            'func': ledger.change_item,
            'error':
            'Error: must provide a existing Item and a new one (str: str)'
        },
        'change_amount': {
            'arg_0': ['change_amount', '-ca'],
            'func':
            ledger.change_amount,
            'error':
            'Error: must provide an Existing Item: Amount (str: int/float)'
        },
        'remove_item': {
            'arg_0': ['remove_item', '-ri'],
            'func': ledger.remove_item,
            'error': 'Error: item not found (str)'
        }
    }

    arg_options_set_1 = make_list_arguments(options_set_1)
    arg_options_set_2 = make_list_arguments(options_set_2)

    print('Press -h for help or -q to exist')
    arg_0, arg_1 = get_arguments(input('>> '))
    while arg_0 not in ['-q', 'quit']:

        if arg_0 in arg_options_set_1 and not arg_1:
            func, key = find_fuction(options_set_1, arg_0)
            func()

        elif arg_0 in arg_options_set_2:
            func, key = find_fuction(options_set_2, arg_0)
            if func(arg_1) is False:
                print(options_set_2[key]['error'])

        else:
            print('Incorrect command press -h for help or -q to exit')

        arg_0, arg_1 = get_arguments(input('>> '))
        if arg_0 in ['-q', 'quit']:
            confirm_save = input('Save any changes before exiting[Y/n]? ')
            ledger.save() if confirm_save.lower() == 'y' else None


# --------------------------------------------------
def make_list_arguments(options_set):
    arg_options_set = list()
    for key in options_set:
        arg_options_set += options_set[key]["arg_0"]
    return arg_options_set


# --------------------------------------------------
def get_arguments(command):
    arg_0 = command.split().pop(0).lower() if command else None
    arg_1 = (' '.join(command.split()[1:]).title()
             if len(command.split()) > 1 else '')
    return arg_0, arg_1


# --------------------------------------------------
def find_fuction(options_set, arg_0):
    for key in options_set:
        if arg_0 in options_set[key]["arg_0"]:
            return options_set[key]['func'], key


# --------------------------------------------------
def get_help():
    usage = 'Usage: python project.py\n\n'
    title = 'Creates and keeps a simple ledger\n\n'
    optional_args = """Options:
  -h, help            show this help message
  -q, quit            exist the this application
  -d, deposit         add cash to ledger
  -w, withdraw        subtract cash from ledger
  -a, add             add item to ledger
  -ci, change_item    change ledger item name
  -ca, change_amount  change ledger item amount
  -ri, remove_item    remove an item from ledger
  -ra, remove_all     remove all items from ledger
  -l, list            print the ledger
  -b, balance         print the current balance
  -e, export          export current ledger to 'ledger.csv'
  -s, save            save current ledger in the hard disk"""
    print(usage + title + optional_args)


# --------------------------------------------------
if __name__ == "__main__":
    main()
