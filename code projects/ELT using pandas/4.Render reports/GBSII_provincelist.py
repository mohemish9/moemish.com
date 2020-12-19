import pandas as pd
import pyreadstat
import numpy as np
import country_converter as coco

rawPath = "/home/ec2-user/survey_project/data/raw/"
processedPath = "/home/ec2-user/survey_project/data/processed/"
interimPath = "/home/ec2-user/survey_project/data/interim/"

def getCountryName(country):
    if not pd.isnull(country):
        return coco.convert(country, to='name_short', not_found=None)
    return None


data = pd.read_csv(processedPath + "regional_dimensions_GBSII_selectedqs.0.0.1.csv")

provinces = data.groupby(['region','country_un', 'year','province']).size().reset_index(name='x')
provinces.drop(['x'],axis=1)

provinces['Country name'] = provinces.apply(lambda row: getCountryName(row['country_un']),axis=1)
provinces.to_csv(processedPath + 'GBSII_provinceList.csv')
