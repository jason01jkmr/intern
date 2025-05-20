import pandas as pd
import os
csv_path = os.path.join(os.path.dirname(__file__), "Employee.csv")
emp = pd.read_csv(csv_path)


class Employees():
    def __init__(self, emp=emp):
        self.emp = emp

    def emp_info(self):
        return self.emp.head(5).to_dict(orient="records")

    def gender_div(self):
        return self.emp["Sex"].value_counts().to_dict()