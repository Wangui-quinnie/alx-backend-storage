-- script that creates a stored procedure ComputeAverageWeightedScoreForUsers th-- at computes and store the average weighted score for all students.

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;

DELIMITER |

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    -- Update average score for each learner
    UPDATE users AS U
    JOIN (
        SELECT U.id, SUM(C.score * P.weight) / SUM(P.weight) AS weighted_average
        FROM users AS U
        JOIN corrections AS C ON U.id = C.user_id
        JOIN projects AS P ON C.project_id = P.id
        GROUP BY U.id
    ) AS WA ON U.id = WA.id
    SET U.average_score = WA.weighted_average;
END |

DELIMITER ;
