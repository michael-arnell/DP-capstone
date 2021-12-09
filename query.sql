SELECT first_name, last_name, competency_name, score
FROM (SELECT u.user_id, u.first_name, u.last_name, c.competency_id, c.competency_name, ar.score, ar.date_taken
FROM Users u
LEFT OUTER JOIN Assessment_Results ar
ON u.user_id = ar.user_id
INNER JOIN Assessments a
ON ar.assessment_id = a.assessment_id
INNER JOIN Competencies c
ON a.competency_id = c.competency_id
ORDER BY ar.date_taken DESC) AS x
GROUP BY user_id, competency_id