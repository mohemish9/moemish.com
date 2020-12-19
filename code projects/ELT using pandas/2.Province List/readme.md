## Stage two: Making Province List

#### Summary
Stage two constructs a list of provinces (subdivisions) of countries around the world with unified codes. Province codes are constructed using ISO3166-2 codes and they are used for merge.
***
#### Files (in order they should be executed)
#### province-codes.0.2.py
__Description:__ Opens provinces list, appends iso3166 country code to each country, then constructs province codes by appending a 3 digit cumulative number to the Is03166 code of the country the province belongs to.

__Input files:__ IP2LOCATION-ISO3166-2.CSV (Source: https://www.ip2location.com/free/iso3166-2)

__Output files:__ provinceList_WVSEVS0.0.6.csv

***
#### province-codes.0.3.py
__Description:__ Opens the file produced by **province-codes.0.2.py** and appends Professor Fing's Country codes.

__Input files:__ new_country_code.csv (Professor Fing's coding key), provinceList_WVSEVS0.0.6.csv

__Output files:__ provinceList0.0.7.csv
***
#### province-codes.0.4.py
__Description:__ Opens the file produced by **province-codes.0.3.py** and constructs province codes by appending a 3 digit cumulative number to the Is03166 code of the country the province belongs to.

__Input files:__ provinceList0.0.7.csv

__Output files:__ provinceList_WVSEVS0.0.9.csv

