import pandas as pd
import pyreadstat
import numpy as np
import chardet

rawPath = "/home/ec2-user/survey_project/data/raw/"
processedPath = "/home/ec2-user/survey_project/data/processed/"
interimPath = "/home/ec2-user/survey_project/data/interim/"
final = '/home/ec2-user/survey_project/final_product_Nov-19/'



def find_encoding(fname):
    r_file = open(final + fname, 'rb').read()
    result = chardet.detect(r_file)
    charenc = result['encoding']
    return charenc


my_encoding = find_encoding('mon_subV_datasetA_1.0.csv')
data = pd.read_csv(final + "mon_subV_datasetA_1.0.csv", encoding=my_encoding)



def getWave(survey,year):
    global data
    rows = data.loc[(data['survey'] == survey) & (data['year'] == year)]
    number = len(pd.unique(rows['iso3166_1_numeric']))
    return number

def getProvinces(pais, wave, year):
    global data
    rows = data.loc[(data['iso3166_osn'] == pais) & (data['survey']==wave) & (data['year']==year)]
    return rows.shape[0]

def colapse_waves():
    global waves
    output = pd.DataFrame()
    unique_values = np.unique(waves['survey'].values)
    for value in unique_values:
        year_min = waves.loc[waves['survey'] == value,'year'].min()
        year_max = waves.loc[waves['survey'] == value,'year'].max()
        year = str(year_min)+ "-"+ str(year_max)
        number = waves.loc[waves['survey'] == value,'Countries Included'].sum()
        output = output.append({'survey' : value}, ignore_index=True)
        output.loc[output.shape[0]-1, "year"] = year
        output.loc[output.shape[0]-1, 'Countries Included'] = number
    return output

#list of waves
waves = data.drop_duplicates(subset=['survey','year'])
waves = pd.DataFrame(waves[['survey','year']])
waves['Countries Included'] = waves.apply(lambda row: getWave(row['survey'], row['year']),axis=1)
waves = colapse_waves()
waves.to_csv( interimPath + "mon_waves_agg.csv")

#lit of countries, waves, years, # of provinces
countries = data.groupby(['iso3166_osn','survey', 'year']).size().reset_index(name='number of provinces')

countries.to_csv(interimPath + "mon_countries.csv")

#list of provinces that didn't have dimentions variables
no_dimensions = data.loc[pd.isnull(data['tradsec']) & pd.isnull(data['matpostmat'])]
no_dimensions = no_dimensions.groupby(['iso3166_osn','survey', 'year']).size().reset_index(name='x')
no_dimensions['y'] = no_dimensions.apply(lambda row: getProvinces(row['iso3166_osn'], row['survey'], row['year']),axis=1)
no_dimensions['percentage of missing dimentions'] = no_dimensions['x'] / no_dimensions['y'] * 100
no_dimensions = no_dimensions.drop(['x','y'], axis=1)
no_dimensions.to_csv(interimPath + "mon_nodimensions.csv")
