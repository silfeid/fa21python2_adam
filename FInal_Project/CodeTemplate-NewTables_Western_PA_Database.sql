USE Western_PA_Climate_DB

SELECT *
FROM TionestaSnow

SELECT *
INTO TionestaSnow
FROM Tionesta
WHERE Snowdepth > 0

SELECT *
FROM Stations
ORDER BY StationName

UPDATE Stations
SET StationName = 'Tionesta 2 SE Lake, PA US'
WHERE Latitude = 41.4792

ALTER TABLE Stations
DROP COLUMN StationNumber

INSERT INTO Stations
SELECT StationCode, StationName, Latitude, Longitude, Elevation FROM Tionesta WHERE ObDate = '1970-01-01'

SELECT *
INTO WaynesburgSnow
FROM Waynesburg
WHERE Waynesburg.Snowdepth > 0

ALTER TABLE Tionesta
DROP COLUMN StationCode, StationName, Latitude, Longitude, Elevation