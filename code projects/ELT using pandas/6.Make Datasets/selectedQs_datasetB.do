clear
cd "/home/ec2-user/survey_project/final_product_Nov-19"

insheet using mon_subV_datasetA_1.0.csv, comma

drop if sample_size < 50

outsheet using mon_subV_datasetB_1.0.csv, comma
