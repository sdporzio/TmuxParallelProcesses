source ~/.bash_profile
source /grid/fermiapp/products/uboone/setup_uboone.sh
setup uboonecode v07_07_00 -q e17:prof
cd /uboone/app/users/sporzio/GridJob/Analysis/Prestage/Temp/Lists
log getListFromDefinition -i $VAR1 -n 20000