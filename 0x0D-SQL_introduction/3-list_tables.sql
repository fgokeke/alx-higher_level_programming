-- SQL script to list all tables in a specified database

SET @db_name = 'mysql';
SELECT @db_name INTO @check_db_name;
USE mysql;
SHOW TABLES;
