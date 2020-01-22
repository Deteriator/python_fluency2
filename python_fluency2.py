import re

def halved(list):
    return [ number/2 for number in list]
    
print(halved([2,4,6,8,10]))

def only_positive(list):
    return [num for num in list if num > 0]
    
print(only_positive([-2,4,6,-8,10]))

def sum(list):
    return sum(list)
    
def stripped_strings(list):
    return [ re.sub('\W', '', string) for string in list ]

print(stripped_strings(["123456jghfj----"]))
    
def find_special(list):
    return [ i for i in range(len(list)) if list[i] == "special"]
    
print(find_special(['spec','special']))
    
def valid_contacts(list):
    return [contact for contact in list if len(contact['phone_number']) == 10]

def contact_names(list):
    return [ contact['name'] for contact in list]