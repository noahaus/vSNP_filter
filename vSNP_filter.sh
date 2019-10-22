#use R to read and filter data, python to keep the vSNP output formatting
CSV=$1
CUTOFF=$2
Rscript vSNP_filter/filter_regions.R $CSV $CUTOFF
python vSNP_filter/excel_writer.py ./pe-ppe_filtered_out.csv
