def squares(width, height, *mini_squares):
    output = [['.' for i in range(width)] for i in range(height)]

    for x, y, size, sym in mini_squares:
        for i in range(size):
            for j in range(size):
                output[y + i][x + j] = sym

    for i in output:
        print(*i, sep="")
    pass

