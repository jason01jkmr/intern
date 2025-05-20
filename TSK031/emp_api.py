from fastapi import FastAPI, Depends
from TSK031.emp import Employees

app = FastAPI()

def get_employees():
    return Employees()

@app.get("/")
def read_root(info: Employees = Depends(get_employees)):
    return info.emp_info()

@app.get("/gender")
def gender(info: Employees = Depends(get_employees)):
    return info.gender_div()
