import datetime


dataset = ["CBC", "Fasting Blood Suger", "Lipid Profile", "LFT", "HBsAg"]


class data_logic:
    def data():
        global dataset
        return dataset 

    def datev():
        today = datetime.date.today()
        return today
    
    def calculate(tests: str) -> None:

        print(tests)




if __name__=='__main__':
    data_logic()