clear
cd "/home/ec2-user/survey_project/data/processed"

insheet using selectedQs_longDataset.0.0.2.csv, comma

drop if missing(iso3166_2_c)

outsheet using selectedQs_longDataset.0.0.3.csv, comma

drop if sample_size < 50

outsheet using selecctedQs_longDataset_b.0.0.1.csv, comma

clear

exit
