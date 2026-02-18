import pandas as pd

pd.DataFrame()
class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

omsApplication = RailwayForm()
omsApplication.name = "Om"
omsApplication.train = "Rajdhani Express"
omsApplication.printData()