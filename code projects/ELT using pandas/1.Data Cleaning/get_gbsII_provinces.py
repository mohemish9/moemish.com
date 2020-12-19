import pandas as pd
import pyreadstat

rawPath = "/home/ec2-user/survey_project/data/raw/"
processedPath = "/home/ec2-user/survey_project/data/processed/"
interimPath = "/home/ec2-user/survey_project/data/interim/"


afro11_13, afro11_13Meta = pyreadstat.read_sav(rawPath + "afro_merged-round-5-data-34-countries-2011-2013-last-update-july-2015.sav", apply_value_formats = True, usecols=['COUNTRY', 'RESPNO', 'REGION'] )
afro11_13.to_csv(interimPath + "afro11_13_respondentsID.csv")
del afro11_13
del afro11_13Meta

#sa13

latin13 = pd.read_stata(rawPath + "Latinobarometro2013Eng.dta", columns = ['idenpa', 'numentre', 'reg'])
latin13.to_csv(interimPath + "latin13_respondentsID.csv")
del latin13

#eurasia

arab10_12 = pd.read_csv(rawPath + "ABIII_English.csv", names = ['qid', 'country', 'q1'])
arab10_12.to_csv(interimPath + "arab10_12_respondentsID.csv")
del arab10_12
