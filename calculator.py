import pandas as pd

# to open csv file with pandas
df = pd.read_csv('table.csv')

# to check format of table.csv
df.head(20)

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

# A basic menu to give the user an option to quit or keep looping


def menu():
    while True:
        print("\nWould you like to enter another symbol?")
        answer = str(input("y/n ")).lower()
        if 'y' in answer:
            print('\n')
            return True
        elif 'n' in answer:
            exit(0)


def input1():
    ''' Basic input function to retrieve atomic number of element which
takes its symbol as input.'''

    print("\nWelcome to the basic element dictionary. ENTER the name of")
    print("the element by its CASE SENSITIVE SYMBOL abbreviation to")
    print("retrieve its atomic number.\n")

    while True:
        try:  # the key will be indexed into the dictionary
            key = str(input('Enter symbol of element: '))
            # if key
            print("\nThe symbol you entered was:'{}' ".format(key))
            print("\nThe element of that symbol is:'{}'".format(dict1[key][0]))
            print("The atomic number is: {}\n".format(dict1[key][1]))
            if menu():
                continue
        except KeyError:
            print('Please enter a valid symbol from the periodic table with')
            print('proper capitalization.\n')
            continue


input1()
