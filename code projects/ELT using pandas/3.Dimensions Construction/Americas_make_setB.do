clear
cd "/home/ec2-user/survey_project/data/processed"

use "regional_dimensions_americas.0.0.3.dta", replace

drop if SAMPLE_SIZE < 50

save regional_dimensions_americas.0.0.4.dta, replace

outsheet using regional_dimensions_americas.0.0.4.csv, comma
