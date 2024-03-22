-- A script that contains a stored procedure that
-- computes and stores the weighted average score
-- for a student.

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser (user_id INTEGER)
BEGIN
    DECLARE total_weight INTEGER;
    DECLARE weighted_sum FLOAT;

    -- Calculate the total weight
    SELECT SUM(projects.weight)
    INTO total_weight
    FROM corrections
    JOIN projects ON corrections.project_id = projects.id
    WHERE corrections.user_id = user_id;

    -- Calculate the weighted sum
    SELECT SUM((projects.weight / total_weight) * corrections.score)
    INTO weighted_sum
    FROM corrections
    JOIN projects ON corrections.project_id = projects.id
    WHERE corrections.user_id = user_id;

    -- Update the average score for the user
    UPDATE users
    SET average_score = weighted_sum
    WHERE id = user_id;
END //

DELIMITER ;
