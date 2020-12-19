## Stage six: Making Datasets

#### Summary
Stage six merges the files from stage three into 2 files, one containing the files that includes all questions (master dataset) and the other contains files that includes Inglehart's dimensions and the questions used to construct them.
***
#### Files (in order they should be executed)
#### selectedQs_dataset.py
__Description:__ This file merges the files produced by stage three that contains the selected questions and the Inglehart dimensions. The merge is done by using the files created in stage five to match the old names from the original survey  Each file in the row holds all the records of a province. Each column after the province name and code holds the values of a give question. Names of questions are put into the following format : *QuestionsName* _ *SurveyName* _ *WaveNumber*  

__Input files:__ merged_WVSEVS.csv, Americans_provinceList.0.3.csv, GBS_provinceList0.2.csv, GBSII_provinceList0.2.csv, selectedQs_dataset.0.0.1.csv (another copy of provinceList0.1.1.xlsx), regional_dimensions_all.0.0.2_selectedQs.csv, regional_dimensions_americas_selectedQs_imputed.0.0.2.csv, regional_dimensions_GBS_selectedQs.0.0.3.csv, regional_dimensions_GBSII_selectedqs.0.0.1.csv

__Output files:__ selectedQs_dataset.0.0.2.csv
***
#### selectedQs_longDataset.py
__Description:__ This file merges the files produced by stage three that contains the selected questions and the Inglehart dimensions in a long format. The merge is done by using the files created in stage five to match the old names from the original survey. Columns of the long dataset contain the values of one question from across all surveys

__Input files:__ master_longDataset.0.0.1.csv(an empty file), merged_WVSEVS.csv, Americans_provinceList.0.3.csv, GBS_provinceList0.2.csv, GBSII_provinceList0.2.csv, master_dataset.0.0.1.csv (another copy of provinceList0.1.1.xlsx), regional_dimensions_all.0.0.2_selectedQs.csv, regional_dimensions_americas_selectedQs_imputed.0.0.2.csv, regional_dimensions_GBS_selectedQs.0.0.3.csv, regional_dimensions_GBSII_selectedqs.0.0.1.csv

__Output files:__ selectedQs_longDataset.0.0.2.csv (empty columns are removed manually later and the file version changed to selectedQs_longDataset.0.0.3.csv)
***

#### master_longDataSet_columns.py
__Description:__ This file creates the columns of the master dataset. Each column, after the province name and code, holds the values of a give question. Names of questions are put into the following format : *SurveyName* _ *QuestionsName* . Moreover, it adds a column called *survey* which stores the name of the survey and the wave.

__Input files:__ regional_dimensions_all.0.0.3.csv, regional_dimensions_americas.0.0.3.csv, regional_dimensions_GBS.0.0.2.csv, regional_dimensions_GBSII0.0.1.csv, master_longDataset.0.0.1.csv (empty file)

__Output files:__ master_longDataSet.0.0.2.csv
***
#### master_longDataset_wvsevs.py
__Description:__ This file open the WVS-EVS files produced in stage three which contains all the questions. It adds the new province code of each province and then adds and merges the values with the file from **master_longDataSet_columns.py** in a long format.

__Input files:__ master_dataset.0.0.1.csv (another copy of provinceList0.1.1.xlsx), master_longDataSet.0.0.2.csv, regional_dimensions_all.0.0.3.csv, merged_WVSEVS.csv

__Output files:__ master_longDataSet.0.0.3.csv
***
#### master_longDataset_gbs.py
__Description:__ This file open the GBS I and GBS II files produced in stage three which contains all the questions. It adds the new province code of each province and then adds and merges the values with the file from **master_longDataset_wvsevs.py** in a long format.

__Input files:__ master_dataset.0.0.1.csv (another copy of provinceList0.1.1.xlsx), master_longDataSet.0.0.3.csv, GBS_provinceList0.2.csv, GBSII_provinceList0.2.csv, regional_dimensions_GBS.0.0.2.csv, regional_dimensions_GBSII0.0.1.csv

__Output files:__ master_longDataSet.0.0.4.csv
***

#### master_longDataset_americas.py
__Description:__ This file open the Americas files produced in stage three which contains all the questions. It adds the new province code of each province and then adds and merges the values with the file from **master_longDataset_gbs.py** in a long format.

__Input files:__ master_dataset.0.0.1.csv (another copy of provinceList0.1.1.xlsx), Americans_provinceList.0.3.csv,
regional_dimensions_americas_imputed.0.0.2.csv

__Output files:__ master_longDataSet.0.0.5.csv
***
#### drop_empty_columns.py
__Description:__ This file open opens the file produced by **master_longDataset_americas.py** and drops columns that are completely empty.

__Input files:__ master_longDataSet.0.0.5.csv

__Output files:__ master_longDataSet.0.0.6.csv
***

#### master_dataset_columns.py (optional)
__Description:__ This file merges the files produced by stage three that contains all the questions. The merge is done by using the files created in stage five to match the old names from the original survey  Each file in the row holds all the records of a province. Each column after the province name and code holds the values of a give question. Names of questions are put into the following format : *SurveyName* _ *QuestionsName*

__Input files:__ master_dataset.0.0.1.csv(copy of provinceList0.1.1.xlsx), regional_dimensions_all.0.0.3.csv, regional_dimensions_americas.0.0.3.csv, regional_dimensions_GBS.0.0.2.csv, regional_dimensions_GBSII0.0.1.csv,  

__Output files:__ master_dataset.0.0.2.csv
***
#### master_dataset_wvsevs.py (optional)
__Description:__ This file open the WVS-EVS files produced in stage three which contains all the questions. It merges the values with the file from **master_datataSet_columns.py** in a long format.

__Input files:__ selectedQs_dataset.0.0.2.csv, regional_dimensions_all.0.0.3.csv, merged_WVSEVS.csv

__Output files:__ master_dataset.0.0.3.csv
***
#### master_dataset_gbs.py (optional)
__Description:__ This file open the GBS I and GBS II files produced in stage three which contains all the questions. It merges the values with the file from **master_dataset_wvsevs.py** in a long format.

__Input files:__ master_dataset.0.0.3.csv, GBS_provinceList0.2.csv, GBSII_provinceList0.2.csv, regional_dimensions_GBS.0.0.2.csv, regional_dimensions_GBSII0.0.1.csv,

__Output files:__ master_dataset.0.0.4.csv
***
#### master_dataset_americas.py (optional)
__Description:__ This file open the Americas files produced in stage three which contains all the questions. It merges the values with the file from **master_dataset_gbs.py** in a long format.

__Input files:__ master_dataset.0.0.4.csv, Americans_provinceList.0.3.csv,  regional_dimensions_americas_imputed.0.0.2.csv

__Output files:__ master_dataset.0.0.5.csv

