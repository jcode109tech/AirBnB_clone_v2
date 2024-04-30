-- A script that prepares a MySQL server for the project:

-- A database hbnb_dev_db
-- A new user hbnb_dev (in localhost)
-- The password of hbnb_dev should be set to hbnb_dev_pwd
-- hbnb_dev should have all privileges on the database hbnb_dev_db (and only this database)
-- hbnb_dev should have SELECT privilege on the database performance_schema (and only this database)
-- If the database hbnb_dev_db or the user hbnb_dev already exists, your script should not fail

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnh_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;

-- guillaume@ubuntu:~/AirBnB_v2$ cat setup_mysql_test.sql | mysql -hlocalhost -uroot -p
-- Enter password: 

-- guillaume@ubuntu:~/AirBnB_v2$ echo "SHOW DATABASES;" | mysql -uhbnb_test -p | grep hbnb_test_db
-- Enter password: 

-- hbnb_test_db

-- guillaume@ubuntu:~/AirBnB_v2$ echo "SHOW GRANTS FOR 'hbnb_test'@'localhost';" | mysql -uroot -p
-- Enter password: 

-- Grants for hbnb_test@localhost
-- GRANT USAGE ON *.* TO 'hbnb_test'@'localhost'
-- GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost'
-- GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost'
