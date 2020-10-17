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

# getting list of element names
el_name = [v for v in _dict['Element'].values()]

# create pairs of symbols and atomic numbers
pair = zip(symbols, el_name, atomic_num)

# making new dictionary
dict1 = {}
for key, name, num in pair:
    dict1[key] = name, num


def input1():
    ''' Basic input function to retrieve atomic number of element which
takes its symbol as input.'''

    print("\nWelcome to the basic element dictionary. ENTER the name of")
    print("the element by its CASE SENSITIVE SYMBOL abbreviation to")
    print("retrieve its atomic number.\n")

    while True:
        try:
            key = str(input('Enter symbol of element: '))
            print("\nThe symbol you entered was:'{}' ".format(key))
            print("\nThe element for that symbol is:'{}'".format(dict1[key][0]))
            print("The atomic number is: {}".format(dict1[key][1]))
        except ValueError:
            continue


input1()
# print(dict1)
#
# exit(0)
