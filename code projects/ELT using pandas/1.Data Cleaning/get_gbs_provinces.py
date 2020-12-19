import pandas as pd
import pyreadstat

rawPath = "/home/ec2-user/survey_project/data/raw/"
processedPath = "/home/ec2-user/survey_project/data/processed/"
interimPath = "/home/ec2-user/survey_project/data/interim/"
#asianII

afro05, afro05Meta = pyreadstat.read_sav(rawPath + "afro_merged_r3_data.sav", apply_value_formats = True, usecols=['country', 'respno', 'region'] )
afro05.to_csv(interimPath + "afro05_respondentsID.csv")
del afro05
del afro05Meta

afro08, afro08Meta = pyreadstat.read_sav(rawPath + "afro_merged_r4_data.sav" ,apply_value_formats = True ,usecols=['COUNTRY', 'RESPNO', 'REGION'] )
afro08.to_csv(interimPath + "afro08_respondentsID.csv")
del afro08
del afro08Meta

#arab06 = pd.read_stata(rawPath + "ABI_English.dta", columns = ['country', ])
arab10 = pd.read_stata(rawPath + "ABII_English.dta", columns = ['qid', 'country', 'q1' ])
arab10.to_csv(interimPath + "arab10_respondentsID.csv")
del arab10

latin05 = pd.read_stata(rawPath + "Latinobarometro_2005_datos_eng_v2014_06_27.dta", columns = ['idenpa', 'numentre', 'reg'])
latin05.to_csv(interimPath + "latin05_respondentsID.csv")
del latin05
latin10 =  pd.read_stata(rawPath + "Latinobarometro_2010_datos_eng_v2014_06_27.dta", columns = ['idenpa', 'numentre', 'reg'])
latin10.to_csv(interimPath + "latin10_respondentsID.csv")
del latin10

#sa05 =
