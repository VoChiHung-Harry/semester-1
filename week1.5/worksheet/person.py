# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self,name,birth):
        if not isinstance(name,str):
            raise TypeError('Name must be a string.')
        if not isinstance(birth,date):
            raise TypeError('Birth must be a date.')
        if name == '':
            raise ValueError('Name must not be empty.')

        self.name = name
        self.birth = birth
 # Implement methods initials() and is_birthday() here
    # Write a constructor here to create and initialize name and
    def initials(self):
        return ''.join(part[0].upper() for part in self.name.split())
    
    # birth fields (see README.md for further details)
    def is_birthday(self):
        today = date.today()
        return (today.month, today.day) == (self.birth.month, self.birth.day)

    # (see README.md for further details)
p = Person('Alan Join Smith', date(2000,11,2))
print(p.initials())
print(p.is_birthday())