-- SQL Challenge: Solution.

-- 1. Write the query that only returns the email_address column.
-- 2. Join the tables together using the join_id column present in both tables
-- Column_1 needs to be divisible by 2 without creating a decimal number (or modulo)
-- column_2 needs to be smaller then column_1
-- Column_3 needs to end with a 1
-- This should result in an email-address

SELECT email
FROM NIMBUS_TEST.PUBLIC.DATA_TABLE
INNER JOIN NIMBUS_TEST.PUBLIC.EMAIL_TABLE ON DATA_TABLE.JOIN_ID = EMAIL_TABLE.JOIN_ID
WHERE Column_1 % 2 = 0 AND column_2 < column_1 AND RIGHT(CAST(Column_3 AS VARCHAR), 1) = '1';
