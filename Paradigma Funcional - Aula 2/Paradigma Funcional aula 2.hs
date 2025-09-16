fatorial :: Integer -> Integer
fatorial f
    | f == 0    = 1
    | f > 0     = f * fatorial (f - 1)

main :: IO ()
main = do
    print (fatorial 4)
