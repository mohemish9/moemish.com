clear
cd "/home/ec2-user/survey_project/data/processed"

insheet using regional_dimensions_americas_imputed.0.0.1.csv,comma

save regional_dimensions_americas_imputed.0.0.1.dta, replace

use regional_dimensions_americas_imputed.0.0.1.dta, replace

drop tradsec
drop survself



pwcorr q5b ab1_plus_2 w14a b43 b14 a4 soct1 prot6 it1


ds, has(type numeric)
local vars_ALL `r(varlist)'
local omit pais wave year prov
local vars: list vars_ALL - omit
collapse (mean) `vars', by (pais wave year prov)


factor q5b ab1_plus_2 w14a b43 b14 a4 soct1 prot6 it1, pcf factors (2)
screeplot
rotate, varimax
estat rotatecompare
loadingplot, ytitle(component 2) xtitle(component 1)

predict tradsec survself

save regional_dimensions_americas_imputed.0.0.2.dta, replace

outsheet using regional_dimensions_americas_imputed.0.0.2.csv, comma

exit
