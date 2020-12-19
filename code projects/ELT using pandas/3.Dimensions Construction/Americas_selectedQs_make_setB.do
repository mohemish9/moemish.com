clear
cd "/home/ec2-user/survey_project/data/processed"

use "regional_dimensions_americas_selectedQs.0.0.1.dta", replace

drop if SAMPLE_SIZE < 50

save regional_dimensions_americas_selectedQs.0.0.2.dta, replace

outsheet using regional_dimensions_americas_selectedQs.0.0.2.csv, comma
