# Copy the data in the file 'web-server-access-log.txt.gz' to the table 'access_log' in the PostgreSQL database 'template1'.
# create table access_log(timestamp timestamp, latitude float, longitude float, visitorid varchar(37));

# # Download the compressed log file
echo "Downloading data"
wget -N 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Bash%20Scripting/ETL%20using%20shell%20scripting/web-server-access-log.txt.gz'

# Unzip the log file
echo "Unzip file"
gzip -f -d web-server-access-log.txt.gz

# Extract phase
echo "Extract data"
cut -d# -f1-4 web-server-access-log.txt > extracted_log_data.txt

# Transform phase
echo "Transforming data"
# read the extracted data and replace the # with commas
tr '#' ',' < extracted_log_data.txt > transformed_log_data.csv

# Load phase
echo "Loading data"
# Send the instructions to connect to 'template1' and
# copy the file to the table 'users' through command pipeline.
echo "\c template1;\COPY access_log FROM `readlink -f transformed_log_data.csv` DELIMITERS ',' CSV HEADER;" | sudo -u postgres psql

# Visualize the data on the database
echo '\c template1;\\SELECT * from access_log;' | sudo -u postgres psql
