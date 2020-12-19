import pandas as pd
import pyreadstat

rawPath = "/home/ec2-user/survey_project/data/raw/"
processedPath = "/home/ec2-user/survey_project/data/processed/"
interimPath = "/home/ec2-user/survey_project/data/interim/"


afro11_13, afro11_13Meta = pyreadstat.read_sav(rawPath + "afro_merged-round-5-data-34-countries-2011-2013-last-update-july-2015.sav", apply_value_formats = True, usecols=['COUNTRY', 'RESPNO'] )
afro11_13F006, afro11_13MetaF006 = pyreadstat.read_sav(rawPath + "afro_merged-round-5-data-34-countries-2011-2013-last-update-july-2015.sav", apply_value_formats = False, usecols=['Q98B'] )
afro11_13['Q98B']  = afro11_13F006['Q98B']
afro11_13.to_csv(interimPath + "afro11_13_F006.csv")
del afro11_13
del afro11_13Meta



latin13 = pd.read_stata(rawPath + "Latinobarometro2013Eng.dta", columns = ['idenpa', 'numentre'])
latin13F006 = pd.read_stata(rawPath + "Latinobarometro2013Eng.dta", columns = ['S14_A'], convert_categoricals=False)
latin13['S14_A'] =  latin13F006['S14_A']
latin13.to_csv(interimPath + "latin13_F006.csv")
del latin13


arab10_12 = pd.read_stata(rawPath + "ABIII_English.dta", columns = ['qid', 'country'])
arab10_12F006 = pd.read_stata(rawPath + "ABIII_English.dta", columns = ['q6101'], convert_categoricals=False)
arab10_12['q6101'] = arab10_12F006['q6101']
arab10_12.to_csv(interimPath + "arab10_12_F006.csv")
del arab10_12
