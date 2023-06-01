module Anagram (anagramsFor) where

import Data.Char (toLower)
import Data.List (sort)

lowerStr :: String -> String
lowerStr s = map toLower s

anagramsFor :: String -> [String] -> [String]
anagramsFor x s = [y | y <- s, lowerStr y /= lowerStr x, sort(lowerStr x) == sort(lowerStr y)]
