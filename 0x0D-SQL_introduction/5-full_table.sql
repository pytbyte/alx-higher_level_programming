-- script that prints a decription of first_table
SELECT ALL
FROM
    information_schema.COLUMNS
WHERE
    TABLE_SCHEMA = 'hbtn_0c_0'
    AND TABLE_NAME = 'first_table';
