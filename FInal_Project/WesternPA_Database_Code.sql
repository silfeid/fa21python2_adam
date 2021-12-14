USE WesternPA

CREATE TABLE dbo.Stations
(
	StationCode nvarchar(50) primary key NOT NULL,
	StationName nvarchar(50) NOT NULL,
	Latitude float NOT NULL,
	Longitude float NOT NULL,
	Elevation float NOT NULL
	)

SELECT *
FROM Stations

DECLARE @Counter int
SET @Counter = 8

WHILE @Counter > 0
	BEGIN
		UPDATE Stations
		SET Elevation = ROUND(Elevation, 0)
		WHERE StationNumber = @Counter
		SET @Counter = @Counter -1
	END

SELECT *
FROM Stations

SELECT *
INTO ErieNoNulls
FROM Erie
WHERE Erie.Snowdepth IS NOT NULL

SELECT *
INTO ErieSnow
FROM ErieNoNulls
WHERE Snowdepth > 0

SELECT *
FROM Erie

SELECT *
FROM DuboisNoNulls


SELECT *
INTO Laurel_MountainNoNulls
FROM Laurel_Mountain
WHERE Laurel_Mountain.Snowdepth IS NOT NULL

SELECT *
INTO Laurel_MountainSnow
FROM Laurel_Mountain
WHERE Laurel_Mountain.Snowdepth IS NOT NULL AND Laurel_Mountain.Snowdepth > 0

SELECT *
INTO Laurel_MountainSnowCheck
FROM Laurel_MountainNoNulls
WHERE Laurel_MountainNoNulls.Snowdepth > 0

SELECT *
INTO IndianaSnow
FROM Indiana
WHERE Indiana.Snowdepth IS NOT NULL AND Indiana.Snowdepth > 0

SELECT *
INTO UniontownSnow
FROM Uniontown
WHERE Uniontown.Snowdepth IS NOT NULL AND Uniontown.Snowdepth > 0

