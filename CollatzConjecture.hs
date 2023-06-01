module CollatzConjecture (collatz) where

collatzPositive :: Integer -> Integer -> Integer
collatzPositive n length
    | n == 1    = length
    | even n    = collatzPositive(n `div` 2) (length + 1)
    | otherwise = collatzPositive(3 * n + 1) (length + 1)

collatz :: Integer -> Maybe Integer
collatz n
        | n <= 0 = Nothing 
        | otherwise = Just (collatzPositive n 0)
