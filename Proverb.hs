module Proverb(recite) where

beginSentence     = "For want of a "
connectorWord     = " the "
endSentence       = " was lost.\n"
beginLastSentence = "And all for the want of a "
endLastSentence   = "."

reciteFirst :: [String] -> String
reciteFirst (x:xs) = if Prelude.length xs > 0 then beginSentence ++ x ++ connectorWord ++ head xs ++ endSentence ++ reciteFirst xs else "" 

reciteLast :: [String] -> String
reciteLast input = beginLastSentence ++ head input ++ endLastSentence

recite :: [String] -> String
recite [] = ""
recite input = reciteFirst input ++ reciteLast input


