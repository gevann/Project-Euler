if __name__ == "__main__":
    numbers = range( 0, 2000000 )
    numbers[1] = 0
    answer = []
    for n in numbers:
        if n != 0:
            answer.append(n)
            i = n + n
            while i < len( numbers ):
                numbers[i] = 0
                i = i + n

    print( sum( answer ) )
