## Stage five: Convert province codes

#### Summary
Stage five constructs a list containing the unique names of country and province codes, the ones produced by stage four, and matches = them with the new province codes constructed in stage two.
***
#### Files (in order they should be executed)
#### WVSEVS_add_newProvinceCodes.py (optional)
__Description:__ Note that the list of province names matched with the new province codes was created manually, so this code doesn't produce any new files.
***
__Input files:__ merged_WVSEVS.xlsx(file created manually by matching old provinces naming convention used in WVS-EVS to the new province codes in files produced by **province-codes.0.4.py**), regional_dimensions_all.0.0.2.csv

__Output files:__ None
***
#### Americas_make_newProvinceCodes.py
__Description:__ This file opens the files produced by **Americas_report.py** and **province-codes.0.4.py** to match the province list produced by the first to the new codes produced by the latter.

__Input files:__ Americans_provinceList.0.2csv.csv ( Americans_provinceList.csv with the years and waves added), provinceList0.1.1.xlsx

__Output files:__ Americans_provinceList.0.3.csv
***
#### GBS_make_newProvinceCodes.py
__Description:__ This file opens the files produced by **GBS_provincelist.py** and **province-codes.0.4.py** to match the province list produced by the first to the new codes produced by the latter. **Note:** the final file produced by this code is edited manually to add province codes for provinces that where encoded using different names from the standard ISO 3166-2. Save output files before rerunning this code.

__Input files:__ GBS_provinceList.csv, provinceList0.1.1.xlsx

__Output files:__ GBS_provinceList0.2.csv (more encoding are added to this file manually after it is rendered by this code)
***
#### GBSII_make_newProvinceCodes.py
__Description:__ This file opens the files produced by **GBSII_provincelist.py** and **province-codes.0.4.py** to match the province list produced by the first to the new codes produced by the latter. **Note:** the final file produced by this code is edited manually to add province codes for provinces that where encoded using different names from the standard ISO 3166-2. Save output files before rerunning this code.

__Input files:__ GBSII_provinceList.csv, provinceList0.1.1.xlsx

__Output files:__ GBSII_provinceList0.2.csv

