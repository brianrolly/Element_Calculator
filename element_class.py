class Atom:
    def __init__(self, label):
        self.label = label

    def __repr__(self):
        return str(self.label)

    def __add__(self, other):
        return Molecule([self, other])


class Molecule:
    def __init__(self, atoms):
        if type(atoms) is list:
            self.atoms = atoms

    def __repr__(self):
        # returns the list as a string
        return str(self.atoms)

        # returns the string without the list but is limited to two items
        # return (f"{self.atoms[0].label}{self.atoms[1].label}")
        # returns string without list
        # return "{}{}".format(*self.atoms)


sodium = Atom("Na")
chlorine = Atom("Cl")
#salt = Molecule([sodium, chlorine])
salt = sodium + chlorine
print(salt)
