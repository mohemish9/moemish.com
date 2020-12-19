clear
cd "/home/ec2-user/survey_project/data/processed"

use "regional_dimensions_americas_selectedQs_imputed.0.0.1.dta", replace

drop tradsec
drop survself

pwcorr q5b ab1_plus_2 w14a b43 b14 a4_n soct1 prot6 it1

gen SAMPLE_SIZE = sample_size
drop sample_size

factor q5b ab1_plus_2 w14a b43 b14 a4_n soct1 prot6 it1 SAMPLE_SIZE, pcf factors (2)
screeplot
rotate, varimax
estat rotatecompare
loadingplot, ytitle(component 2) xtitle(component 1)

predict tradsec survself

save regional_dimensions_americas_selectedQs_imputed.0.0.2.dta

exit
