SELECT
    user_id,
    COUNT(DISTINCT location) AS location_count
FROM transactions
GROUP BY user_id;
