import pandas as pd

rawPath = "/home/ec2-user/survey_project/data/raw/"
processedPath = "/home/ec2-user/survey_project/data/processed/"
interimPath = "/home/ec2-user/survey_project/data/interim/"

#loss counters
hit = 0
miss = 0


#define helper functions
def makeColumns(survey):
    global questions
    global data
    global surveys

    for wave in surveys[survey]:
        for question in questions:
            data[question + "." + survey + "." + str(wave)] = None

def fixCode(code):
    if (str(code) != "nan") and len(str(code)) < 6:
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


def merge1(key,survey, country, wave, province, F063,Y003,F120,G006,E018,Y002,A008,E025,F118,A165,tradsec,survself):
    global data
    global questions
    global hit, miss
    values = [F063,Y003,F120,G006,E018,Y002,A008,E025,F118,A165,tradsec,survself]
    index = 0
    #get location
    df = key.loc[(key["S003"] == country) & (key["X048_ALL"] == province) , 'new_subdivision_code']
    if not df.empty:
        hit = hit + 1
        provinceCode = str(df.iloc[0])
        for question in questions:
            #get row and loop over qestions
            title = question + "." + survey[-3:] + "."+ wave[0]
            data.loc[data['new_subdivision_code'] == provinceCode, title] = values[index]
            index = index+1
    else:
        miss = miss + 1

def merge2(key,survey, country, wave, province, F063,Y003,F120,G006,E018,Y002,A008,E025,F118,A165,tradsec,survself):
    global data
    global questions
    global hit, miss
    values = [F063,Y003,F120,G006,E018,Y002,A008,E025,F118,A165,tradsec,survself]
    index = 0
    #get location
    df = key.loc[(key["pais"] == country) & (key["prov"] == province) , 'new_subdivision_code']
    if not df.empty:
        hit = hit + 1
        provinceCode = str(df.iloc[0])
        for question in questions:
            #get row and loop over qestions
            title = question + "." + survey + "."+ str(wave)
            data.loc[data['new_subdivision_code'] == provinceCode, title] = values[index]
            index = index+1
    else:
        miss = miss + 1

def merge3(key,survey, waves, country, province, F063,Y003,F120,G006,E018,Y002,A008,E025,F118,A165,tradsec,survself):
    global data
    global questions
    global hit, miss
    values = [F063,Y003,F120,G006,E018,Y002,A008,E025,F118,A165,tradsec,survself]
    index = 0
    #get location
    df = key.loc[(key["country_un"] == country) & (key["province"] == province) , 'new_subdivision_code']
    if not df.empty:
        hit = hit + 1
        provinceCode = str(df.iloc[0])
        for question in questions:
            #get row and loop over qestions
            title = question + "." + waves[survey]
            data.loc[data['new_subdivision_code'] == provinceCode, title] = values[index]
            index = index+1
    else:
        miss = miss + 1

#define surveys and waves
data = pd.read_csv(interimPath + "selectedQs_dataset.0.0.1.csv", encoding = "ISO-8859-1")
questions = ["F063","Y003","F120","G006","E018","Y002","A008","E025","F118","A165","tradsec","survself"]
surveys = {"wvs":[1,2,3,4,5,6],
            "evs":[1,2,3,4],
            "americas.barometer": [2004,2006,2008,2010,2012,2014],
            "Afrobarometer": [3,4,5],
            "ArabBarometer": [2,3],
            "Latinobarometer": [2005,2010,2013]}

#construct columns
for survey in surveys:
    makeColumns(survey)

#read province list keys
wvsEvsProvinceList = pd.read_csv(processedPath + "merged_WVSEVS.csv",encoding = "ISO-8859-1")
americasProvinceList = pd.read_csv(processedPath + "Americans_provinceList.0.3.csv",encoding = "ISO-8859-1")
GBS1ProvinceList = pd.read_csv(processedPath + "GBS_provinceList0.2.csv",encoding = "ISO-8859-1" )
GBS2ProvinceList = pd.read_csv(processedPath + "GBSII_provinceList0.2.csv",encoding = "ISO-8859-1")

#fix codes
wvsEvsProvinceList["new_subdivision_code"] = wvsEvsProvinceList["new_subdivision_code"].astype(str)
wvsEvsProvinceList["new_subdivision_code"] = wvsEvsProvinceList.apply(lambda row: fixCode(row['new_subdivision_code']), axis=1)

americasProvinceList["new_subdivision_code"] = americasProvinceList["new_subdivision_code"].astype(str)
americasProvinceList["new_subdivision_code"] = americasProvinceList.apply(lambda row: fixCode2(row['new_subdivision_code']), axis=1)

GBS1ProvinceList["new_subdivision_code"] = GBS1ProvinceList["new_subdivision_code"].astype(str)
GBS1ProvinceList["new_subdivision_code"] = GBS1ProvinceList.apply(lambda row: fixCode2(row['new_subdivision_code']), axis=1)

GBS2ProvinceList["new_subdivision_code"] = GBS2ProvinceList["new_subdivision_code"].astype(str)
GBS2ProvinceList["new_subdivision_code"] = GBS2ProvinceList.apply(lambda row: fixCode2(row['new_subdivision_code']), axis=1)

#read dimensions datasets
wvsEvsDimensions = pd.read_csv(processedPath + "regional_dimensions_all.0.0.2_selectedQs.csv")
americansDimensions = pd.read_csv(processedPath + "regional_dimensions_americas_selectedQs_imputed.0.0.2.csv")
GBS1Dimentions = pd.read_csv(processedPath + "regional_dimensions_GBS_selectedQs.0.0.3.csv")
GBS2Dimentions = pd.read_csv(processedPath + "regional_dimensions_GBSII_selectedqs.0.0.1.csv")

#merge to dataset
wvsEvsDimensions.apply(lambda row: merge1(wvsEvsProvinceList, row["S001"], row["S003"], row["S002_ALL"],
                                         row["X048_ALL"], row["F063"], row["Y003"], row["F120"], row["G006"],
                                         row["E018"], row["Y002"], row["A008"], row["E025"], row["F118"],
                                         row["A165"], row["tradsec"], row["survself"]), axis=1)

print("provinces found: " + str(hit))
print("provinces missed: " + str(miss))
print("merge efficancy:" + str(hit / (miss+hit)))
hit=0
miss=0

americansDimensions.apply(lambda row: merge2(americasProvinceList, "americas.barometer", row["pais"], row["wave"],
                                         row["prov"], row["q5b"], row["ab1_plus_2"], row["w14a"], row["b43"],
                                         row["b14"], row["a4"], row["soct1"], row["prot6"], None ,
                                         row["it1"], row["tradsec"], row["survself"]), axis=1)

print("provinces found: " + str(hit))
print("provinces missed: " + str(miss))
print("merge efficancy:" + str(hit / (miss+hit)))
hit=0
miss=0

GBS1waves = {2:"Afrobarometer.3",
             3: "Afrobarometer.4",
             5: "ArabBarometer.2",
             6: "Latinobarometer.2005",
             7: "Latinobarometer.2010"}

GBS1Dimentions.apply(lambda row: merge3(GBS1ProvinceList, row["region"], GBS1waves, row["country_un"],
                                         row["province"], row["se10"], None, row["ge1"], row["cit2"],
                                         row["sd5"], row["imp1_2_3"], row["ee1"], row["pp8"], None ,
                                         row["sc1"], row["tradsec"], row["survself"]), axis=1)

print("provinces found: " + str(hit))
print("provinces missed: " + str(miss))
print("merge efficancy:" + str(hit / (miss+hit)))
hit=0
miss=0

GBS2waves = {2:"Afrobarometer.5",
             3: "ArabBarometer.3",
             5: "Latinobarometer.2013"}

GBS2Dimentions.apply(lambda row: merge3(GBS2ProvinceList, row["region"], GBS2waves, row["country_un"],
                                         row["province"], row["f006_customized"], None, None, None,
                                         row["gov5"], row["imp1_2_3"], row["ee1"], row["pp6"], None ,
                                         row["sc1"], row["tradsec"], row["survself"]), axis=1)

print("provinces found: " + str(hit))
print("provinces missed: " + str(miss))
print("merge efficancy:" + str(hit / (miss+hit)))

data.to_csv(processedPath+"selectedQs_dataset.0.0.2.csv")
