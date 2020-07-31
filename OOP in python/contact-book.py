#storing objects in a dictionary
#a script which accepts values from the user 
# and prints final information as key:value pairs

class ContactDetails:
    def __init__ (self, contact_name, contact_email, contact_address):
        self.__name = contact_name
        self.__email = contact_email
        self.__address = contact_address
    
    #set the values of contact_name, contact_email and contact_address
    def set_name(self, contact_name):
        self.__name = contact_name
    
    def set_email(self, contact_email):
        self.__email = contact_email
    
    def set_address(self, contact_address):
        self.__address = contact_address
    
    #get the values of contact_name, contact_email and contact_address
    def get_name(self):
        return self.__name
    
    def get_email(self):
        return self.__email
    
    def get_address(self):
        return self.__address
    
    #def a __str__ to return the obejct as a string
    def __str__(self):
        return 'The name is ' + self.__name + ', \n' \
                'lives at ' + self.__address + ', \n' \
                'and has an email with address: ' + self.__address
