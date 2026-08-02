def validate_name_and_contact(func):
    def wrapper(name,contact_number):
        if not name or not isinstance(name,str):
            return "name must be a  non-empty string"

        if len(contact_number)!= 10 or not contact_number.isdigit():
            return"contact number must be a 10-digit number"

        return func(name,contact_number)
    return wrapper

@validate_name_and_contact

def registar_user(name,contact_number):
    return f"user (name) with contact number (contact_number) has been successfully registered"

print(registar_user("dhruv","1234578956"))
print(registar_user("jay","4567895315"))
print(registar_user("","12345"))
print(registar_user("raj","12abc78956"))
