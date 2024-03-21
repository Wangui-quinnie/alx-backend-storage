-- List all bands with Glam rock as their main style, ranked by their longevity
SELECT band_name, 
       IF(SUBSTRING_INDEX(lifespan, '-', -1) = 'present', 
          2022 - CAST(SUBSTRING_INDEX(lifespan, '-', 1) AS UNSIGNED),
          CAST(SUBSTRING_INDEX(lifespan, '-', -1) AS UNSIGNED) - CAST(SUBSTRING_INDEX(lifespan, '-', 1) AS UNSIGNED)) AS lifespan
FROM metal_bands
WHERE main_style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
