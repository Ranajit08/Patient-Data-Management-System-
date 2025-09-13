import datetime
import csv
from tabulate import tabulate


dataset = ["CBC", "Fasting Blood Suger", "Lipid Profile", "LFT", "HBsAg"]


class data_logic:
    def data():
        global dataset
        return dataset 

    def datev():
        today = datetime.date.today()
        return today
    
    def save_data(tests: list) -> None:
        id = 0
        try:
            with open("patient_data.csv", 'r', newline='') as file:
                csv_data = csv.reader(file)
                data = list(csv_data)
                id += len(data)
        except:
            return False
        
        temp_data = []
        for i in tests:
            temp_data.append(i)
        try:
            with open("patient_data.csv", "a", newline='') as file1:
                write = csv.writer(file1)
                write.writerow([id, temp_data[0], temp_data[1], temp_data[2], temp_data[3], temp_data[4], temp_data[5], temp_data[6], temp_data[7]])
                file1.close()
                return True
        except:
            return False
        

    def calculate():
        ...

    def pdf():
        ...

    def user_data():
        with open('patient_data.csv') as f:
            reader = csv.reader(f)
            g = list(reader)
        d = tabulate(g, headers="firstrow", tablefmt='grid')
        return d


if __name__=='__main__':
    data_logic()