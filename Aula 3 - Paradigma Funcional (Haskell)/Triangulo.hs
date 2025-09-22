classificaTriangulo :: Int -> Int -> Int -> String
classificaTriangulo a b c
    | not (valido a b c) = "Invalido"
    | a == b && b == c   = "Equilatero"
    | a == b || b == c || a == c = "Isoceles"
    | otherwise= "Escaleno"
  where
    valido x y z = x + y > z && x + z > y && y + z > x
    
main :: IO()
main = do
    print(classificaTriangulo 3 3 3)