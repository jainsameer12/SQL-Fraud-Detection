SELECT
    user_id,
    COUNT(DISTINCT device_id) AS device_count
FROM transactions
GROUP BY user_id;
