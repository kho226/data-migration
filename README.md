# data-migration
a tool to backfill a postgres database

# Table of Contents
1. [Problem](README.md#problem)
2. [Approach](README.md#approach)
3. [Run Instructions](README.md#run-instructions)
4. [Test Instructions](README.md#test-instructions)


# Problem

Imagine a scenario where you were given the task create an ETL (Extract, Transform, Load) so that API data is consumable by business analysts. Fortunately, your co-workers have already done the Extract step and has provided you with a .zip file containing retail order data in the raw JSON format. Your project manager has put you on the task to support these business analysts so that they can query that data using SQL from a PSQL database. While you’re at it, they would also want you to create a user table that would contain summary metrics that you think business analysts would find useful.
Note: Keep in mind that the newly created tables have to be sanely structured and those steps should be reproducible with the expectation that the ETL would run daily.

# Approach
```
      ├── README.md 
      ├── src
      │   └──dataReader.py
      │   └──dbTableWriter.py
      │   └──main.py
      │   └──sqlStatements.py
      └──requirements.txt    
```
dataReader.py ~ reads data from infile
dbTableWriter.py ~ creates table_name if it does not exist. Writes data from dataReader in configurable batch sizes
main.py ~ executed dbTableWriter.py
 
# Dependencies
- psycopg2==2.7.7
- psycopg2-binary==2.7.7
- python==3.6.3

# Run-Instructions
## Clone the Repo
```
    cd /desired/location
    git clone https://github.com/kho226/data-migration
```
## Set up virtualenv
```
    virtualenv venv
```
## Activate virtualenv
```
    source venv/bin/activate
```
## Run tool
```
    python main.py --host <host> --user <user> --password <password> --dbname <dbname> --tablename <tablename> --infile <infile> --batchsize <batchsize>
```

# Test Instructions
```
    cd /a/directory/that/doesnot/exist
    python yea_right.py
```