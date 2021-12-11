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



