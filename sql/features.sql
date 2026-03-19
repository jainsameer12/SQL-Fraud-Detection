SELECT
    user_id,
    COUNT(*) AS tx_count,
    AVG(amount) AS avg_amount,
    COUNT(DISTINCT location) AS location_count,
    MAX(is_fraud) AS is_fraud
FROM transactions
GROUP BY user_id;
