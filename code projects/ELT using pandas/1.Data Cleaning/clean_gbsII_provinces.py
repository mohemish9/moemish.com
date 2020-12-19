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


arab10_12 = pd.read_csv(interimPath+"arab10_12_respondentsID.csv")
arab10_12['UN_code'] = arab10_12.apply(lambda row: getUNCode(row['country']),axis=1)
arab10_12.to_csv(interimPath+"arab11_13_respondentsID_c.csv")
del arab10_12
print('arab12 is done')

afro11_13 = pd.read_csv(interimPath+"afro11_13_respondentsID.csv")
afro11_13['UN_code'] = afro11_13.apply(lambda row: getUNCode(row['COUNTRY']),axis=1)
afro11_13['RESPNO'] = afro11_13.apply(lambda row: cleanIDs(row['RESPNO']),axis=1)
afro11_13.to_csv(interimPath+"afro11_13_respondentsID_c.csv")
del afro11_13
print('afro11_13 is done')

latin13 = pd.read_csv(interimPath+"latin13_respondentsID.csv")
latin13['UN_code'] = latin13.apply(lambda row: getUNCode(row['idenpa']),axis=1)
latin13.to_csv(interimPath+"latin13_respondentsID_c.csv")
print("latin13 is done")
