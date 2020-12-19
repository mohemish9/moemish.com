import pandas as pd
import pyreadstat
import numpy as np

rawPath = "/home/ec2-user/survey_project/data/raw/"
processedPath = "/home/ec2-user/survey_project/data/processed/"
interimPath = "/home/ec2-user/survey_project/data/interim/"

data = pd.read_csv(processedPath + "regional_dimensions_americas_selectedQs.0.0.2.csv")

print(data)
exit()

def getWave(wave):
    global data
    rows = data.loc[data['wave'] == wave]
    number = len(pd.unique(rows['pais']))
    return number

def cleanCountry(country):
    return country.split(". ",1)[1]

def getProvinces(pais, wave, year):
    global data
    rows = data.loc[(data['pais'] == pais) & (data['wave']==wave) & (data['year']==year)]
    return rows.shape[0]


#list of variables
vars =  pd.DataFrame(data = list(data.columns), columns=['varaible name'])
vars.to_csv(interimPath + "Americas_columns.csv")


#list of waves
waves = pd.DataFrame(pd.unique(data['wave']), columns=['wave'])
waves['countries_included'] = waves.apply(lambda row: getWave(row['wave']), axis=1)
waves.to_csv( interimPath + "Americas_waves.csv")

#lit of countries, waves, years, # of provinces
countries = data.groupby(['pais','wave', 'year']).size().reset_index(name='number of provinces')
countries['pais'] = countries.apply(lambda row: cleanCountry(row['pais']) ,axis=1)
countries.to_csv(interimPath + "Americas_countries.csv")

#list of provinces that didn't have dimentions variables
no_dimensions = data.loc[pd.isnull(data['tradsec']) & pd.isnull(data['survself'])]
no_dimensions = no_dimensions.groupby(['pais','wave', 'year']).size().reset_index(name='x')
no_dimensions['y'] = no_dimensions.apply(lambda row: getProvinces(row['pais'], row['wave'], row['year']),axis=1)
no_dimensions['percentage of missing dimentions'] = no_dimensions['x'] / no_dimensions['y'] * 100
no_dimensions.drop(['x','y'],axis=1)
no_dimensions.to_csv(interimPath + "Americas_nodimensions.csv")

#list of unique provinces
provinces = data.groupby(['pais','wave', 'year','prov']).size().reset_index(name='x')
provinces.drop(['x'],axis=1)
provinces.to_csv(processedPath + 'Americans_provinceList.csv')
