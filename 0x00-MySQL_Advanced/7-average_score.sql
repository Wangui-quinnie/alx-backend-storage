-- a SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and stores the average score for a student.

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(user_id INTEGER)
BEGIN
    DECLARE avg_score FLOAT;
    SELECT AVG(score) INTO average FROM corrections
    WHERE corrections.user+id = user_id;

    -- Update the average_score for the user
    UPDATE users
    SET average_score = avg_score
    WHERE id = user_id;
END //
DELIMITER ;
