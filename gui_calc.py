''' Refactoring calculator.py to have a GUI. '''

import tkinter as tk
import pandas as pd

# CSV HANDLING BELOW #

# to open csv file with pandas
df = pd.read_csv('table.csv')

# creating a dictionary from CSV file
_dict = df.to_dict()

# getting list of symbols
symbols = [v for v in _dict['Symbol'].values()]

# getting list of atomic numbers
atomic_num = [v for v in _dict['AtomicNumber'].values()]

# getting list of element names
el_name = [v for v in _dict['Element'].values()]

# create sets of symbols and atomic numbers
set = zip(symbols, el_name, atomic_num)

# making new dictionary
dict1 = {}
for key, name, num in set:
    dict1[key] = name, num

# GUI BELOW #


def refresh():
    ''' Creates command for restart_button to refresh the page. '''

    root.destroy()
    start()


def restart_button():
    ''' Setting the refresh button. '''

    button2 = tk.Button(text="Refresh", command=refresh)
    canvas1.create_window(350, 200, window=button2)  # 100, 190


def retrieve(key):
    ''' Takes the input and uses it as a dictionary to access the desired
    values and outputs them. '''

    try:
        canvas1.create_text(
            350, 255, text="The element of that symbol is: {}".format(dict1[key][0]))
        canvas1.create_text(350, 275, text="The atomic number is: {}".format(dict1[key][1]))
    except KeyError:
        canvas1.create_text(350, 255, text="No known element with this symbol!")
    # create new button here
    restart_button()


def get_key():
    ''' Receives the input and stores it in the "key" variable and then passes
    that variable to the retrieve() function call to get the element name and
    its atomic number from the dict1 dictionary '''

    key = entry1.get()
    message1 = 'The symbol you entered was: {}'.format(key)
    label1 = tk.Label(root, text=message1)
    canvas1.create_window(350, 235, window=label1)
    retrieve(key)

# TKINTER GUI CREATION STARTS HERE #


def start():
    ''' Initiates the program and creates the GUI and runs until line 96 calls
    the get_key() function and then continues in a chain of functions. '''

    # establish root
    global root
    root = tk.Tk()

    # make canvas
    global canvas1
    canvas1 = tk.Canvas(root, width=700, height=400)
    canvas1.create_text(
        350, 80, text="Welcome to the basic element dictionary. ENTER the name")
    canvas1.create_text(
        350, 100, text="of the element by its CASE SENSITIVE SYMBOL")
    canvas1.create_text(350, 120, text="abbreviation to retrieve its atomic number.")
    canvas1.pack()

    # creating entry point for input
    global entry1
    entry1 = tk.Entry(root)
    # linking window with entry object
    canvas1.create_window(350, 170, window=entry1)

    # create button that executes get_key()
    button1 = tk.Button(text='ENTER', command=get_key)
    canvas1.create_window(350, 200, window=button1)

    # keep the gui window up
    root.mainloop()


# PROGRAM GUI RUNS FROM HERE #
start()
