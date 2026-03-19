SELECT
    user_id,
    AVG(amount) AS avg_amount,
    COALESCE(STDDEV(amount), 0) AS std_amount
FROM transactions
GROUP BY user_id;
