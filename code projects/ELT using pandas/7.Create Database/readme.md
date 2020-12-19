## Stage seven: Create Database

#### Summary
In stage seven, Mongo database is initialized, and the datasets from stage six are uploaded to Mongo Server.

#### Files (in order they should be executed)
#### create_database.js
The code in this file initialize the Database on mongo server, creates two collections (one for master dataset and another for selected questions) and then uploads **selectedQs_dataset.0.0.2.csv** and **master_longDataSet.0.0.6.csv** into these collections respectively.

#### selectedQs.sql
This file contains the code to create a SQL Database and table for the selected questions.

