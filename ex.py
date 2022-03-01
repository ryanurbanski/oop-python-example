
class Student:
    """ Create a Student object"""
    def __init__(self, fname, lname, address):
        self.fname = fname
        self.lname = lname
        self.address = address


class Address:
    """ Create an Address object"""
    def __init__(self, street, city, state, zip):
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip

# Create instance of a 'joey' object -------------------
joeyAddr = Address("1 Electric Ave", "Ashland", "VA", "23005")
joey = Student("Joey", "Menditto", joeyAddr)
        
# Create instance of a 'joceyln' object -------------------
jocAddr = Address("123 Good St.", "Pittsburgh", "PA", "15238")
jocelyn = Student("jocelyn", "Inlay", jocAddr)

# Prints ------------------------------------------------
print(jocelyn)
print(jocelyn.lname)
print(jocelyn.address.state)
print(jocelyn.address.zip)

# Reassign Values ---------------------------------------
print(joey.address.street)
joey.address.street = "123 Home St"
print(joey.address.street)