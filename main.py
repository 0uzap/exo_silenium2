from fastapi import FastAPI

# init app
app = FastAPI()

@app.get("/")
def home():
    return "hello World!"

@app.get("/{number}")
def return_double(number: int):
    return get_double(number)

def get_double(number: int):
    return number * 2

# c'est un faux truc je veux juste une modif avec le reste