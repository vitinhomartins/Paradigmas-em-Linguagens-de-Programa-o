fatorialEmCauda :: Integer -> Integer -> Integer
fatorialEmCauda n1 n2 
            | n1 == 0 = n2
            |otherwise = fatorialEmCauda (n1 - 1) (n2 * n1)

main :: IO()
main = do
    print(fatorialEmCauda 5 1)