import pandas as pd

df = pd.read_csv('table.csv')

df.head(100)

# creating a dictionary from CSV file
_dict = df.to_dict()

# checking dictionary
_dict

# getting list of symbols
symbols = [v for v in _dict['Symbol'].values()]

# getting list of atomic numbers
atomic_num = [v for v in _dict['AtomicNumber'].values()]

# create pairs of symbols and atomic numbers
pair1 = zip(symbols, atomic_num)

# making new dictionary
dict1 = {}
for k, v in pair1:
    dict1[k] = v


def input1():
    ''' Basic input function to retrieve atomic number of element which
takes its symbol as input.'''

    print('''\nWelcome to the basic element dictionary. ENTER the name of the
element by its CASE SENSITIVE SYMBOL abbreviation. \n ''')

    while True:
        try:
            key = str(input('Enter symbol of element to retrieve its atomic number: '))
            print("\nThe symbol you entered was:'{}' ".format(key))
            print("The atomic number is: {}".format(dict1[key]))
        except:
            pass


input1()
# print(dict1)
#
# exit(0)
