class InvalidAgeError(Exception):

    def __init__(self,age,message="age must be 18 or above"):
        self.age=age
        self.message=message
        super().__init__(f"{message}. given age : {age}")

def register_user(age):
    if age<18:
        raise InvalidAgeError(age)

    print("user registered successfully")


try:
    registered_user(25)
except InvalidAgeError as e:
    print(f"error")
