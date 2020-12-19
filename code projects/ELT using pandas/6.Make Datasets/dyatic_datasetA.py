import pandas as pd
import math


rawPath = "/home/ec2-user/survey_project/data/raw/"
processedPath = "/home/ec2-user/survey_project/data/processed/"
interimPath = "/home/ec2-user/survey_project/data/interim/"


data = pd.read_csv(processedPath + 'selectedQs_longDataset.0.0.3.csv',encoding = "ISO-8859-1")
data['merge'] = 1

def calculate_distance(x,y):
    distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
    return distance


canada = data.loc[data['iso3166_osn'] == "Canada"]
spain = data.loc[data['iso3166_osn'] == "Spain"]
colombia = data.loc[data['iso3166_osn'] == "Colombia"]
southAfrica = data.loc[data['iso3166_osn'] == "South Africa"]
china = data.loc[data['iso3166_osn'] == "China"]

data = pd.concat([canada,spain,colombia,southAfrica,china])
data['merge'] = 1
data_target = data


data = data.merge(data_target,on = "merge", suffixes =("_source","_target"))
data = data.drop("merge", axis = 1)
data["dyat_distance"]= data.apply(lambda row: calculate_distance((row['tradsec_source'], row['survself_source']), (row['tradsec_target'], row['survself_target'])),axis=1)
print(data.columns)

data.to_csv(processedPath+"dyatic_dataset.csv")
