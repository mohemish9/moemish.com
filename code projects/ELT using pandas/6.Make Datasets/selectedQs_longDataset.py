import pandas as pd
import numpy as np

rawPath = "/home/ec2-user/survey_project/data/raw/"
processedPath = "/home/ec2-user/survey_project/data/processed/"
interimPath = "/home/ec2-user/survey_project/data/interim/"

#loss counters
hit = 0
miss = 0



#define helper functions
def makeColumns():
    global questions

    for question in questions:
            data[question] = None

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

missing_countries = np.empty([1, 1])

def merge1(key,survey, country, wave, province, F063,Y003,F120,G006,E018,Y002,A008,E025,F118,A165,tradsec,survself,year,sample_size):
    global data
    global questions
    global hit, miss
    global provinceKey
    global missing_countries
    values = [sample_size,F063,Y003,F120,G006,E018,Y002,A008,E025,F118,A165,tradsec,survself]
    index = 0
    #get location
    df = key.loc[(key["S003"] == country) & (key["X048_ALL"] == province) , 'new_subdivision_code']
    if not df.empty:
        if not (str(df.iloc[0]) == "nan" or str(df.iloc[0]) == "None"):
            df = df.unique()
            for r in range(len(df)):
                hit = hit + 1
                provinceCode = str(df[r])
                provinceInfo = provinceKey.loc[provinceKey["new_subdivision_code"] == provinceCode]
                info = provinceInfo.columns
                surveyTitle = survey[-3:] + "."+ wave[0]
                data = data.append({'survey' : surveyTitle}, ignore_index=True)
                data.loc[data.shape[0]-1, "year"] = int(year[:4])
                for i in info:
                    if not provinceInfo[i].empty:
                        data.loc[data.shape[0]-1,i ] = provinceInfo[i].iloc[0]
                for question in questions:
                    #get row and loop over qestions
                    title = question
                    data.loc[data.shape[0]-1, title] = values[index]
                    index = index+1
                index = 0
    else:

        surveyTitle = survey[-3:] + "."+ wave[0]
        data = data.append({'survey' : surveyTitle}, ignore_index=True)
        data.loc[data.shape[0]-1, "year"] = int(year[:4])
        prov = str(province).split(". ",1)
        coun = str(country).split(". ",1)
        #print(prov[len(prov)-1])
        #print(coun[len(coun)-1])
        if not prov[len(prov)-1] == 'nan':
            data.loc[data.shape[0]-1, "ISO3166_2_c"] = prov[len(prov)-1]
        data.loc[data.shape[0]-1, "ISO3166_OSN"] = coun[len(coun)-1]
        for question in questions:
            #get row and loop over qestions
            title = question
            data.loc[data.shape[0]-1, title] = values[index]
            index = index+1
        miss = miss + 1
        missing_countries = np.append(missing_countries,[[str(country) + "@" + str(province)]])


def merge2(key,survey, country, wave, province, F063,Y003,F120,G006,E018,Y002,A008,E025,F118,A165,tradsec,survself,year,sample_size):
    global data
    global questions
    global missing_countries
    global hit, miss
    values = [sample_size,F063,Y003,F120,G006,E018,Y002,A008,E025,F118,A165,tradsec,survself]
    index = 0
    #get location
    df = key.loc[(key["pais"] == country) & (key["prov"] == province) , 'new_subdivision_code']
    if not df.empty:
        if not (str(df.iloc[0]) == "nan" or str(df.iloc[0]) == "None"):
            df = df.unique()
            for r in range(len(df)):
                hit = hit + 1
                provinceCode = str(df[r])
                provinceInfo = provinceKey.loc[provinceKey["new_subdivision_code"] == provinceCode]
                info = provinceInfo.columns
                surveyTitle = survey + "."+ str(wave)
                data = data.append({'survey' : surveyTitle}, ignore_index=True)
                data.loc[data.shape[0]-1, "year"] = int(year)
                for i in info:
                    if not provinceInfo[i].empty:
                        data.loc[data.shape[0]-1,i ] = provinceInfo[i].iloc[0]
                for question in questions:
                    #get row and loop over qestions
                    title = question
                    data.loc[data.shape[0]-1, title] = values[index]
                    index = index+1
                index = 0
    else:
        surveyTitle = survey + "."+ str(wave)
        data = data.append({'survey' : surveyTitle}, ignore_index=True)
        data.loc[data.shape[0]-1, "year"] = int(year)
        prov = str(province).split(". ",1)
        coun = str(country).split(". ",1)
        if not prov[len(prov)-1]== 'nan':
            data.loc[data.shape[0]-1, "ISO3166_2_c"] = prov[len(prov)-1]
        data.loc[data.shape[0]-1, "ISO3166_OSN"] = coun[len(coun)-1]
        for question in questions:
            #get row and loop over qestions
            title = question
            data.loc[data.shape[0]-1, title] = values[index]
            index = index+1
        missing_countries = np.append(missing_countries,[[str(country) + "@" + str(province)]])
        miss = miss + 1

def merge3(key,survey, waves, country, province, F063,Y003,F120,G006,E018,Y002,A008,E025,F118,A165,tradsec,survself,year,sample_size):
    global data
    global questions
    global hit, miss
    global missing_countries
    values = [sample_size, F063,Y003,F120,G006,E018,Y002,A008,E025,F118,A165,tradsec,survself]
    index = 0
    #get location
    df = key.loc[(key["country_un"] == country) & (key["province"] == province) , 'new_subdivision_code']
    if not df.empty:
        if not (str(df.iloc[0]) == "nan" or str(df.iloc[0]) == "None"):
            df = df.unique()
            for r in range(len(df)):
                hit = hit + 1
                provinceCode = str(df[r])
                provinceInfo = provinceKey.loc[provinceKey["new_subdivision_code"] == provinceCode]
                info = provinceInfo.columns
                surveyTitle = waves[survey]
                data = data.append({'survey' : surveyTitle}, ignore_index=True)
                data.loc[data.shape[0]-1, "year"] = int(year)
                for i in info:
                    if not provinceInfo[i].empty:
                        data.loc[data.shape[0]-1,i ] = provinceInfo[i].iloc[0]
                for question in questions:
                    #get row and loop over qestions
                    title = question
                    data.loc[data.shape[0]-1, title] = values[index]
                    index = index+1
                index = 0
    else:
        surveyTitle = waves[survey]
        data = data.append({'survey' : surveyTitle}, ignore_index=True)
        data.loc[data.shape[0]-1, "year"] = int(year)
        if not province == 'nan':
            data.loc[data.shape[0]-1, "ISO3166_2_c"] = province
        data.loc[data.shape[0]-1, "ISO3166_OSN"] = country
        for question in questions:
            #get row and loop over qestions
            title = question
            data.loc[data.shape[0]-1, title] = values[index]
            index = index+1
        missing_countries = np.append(missing_countries,[[str(country) + "@" + str(province)]])
        miss = miss + 1

#define surveys and waves
data = pd.read_csv(interimPath + "master_longDataset.0.0.1.csv", encoding = "ISO-8859-1")
questions = ["SAMPLE_SIZE","F063","Y003","F120","G006","E018","Y002","A008","E025","F118","A165","tradsec","survself"]
surveys = {"wvs":[1,2,3,4,5,6],
            "evs":[1,2,3,4],
            "americas.barometer": [2004,2006,2008,2010,2012,2014],
            "Afrobarometer": [3,4,5],
            "ArabBarometer": [2,3],
            "Latinobarometer": [2005,2010,2013]}

#construct columns
data["survey"] = None
data["year"] = None
makeColumns()

#read province list keys
wvsEvsProvinceList = pd.read_csv(processedPath + "merged_WVSEVS0.3.csv",encoding = "ISO-8859-1")
americasProvinceList = pd.read_csv(processedPath + "Americans_provinceList.0.4.csv",encoding = "ISO-8859-1")
GBS1ProvinceList = pd.read_csv(processedPath + "GBS_provinceList0.2.csv",encoding = "ISO-8859-1" )
#GBS2ProvinceList = pd.read_csv(processedPath + "GBSII_provinceList0.2.csv",encoding = "ISO-8859-1")
provinceKey = pd.read_csv(interimPath + "master_dataset.0.0.1.csv", encoding = "ISO-8859-1")


#fix codes
wvsEvsProvinceList["new_subdivision_code"] = wvsEvsProvinceList["new_subdivision_code"].astype(str)
wvsEvsProvinceList["new_subdivision_code"] = wvsEvsProvinceList.apply(lambda row: fixCode(row['new_subdivision_code']), axis=1)

americasProvinceList["new_subdivision_code"] = americasProvinceList["new_subdivision_code"].astype(str)
americasProvinceList["new_subdivision_code"] = americasProvinceList.apply(lambda row: fixCode2(row['new_subdivision_code']), axis=1)

GBS1ProvinceList["new_subdivision_code"] = GBS1ProvinceList["new_subdivision_code"].astype(str)
GBS1ProvinceList["new_subdivision_code"] = GBS1ProvinceList.apply(lambda row: fixCode2(row['new_subdivision_code']), axis=1)

#GBS2ProvinceList["new_subdivision_code"] = GBS2ProvinceList["new_subdivision_code"].astype(str)
#GBS2ProvinceList["new_subdivision_code"] = GBS2ProvinceList.apply(lambda row: fixCode2(row['new_subdivision_code']), axis=1)

#read dimensions datasets
wvsEvsDimensions = pd.read_csv(processedPath + "regional_dimensions_all.0.0.2_selectedQs.csv")
americansDimensions = pd.read_csv(processedPath + "regional_dimensions_americas_selectedQs_imputed.0.0.2.csv",encoding = "ISO-8859-1")
GBS1Dimentions = pd.read_csv(processedPath + "regional_dimensions_GBS_selectedQs.0.0.3.csv")
#GBS2Dimentions = pd.read_csv(processedPath + "regional_dimensions_GBSII_selectedqs.0.0.1.csv")

#merge to dataset
wvsEvsDimensions.apply(lambda row: merge1(wvsEvsProvinceList, row["S001"], row["S003"], row["S002_ALL"],
                                         row["X048_ALL"], row["F063"], row["Y003"], row["F120"], row["G006"],
                                         row["E018"], row["Y002"], row["A008"], row["E025"], row["F118"],
                                         row["A165"], row["tradsec"], row["survself"], row['S020'], row['SAMPLE_SIZE']), axis=1)

print("provinces found: " + str(hit))
print("provinces missed: " + str(miss))
print("merge efficancy:" + str(hit / (miss+hit)))
unique, counts = np.unique(missing_countries, return_counts=True)
merge_imp_dic = dict(zip(unique, counts))
merge_imp = pd.DataFrame(merge_imp_dic, index= [0])
merge_imp = merge_imp.T
merge_imp.columns = ["num"]
merge_imp = merge_imp.sort_values(by=['num'], ascending=False)
merge_imp.to_csv(interimPath+"merge_imp_wvsevs.csv")

hit=0
miss=0
missing_countries = np.empty([1, 1])

americansDimensions.apply(lambda row: merge2(americasProvinceList, "americas.barometer", row["pais"], row["wave"],
                                         row["prov"], row["q5b"], row["ab1_plus_2"], row["w14a"], row["b43"],
                                         row["b14"], row["a4_n"], row["soct1"], row["prot6"], None ,
                                         row["it1"], row["tradsec"], row["survself"], row['year'], row['SAMPLE_SIZE']), axis=1)

print("provinces found: " + str(hit))
print("provinces missed: " + str(miss))
print("merge efficancy:" + str(hit / (miss+hit)))

unique, counts = np.unique(missing_countries, return_counts=True)
merge_imp_dic = dict(zip(unique, counts))
merge_imp = pd.DataFrame(merge_imp_dic, index= [0])
merge_imp = merge_imp.T
merge_imp.columns = ["num"]
merge_imp = merge_imp.sort_values(by=['num'], ascending=False)
merge_imp.to_csv(interimPath+"merge_imp_americas.csv")

hit=0
miss=0
missing_countries = np.empty([1, 1])

GBS1waves = {2:"Afrobarometer.3",
             3: "Afrobarometer.4",
             5: "ArabBarometer.2",
             6: "Latinobarometer.2005",
             7: "Latinobarometer.2010"}

GBS1Dimentions.apply(lambda row: merge3(GBS1ProvinceList, row["region"], GBS1waves, row["country_un"],
                                         row["province"], row["se10"], None, row["ge1"], row["cit2"],
                                         row["sd5"], row["imp1_2_3"], row["ee1"], row["pp8"], None ,
                                         row["sc1"], row["tradsec"], row["survself"], row['year'], row['SAMPLE_SIZE']), axis=1)

print("provinces found: " + str(hit))
print("provinces missed: " + str(miss))
print("merge efficancy:" + str(hit / (miss+hit)))

unique, counts = np.unique(missing_countries, return_counts=True)
merge_imp_dic = dict(zip(unique, counts))
merge_imp = pd.DataFrame(merge_imp_dic, index= [0])
merge_imp = merge_imp.T
merge_imp.columns = ["num"]
merge_imp = merge_imp.sort_values(by=['num'], ascending=False)
merge_imp.to_csv(interimPath+"merge_imp_gbs.csv")



hit=0
miss=0

"""GBS2waves = {2:"Afrobarometer.5",
             3: "ArabBarometer.3",
             5: "Latinobarometer.2013"}

GBS2Dimentions.apply(lambda row: merge3(GBS2ProvinceList, row["region"], GBS2waves, row["country_un"],
                                         row["province"], row["f006_customized"], None, None, None,
                                         row["gov5"], row["imp1_2_3"], row["ee1"], row["pp6"], None ,
                                         row["sc1"], row["tradsec"], row["survself"],row['year']), axis=1)"""

"""print("provinces found: " + str(hit))
print("provinces missed: " + str(miss))
print("merge efficancy:" + str(hit / (miss+hit)))"""

data.to_csv(processedPath+"selectedQs_longDataset.0.0.2.csv")
