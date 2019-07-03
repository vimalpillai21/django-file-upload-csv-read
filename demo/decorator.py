class ValidationError(Exception):
    def __init__(self, message, errors):

        # Call the base class constructor with the parameters it needs
        super().__init__(message)

        # Now for your custom code...
        self.errors = errors

def my_decorator(func):
    def wrapper(*args,**kwargs):
        for index,value in enumerate(args):
            if index == 0 and value<=3:
                raise ValidationError("Number Can\'t be less than or equal to"+
                 " 3",200)
            else:
                print("Addition of Numbers")
                func(*args,**kwargs)
                print("Addition Complete")
    return wrapper

@my_decorator
def add(num1,num2):
    print(f"Result After Addition - {num1+num2}")

try:
    x,y = map(int,input("Enter two numbers -\t").split())
    add(x,y)
except ValidationError as e:
    print(str(e))
finally:
    print('finally executed')
