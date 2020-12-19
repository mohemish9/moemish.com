import pandas as pd

rawPath = "/home/ec2-user/survey_project/data/raw/"
processedPath = "/home/ec2-user/survey_project/data/processed/"
interimPath = "/home/ec2-user/survey_project/data/interim/"

#define helper functions

def makeColumns(columns ,survey):
    global data
    global surveys

    for wave in surveys[survey]:
        for column in columns:
            data[column + "." + survey + "." + str(wave)] = None


data = pd.read_csv(interimPath + "master_dataset.0.0.1.csv", encoding = "ISO-8859-1")


surveys = {"wvs":[1,2,3,4,5,6],
            "evs":[1,2,3,4],
            "americas.barometer": [2004,2006,2008,2010,2012,2014],
            "gbs1.Afrobarometer": [3,4],
            "gbs2.Afrobarometer":[5],
            "gbs1.ArabBarometer": [2],
            "gbs2.ArabBarometer": [3],
            "gbs1.Latinobarometer": [2005,2010],
            "gbs2.Latinobarometer": [2013]}


#read  datasets
wvsEvsData = pd.read_csv(processedPath + "regional_dimensions_all.0.0.3.csv")
americasData = pd.read_csv(processedPath + "regional_dimensions_americas.0.0.3.csv", encoding = "ISO-8859-1")
GBS1Data = pd.read_csv(processedPath + "regional_dimensions_GBS.0.0.2.csv")
GBS2Data = pd.read_csv(processedPath + "regional_dimensions_GBSII0.0.1.csv")

#make columns
makeColumns(wvsEvsData.columns,"wvs")
makeColumns(wvsEvsData.columns,"evs")
makeColumns(americasData.columns,"americas.barometer" )
makeColumns(GBS1Data.columns, "gbs1.Afrobarometer")
makeColumns(GBS1Data.columns, "gbs1.ArabBarometer")
makeColumns(GBS1Data.columns, "gbs1.Latinobarometer")
makeColumns(GBS2Data.columns, "gbs2.Afrobarometer")
makeColumns(GBS2Data.columns, "gbs2.ArabBarometer")
makeColumns(GBS2Data.columns, "gbs2.Latinobarometer")

data.to_csv(processedPath+"master_dataset.0.0.2.csv")
