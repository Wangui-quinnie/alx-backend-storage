-- a SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and stores the average score for a student.

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(user_id INTEGER)
BEGIN
    DECLARE total_score DECIMAL(10, 2);
    DECLARE num_corrections INTEGER;
    DECLARE avg_score DECIMAL(10, 2);

    -- Calculate total score for the user
    SELECT SUM(score)
    INTO total_score
    FROM corrections
    WHERE user_id = user_id;

    -- Count the number of corrections for the user
    SELECT COUNT(*)
    INTO num_corrections
    FROM corrections
    WHERE user_id = user_id;

    -- Compute average score
    IF num_corrections > 0 THEN
        SET avg_score = total_score / num_corrections;
    ELSE
        SET avg_score = 0;
    END IF;

    -- Update the average_score for the user
    UPDATE users
    SET average_score = avg_score
    WHERE id = user_id;
END //
DELIMITER ;
