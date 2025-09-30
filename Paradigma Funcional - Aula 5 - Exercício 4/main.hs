maiorElemento :: [Int] -> Int
maiorElemento []  = 0
maiorElemento [x] = x
maiorElemento lista
    | head lista > maiorElemento (tail lista) = head lista
    | otherwise = maiorElemento (tail lista)
    
main :: IO()
main = do
    print(maiorElemento [9, -205, 23435, 7, 2])