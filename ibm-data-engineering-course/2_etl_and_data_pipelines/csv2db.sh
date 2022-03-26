#! /bin/bash

# This script
# Extracts data from /etc/passwd file into a CSV file.

# The csv data file contains the user name, user id and
# home directory of each user account defined in /etc/passwd

# Transforms the text delimiter from ":" to ",".
# Loads the data from the CSV file into a table in PostgreSQL database.
# In the default database template1 the table users was created with
# the sql command: create table users(username varchar(50),userid int,homedirectory varchar(100));

# Extract phase
echo "Extracting data"
# Extract the columns 1 (user name), 2 (user id) and
# 6 (home directory path) from /etc/passwd
cut -d":" -f1,3,6 /etc/passwd > extracted_data.txt

# Transform phase
echo "Transforming data"
# read the extracted data and replace the colons with commas.
tr ":" "," < extracted_data.txt > transformed_data.csv

# Load phase
echo "Loading data"
# Send the instructions to connect to 'template1' and
# copy the file to the table 'users' through command pipeline.
(export path_to_data=$(readlink -f transformed_data.csv); echo "\c template1;\COPY users FROM $path_to_data DELIMITERS ',' CSV;" | sudo -u postgres psql)

echo '\c template1;\\SELECT * from users;' | sudo -u postgres psql
