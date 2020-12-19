import pandas as pd

rawPath = "/home/ec2-user/survey_project/data/raw/"
processedPath = "/home/ec2-user/survey_project/data/processed/"
interimPath = "/home/ec2-user/survey_project/data/interim/"

#define helper functions

def makeColumns(columns, survey):
    global data
    for column in columns:
        if column:
            #print(column)
            data[column.lower()] = None


data = pd.read_csv(interimPath + "master_longDataset.0.0.1.csv", encoding = "ISO-8859-1")


#read  datasets
wvsEvsData = pd.read_csv(processedPath + "regional_dimensions_all.0.0.3.csv")
americasData = pd.read_csv(processedPath + "regional_dimensions_americas.0.0.3.csv", encoding = "ISO-8859-1")
GBS1Data = pd.read_csv(processedPath + "regional_dimensions_GBS.0.0.2.csv")
#GBS2Data = pd.read_csv(processedPath + "regional_dimensions_GBSII0.0.1.csv")

#make columns
#add survey column
data["survey"] = None
data["year"] = None
#add question columns
makeColumns(wvsEvsData.columns, "WVS_EVS")
makeColumns(americasData.columns, "americas.barometer")
makeColumns(GBS1Data.columns, "GBS1")
#makeColumns(GBS2Data.columns,"GBS2")

data.to_csv(processedPath+"master_longDataSet.0.0.2.csv")
