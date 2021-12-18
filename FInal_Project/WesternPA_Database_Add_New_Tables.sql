SELECT *
INTO FranklinSnow
FROM Franklin
WHERE Snowdepth IS NOT NULL AND Snowdepth > 0

SELECT *
FROM FranklinSnow

INSERT INTO Stations
SELECT StationCode, StationName, Latitude, Longitude, Elevation
FROM FranklinSnow
WHERE ObDate = '1970-01-01'

SELECT *
FROM Stations
ORDER BY StationName

UPDATE Stations
SET StationName = 'Franklin'
WHERE Elevation = 1015

ALTER TABLE FranklinSnow
DROP COLUMN StationName, Latitude, Longitude, Elevation

DROP TABLE Franklin