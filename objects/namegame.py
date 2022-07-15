#Create a class called Name. Name should have two attributes
#(instance variables): first_name and last_name. Make sure
#the variable names match those words. Both will be strings.
#
#Name should have a constructor with two required parameters,
#one for each of those attributes (first_name and last_name,
#in that order).
#
#Name should also have two methods. The first should be
#called find_printed_name, and should return the first and
#last name with a space in between, e.g. "David Joyner". The
#second method should be called find_sortable_name, and
#should return the last name, then a comma and space, and
#then only the first initial, e.g. "Joyner, D".
#
#Neither sortable_name nor printed_name should be attributes:
#both should be created and returned when those methods are
#called. Neither method will have any parameters besides self.

class Name:
    """
    A class that recibes a name in string form.
    """
    def __init__(self, first_name, last_name):
        """
        Receives two attributes, first_name and last_name
        to be initiated with the class
        
        Args:
            first_name (string) = The first name
            last_name (string) = The last name
        """
        self.first_name = first_name
        self.last_name = last_name

    def find_printed_name(self):
        """
        Using the class attributes, returns the first and
        last name with a space in between, e.g. "David Joyner"
        
        Returtns:
            (string) = A string combining the first and last
                       name with a space in between.
        """
        return "{} {}".format(self.first_name,self.last_name)

    def find_sortable_name(self):
        """
        Using the class attributes, returns the last name,
        then a comma and space, and then only the first
        initial, e.g. "Joyner, D".
        
        Returtns:
            (string) = A string combining the last name and the
                       first letter of the first name wit a space
                       and a comma in between.
        """
        return "{}, {}".format(self.last_name,self.first_name[0])