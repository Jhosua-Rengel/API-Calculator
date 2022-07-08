'''
API Calculator wiht code python by: Jhosua-Rengel
'''
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Data(BaseModel):
    """Class to store data of the POST."""
    number_list: list[float] # This is a list to sum values and take the average.
    number_one: float # This is my first value to perform my calculations.
    number_two: float # This is my second value to perform my calculations.
    def search1(self):
        """This function is not necesary 'added for nomenclature only'.'"""
        print(f"{self.number_one} is a value searching.")
    def search2(self):
        """This function is not necesary 'added for nomenclature only'."""
        print(f"{self.number_two} is a value searching.")

def numbers_list(post:Data):
    """This function take the values sent from the endpoint, turns
    it into a dictionary and get the key 'numbers_list' """
    build_dict = post.dict()
    take_number_list = build_dict.get('number_list')
    return take_number_list

@app.get('/') # Welcome
def welcome():
    """This function retorn a welcome to the user."""
    return {"Greting":"Welcome to my API"}

@app.post('/average') # Average
def extract_average(post:Data):
    """This function return the result average of the number_list."""
    uses_func_number_list = numbers_list(post)
    take_average = sum(uses_func_number_list) / len(uses_func_number_list)
    return "The result of the average is:",round(take_average,2)

@app.post('/subtract') # Substract
def extract_subtract(post:Data):
    """This function return the result substract of the first and second value."""
    subtract = post.number_one - post.number_two
    return {"The result of the substract is:",(subtract)}

@app.post('/sum') # Sum
def extract_sum(post:Data):
    """This function return the result sum of the first and second value."""
    suma = post.number_one + post.number_two
    return {"The result of the sum is:",(suma)}

@app.post('/multiply') # Multiply
def extract_multiply(post:Data):
    """This function return the result multiply of the first and second value"""
    multiply = post.number_one * post.number_two
    return {"The result of the multiply is:",(multiply)}

@app.post('/division') # Division
def extract_division(post:Data):
    """This function return the result division of the first and second value"""
    division = post.number_one / post.number_two
    return {"The result of the division is:",round(division,2)}
