SELECT
    user_id,
    COUNT(*) AS tx_count
FROM transactions
GROUP BY user_id;
