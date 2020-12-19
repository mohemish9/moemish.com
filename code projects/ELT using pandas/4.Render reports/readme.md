## Stage four: Rendering reports

#### Summary
Stage five produces tables containing summaries of the data produced by stage three. This tables are used in the codebooks of the new datasets.
***
#### Files (in order they should be executed)

#### province_list.do
__Description:__ This file reads file produced by **WVSEVS_Dimensions_Construction.do** and produces a list of unique provinces and country names.

__Input files:__ regional_dimensions_all.0.0.2.dta

__Output files:__ provinceList_WVSEVS0.0.3.dta
***
#### province-codes.py
__Description:__ This file reads file produced by **province_list.do** and cleans names of provinces.

__Input files:__ provinceList_WVSEVS0.0.3.dta

__Output files:__ provinceList_WVSEVS0.0.4.csv
***
#### Americas_report.py
__Description:__ This file reads file produced by **Americas_Dimensions_Construction_afterimputation.do** and produces tables containing titles of the questions, a list of waves, list of countries and how many provinces each country includes, list of provinces that doesn't have enough data to construct Inglehart's dimensions, and a list of unique provinces and country names.

__Input files:__ regional_dimensions_americas_selectedQs.0.0.2.csv

__Output files:__ Americas_columns.csv, Americas_waves.csv, Americas_countries.csv, Americas_nodimensions.csv, Americans_provinceList.csv
***
#### GBS_report.py (optional)
__Description:__ This file reads file produced by **GBS_Dimensions_Construction_selectedQs.do** and produces tables containing titles of the questions, a list of waves, list of countries and how many provinces each country includes, and a list of provinces that doesn't have enough data to construct Inglehart's dimensions

__Input files:__ regional_dimensions_GBS_selectedQs.0.0.3.csv

__Output files:__ GBS_columns.csv, GBS_waves.csv, GBS_countries.csv,GBS_nodimensions.csv
***
#### GBS_provincelist.py
__Description:__ This file reads file produced by **GBS_Dimensions_Construction_selectedQs.do** and produces a list of unique provinces and country names.

__Input files:__ regional_dimensions_GBS_selectedQs.0.0.3.csv

__Output files:__ GBS_provinceList.csv
***
#### GBSII_report.py (optional)
__Description:__ This file reads file produced by **GBSII_Dimensions_Construction_selectedQs.do** and produces tables containing titles of the questions, a list of waves, list of countries and how many provinces each country includes, and a list of provinces that doesn't have enough data to construct Inglehart's dimensions

__Input files:__ regional_dimensions_GBSII_selectedqs.0.0.1.csv

__Output files:__ GBSII_columns.csv, GBSII_waves.csv, GBSII_countries.csv, GBSII_nodimensions.csv
***
#### GBSII_provincelist.py
__Description:__ This file reads file produced by **GBSII_Dimensions_Construction_selectedQs.do** produces a list of unique provinces and country names.

__Input files:__ regional_dimensions_GBSII_selectedqs.0.0.1.csv

__Output files:__ GBSII_provinceList.csv

