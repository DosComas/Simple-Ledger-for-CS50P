# SIMPLE LEDGER

#### VIDEO DEMO: <https://youtu.be/I0n4CSD318I>


#### INTRODUCTION:

For the final project of CS50's Introduction to Programming with Python, I created an app that works like a ledger.

It allows the user to enter items and their values in the app, which handles the data using a dictionary format in which the item name is used as the key {item:1 value, item2: value, ...}. Also, it allows the user to modify the stored item's names and values, save them to the hard disk in a JSON format and export the information to a CSV file.


#### HOW IT WORKS:

The app is executed by running 'project.py' with all of the user interaction with the app handled by him writing in the command line interface.

This is the help message that can be printed by typing 'help' or '-h' in the console when the app is open. It shows the different functions that the user can invoke.

```
Usage: python project.py

Creates and keeps a simple ledger

Options:
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
  -s, save            save current ledger in the hard disk
```

If the user types an 'Option' not in the help message, the app will print the following error message and allow the user to try entering an option again.

```
Incorrect command press -h for help or -q to exit
```

For the options of 'add', and 'change_amount', the user must enter the item and value pair in this format 'str: int/float'. If the format is incorrect, the app will print an error message and allow the user to try again. 

Likewise, for 'deposit' and 'withdraw', the valid format is int/float, for 'change_item', the format is 'str: str', and for 'remove_item' is 'str'.

Example of the error message for the 'add' function.

```
Error: must provide an Item and Amount (str: int/float)
```

If the 'change_item' option is used and the new article name already exists, it will print the following confirmation message.

```
The item {new_item} already exists. Press Y to merge the Items or n to cancel[Y/n]: 
```

For the options that delete an existing item, 'remove_item' and 'remove_all', the user will be required to confirm the operation.

Example of the message for the 'remove_item' function.

```
'The Item will be permanently deleted. Confirm[Y/n]: '
```

The user can choose to save the changes at any time using the 'save' option and will be prompted for confirmation before saving the data to the JSON file.

The 'balance' option is used to get the current sum of all the items in the ledger. The 'list' option can get a list of all the items in the ledger, and the 'remove_all' option will empty the ledger by removing all items and their values. 

If the 'quit' option is used after entering a command, the application will ask the user if he wants to save the changes. This data will be saved in 'utils\ledger.json', and the user can choose to save the changes at any time by typing 'save'. 

Also, the user can choose to export the data to a CSV file. This file will be created automatically with the name ledger.csv. Warning, if the file already exists, the application will overwrite it and delete the existing data.


#### REQUIRIMENTS:

The app requires python 3 and the tabulate ver. 0.9.0 library to work.


#### UNIT TESTS INCLUDED:

Also, in 'test_project.py', I included unit test for all the functions in 'preject.py', which is the user interface module, and the functions in 'utils\ledger.py' that require the user to enter item and value pairs.