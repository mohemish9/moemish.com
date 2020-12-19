import pandas as pd
import country_converter as coco

rawPath = "/home/ec2-user/survey_project/data/raw/"
processedPath = "/home/ec2-user/survey_project/data/processed/"
interimPath = "/home/ec2-user/survey_project/data/interim/"

def getUNCode(country):
    if not pd.isnull(country):
        return coco.convert(country, to='UNcode', not_found=None)
    return None

def cleanIDs(id):
    return id[3:]

def cleanCountry(country):
    return country.split(".",1)[1]

afro05 = pd.read_csv(interimPath+"afro05_respondentsID.csv")
afro05['UN_code'] = afro05.apply(lambda row: getUNCode(row['country']),axis=1)
afro05['respno'] = afro05.apply(lambda row: cleanIDs(row['respno']),axis=1)
afro05.to_csv(interimPath+"afro05_respondentsID_c.csv")
del afro05

afro08 = pd.read_csv(interimPath+"afro08_respondentsID.csv")
afro08['UN_code'] = afro08.apply(lambda row: getUNCode(row['COUNTRY']),axis=1)
afro08['RESPNO'] = afro08.apply(lambda row: cleanIDs(row['RESPNO']),axis=1)
afro08.to_csv(interimPath+"afro08_respondentsID_c.csv")
del afro08

arab10 = pd.read_csv(interimPath+"arab10_respondentsID.csv")
arab10['country'] = arab10.apply(lambda row: cleanCountry(row['country']),axis=1)
arab10['q1'] = arab10.apply(lambda row: cleanCountry(row['q1']),axis=1)
arab10['UN_code'] = arab10.apply(lambda row: getUNCode(row['country']),axis=1)
arab10.to_csv(interimPath+"arab10_respondentsID_c.csv")
del arab10

latin05 = pd.read_csv(interimPath + "latin05_respondentsID.csv")
latin05['UN_code'] = latin05.apply(lambda row: getUNCode(row['idenpa']),axis=1)
latin05.to_csv(interimPath + "latin05_respondentsID_c.csv")
del latin05

latin10 = pd.read_csv(interimPath + "latin10_respondentsID.csv")
latin10['UN_code'] = latin10.apply(lambda row: getUNCode(row['idenpa']),axis=1)
latin10.to_csv(interimPath + "latin10_respondentsID_c.csv")
