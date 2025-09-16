import datetime
import csv
from tabulate import tabulate
from database_manage import insert

dataset = ["CBC", "Fasting Blood Suger", "Lipid Profile", "LFT", "HBsAg"]


class data_logic:
    def data():
        global dataset
        return dataset 

    def datev():
        today = datetime.date.today()
        return today
    
    def save_data(tests: list) -> None: 
        temp_data = []
        for i in tests:
            temp_data.append(i)

        insert(temp_data[0], temp_data[1], temp_data[2], temp_data[3], temp_data[4], temp_data[5], temp_data[6], temp_data[7])
        
        

    def calculate():
        ...

    def pdf():
        ...

    def user_data():
        ...


if __name__=='__main__':
    data_logic()