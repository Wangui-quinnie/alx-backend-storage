-- List all bands with Glam rock as their main style, ranked by their longevity
-- Function to compute the lifespan based on formed and split attributes
DROP FUNCTION IF EXISTS lifespan;
DELIMITER //
CREATE FUNCTION lifespan(formed INTEGER, split INTEGER)
    RETURNS INTEGER DETERMINISTIC
BEGIN
    IF split IS NULL THEN
        RETURN 2022 - formed;
    ELSE
        RETURN split - formed;
    END IF;
END//
DELIMITER ;

-- Query to select bands with Glam rock as their main style and compute
-- their lifespan
SELECT band_name, lifespan(formed, split) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
