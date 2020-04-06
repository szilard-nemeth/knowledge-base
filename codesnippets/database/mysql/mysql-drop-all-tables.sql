--https://stackoverflow.com/questions/3476765/mysql-drop-all-tables-ignoring-foreign-keys

SET FOREIGN_KEY_CHECKS = 0;

SELECT concat('DROP TABLE IF EXISTS ', table_name, ';')
FROM information_schema.tables
WHERE table_schema = 'homedb';

SET FOREIGN_KEY_CHECKS = 1;