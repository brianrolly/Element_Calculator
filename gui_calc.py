''' Refactoring calculator.py to have a GUI. '''

import tkinter as tk
import pandas as pd

# CSV HANDLING BELOW #

# to open csv file with pandas
df = pd.read_csv('table.csv')

# to check format of table.csv
df.head(20)

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


def get_key():
    key = entry1.get()
    message1 = 'The symbol you entered was: {}'.format(key)
    label1 = tk.Label(root, text=message1)
    canvas1.create_window(350, 235, window=label1)
    try:
        canvas1.create_text(
            350, 255, text="The element of that symbol is: {}".format(dict1[key][0]))
        canvas1.create_text(350, 275, text="The atomic number is: {}".format(dict1[key][1]))
    except KeyError:
        canvas1.create_text(350, 255, text="No known element with this symbol!")
    # create new button here
    restart_button()
# "The atomic number is: {}\n".format(dict1[key][1])


def start():

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


# Program GUI runs from here
start()
