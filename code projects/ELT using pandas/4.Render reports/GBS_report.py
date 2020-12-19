import pandas as pd
import pyreadstat
import numpy as np
import country_converter as coco


rawPath = "/home/ec2-user/survey_project/data/raw/"
processedPath = "/home/ec2-user/survey_project/data/processed/"
interimPath = "/home/ec2-user/survey_project/data/interim/"

data = pd.read_csv(processedPath + "regional_dimensions_GBS_selectedQs.0.0.3.csv")

print(data)

def getWave(wave):
    global data
    rows = data.loc[data['region'] == wave]
    number = len(pd.unique(rows['country_un']))
    return number

def cleanCountry(country):
    return country.split(". ",1)[1]

def getProvinces(pais, wave, year):
    global data
    rows = data.loc[(data['country_un'] == pais) & (data['region']==wave) & (data['year']==year)]
    return rows.shape[0]

def getCountry(country):
    if not pd.isnull(country):
        return coco.convert(country, to='name_short', not_found=None)
    return None


#list of variables
vars =  pd.DataFrame(data = list(data.columns), columns=['varaible name'])
vars.to_csv(interimPath + "GBS_columns.csv")


#list of waves
waves = pd.DataFrame(pd.unique(data['region']), columns=['wave'])
waves['countries_included'] = waves.apply(lambda row: getWave(row['wave']), axis=1)
waves.to_csv( interimPath + "GBS_waves.csv")

#lit of countries, waves, years, # of provinces
countries = data.groupby(['country_un','region', 'year']).size().reset_index(name='number of provinces')
countries['country'] = countries.apply(lambda row: getCountry(row['country_un']) ,axis=1)
countries.to_csv(interimPath + "GBS_countries.csv")

#list of provinces that didn't have dimentions variables
no_dimensions = data.loc[pd.isnull(data['tradsec']) & pd.isnull(data['survself'])]
no_dimensions = no_dimensions.groupby(['country_un','region', 'year']).size().reset_index(name='x')
no_dimensions['y'] = no_dimensions.apply(lambda row: getProvinces(row['country_un'], row['region'], row['year']),axis=1)
no_dimensions['percentage of missing dimentions'] = no_dimensions['x'] / no_dimensions['y'] * 100
no_dimensions.drop(['x','y'], axis=1)
no_dimensions.to_csv(interimPath + "GBS_nodimensions.csv")
