import pandas as pd
import pycountry as pc

def clean(province):
    if ": " in province:
        return province.split(": ",1)[1]
    elif ":" in province:
        return province.split(":",1)[1]
    else:
        return province

def getCode(country, province):
    if pd.isnull(province):
        return None
    else:
        set = pc.subdivisions.get(country_code= country)
        if set != None:
            for x in set:
                if x.name == province:
                    return x.code
        else:
            return None

df = pd.read_stata('provinceList_WVSEVS0.0.3.dta')
#remove numbers and country code before the name
df['X048_CLEAN'] = df.X048_ALL.apply(clean)
df['PROVINCE_CODE'] = df.apply(lambda row : getCode(row['S009'], row['X048_CLEAN']),axis=1)

df.to_csv('provinceList_WVSEVS0.0.4.csv')
