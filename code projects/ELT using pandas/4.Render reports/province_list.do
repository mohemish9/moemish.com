clear

use regional_dimensions_all.0.0.2.dta, replace

gen x = 1
collapse (mean) x , by (S001 S002_ALL S003 S020 S009 S009A X048_ALL)
tostring S003 X048_ALL , generate(UNIQUE_COUNTRY_NUMBER UNIQUE_REGION_NUMBER)
drop x

save provinceList_WVSEVS0.0.3.dta

clear
