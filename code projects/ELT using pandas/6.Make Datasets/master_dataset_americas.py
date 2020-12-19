import pandas as pd

rawPath = "/home/ec2-user/survey_project/data/raw/"
processedPath = "/home/ec2-user/survey_project/data/processed/"
interimPath = "/home/ec2-user/survey_project/data/interim/"

#init miss and hit counters
miss = 0
hit = 0

#define helper functions

def fixCode(code):
    if (str(code) != "nan") and (str(code) != "None") and len(str(code)) < 6:
        dif = 6 - len(str(code))
        return ("0" * dif) + str(code)
    else:
        return code

def fixCode2(code):
    if "." in code:
        code = code.split(".",1)[0]
    if (str(code) != "nan") and len(str(code)) < 6:
        dif = 6 - len(str(code))
        return ("0" * dif) + str(code)
    else:
        return code


def merge2(df):
    global data
    global americasProvinceList
    global americasData
    global hit, miss

    key = americasProvinceList
    questions = americasData.columns
    #get location
    code = key.loc[(key["pais"] == country) & (key["prov"] == province) , 'new_subdivision_code']
    survey = "americas.barometer"
    if not code.empty:
        if not (str(code.iloc[0]) == "nan" or str(code.iloc[0]) == "None"):
            hit = hit + 1
            provinceCode = str(df.iloc[0])
            for question in questions:
                #get row and loop over qestions
                title = question + "." + survey + "."+ df['wave']
                data.loc[data['new_subdivision_code'] == provinceCode, title] = values[index]
    else:
        miss = miss + 1


data = pd.read_csv(processedPath + "master_dataset.0.0.4.csv", encoding = "ISO-8859-1")


surveys = {"wvs":[1,2,3,4,5,6],
            "evs":[1,2,3,4],
            "americas.barometer": [2004,2006,2008,2010,2012,2014],
            "gbs1.Afrobarometer": [3,4],
            "gbs2.Afrobarometer":[5],
            "gbs1.ArabBarometer": [2],
            "gbs2.ArabBarometer": [3],
            "gbs1.Latinobarometer": [2005,2010],
            "gbs2.Latinobarometer": [2013]}



#read province list keys
americasProvinceList = pd.read_csv(processedPath + "Americans_provinceList.0.3.csv",encoding = "ISO-8859-1" )
#fix codes
data["new_subdivision_code"] = data["new_subdivision_code"].astype(str)
data["new_subdivision_code"] = data.apply(lambda row: fixCode(row['new_subdivision_code']), axis=1)

americasProvinceList["new_subdivision_code"] = GBS1ProvinceList["new_subdivision_code"].astype(str)
americasProvinceList["new_subdivision_code"] = GBS1ProvinceList.apply(lambda row: fixCode2(row['new_subdivision_code']), axis=1)



#read  datasets

americasData = pd.read_csv(processedPath + "regional_dimensions_americas_imputed.0.0.2.csv")

#merge datasets

americasData.apply(merge2, axis=1)
print(miss / (miss+hit))

data.to_csv(processedPath+"master_dataset.0.0.5.csv")
