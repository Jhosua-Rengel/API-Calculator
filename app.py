'''
API Calculator wiht code python by: Jhosua-Rengel
'''
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Data(BaseModel):
    """Class documentation string."""
    number_list: list[float] # This is a list to sum values and take the average.
    number_one: float # This is my value two to perform my calculations.
    number_two: float # This is my value two to perform my calculations.
    def search1(self):
        """Function documentation string."""
        print(f"{self.number_one} is a value searching.")
    def search2(self):
        """Function documentation string."""
        print(f"{self.number_two} is a value searching.")

def numbers_list(post:Data):
    """This function take the values sent from the endpoint, turns
    it into a dictionary and get the key 'numbers_list'"""
    get_dict = post.dict()
    take_list = get_dict.get('number_list')
    return take_list

@app.get('/') # Welcome
def welcome():
    """Function documentation string."""
    return {"Greting":"Welcome to my API"}

@app.post('/average') # Average
def extract_average(post:Data):
    """Function documentation string."""
    uses = numbers_list(post)
    added = sum(uses) / len(uses)
    return "The result of the average is:",round(added,2)

@app.post('/subtract') # Substract
def extract_subtract(post:Data):
    """Function documentation string"""
    subtract = post.number_one - post.number_two
    return {"The result of the substract is:",(subtract)}

@app.post('/sum') # Sum
def extract_sum(post:Data):
    """Function documentation string."""
    suma = post.number_one + post.number_two
    return {"The result of the sum is:",(suma)}

@app.post('/multiply') # Mulriply
def extract_multiply(post:Data):
    """Function documentation string."""
    multiply = post.number_one * post.number_two
    return {"The result of the multiply is:",(multiply)}

@app.post('/division') # Division
def extract_division(post:Data):
    """Function documentation string."""
    division = post.number_one / post.number_two
    return {"The result of the division is:",round(division,2)}
