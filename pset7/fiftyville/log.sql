-- Keep a log of any SQL queries you execute as you solve the mystery.
.tables #find out about all the available tables in the database

SELECT *
FROM crime_scene_reports
LIMIT 15;
to find out about the content of the table

SELECT *
FROM crime_scene_reports
WHERE year=2021
AND month=7
AND day=28
AND description LIKE "Theft%";
Return the exact description of the crime in the crime scene reports.

SELECT *
FROM bakery_security_logs
WHERE year=2021
AND month=7
AND day=28
AND hour=10
Find out who entered and exited the bakery around the time of the crime.
