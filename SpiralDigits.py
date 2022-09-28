M, N = map(int, input().split(','))
a = [[0] * M for i in range(N)]
k, digit = 0, 0
left_corner, right_corner, high_bound, lower_bound = 0, M - 1, 0, N - 1
while (k < M * N):
    current_left_corner = left_corner
    current_high_bound = high_bound
    for current_left_corner in range(left_corner, right_corner + 1):
        a[current_high_bound][current_left_corner] = digit
        digit = (digit + 1) % 10
        k += 1
    high_bound += 1
    if k < M * N:
        for current_high_bound in range(high_bound, lower_bound + 1):
            a[current_high_bound][current_left_corner] = digit
            digit = (digit + 1) % 10
            k += 1
        right_corner -= 1
    if k < M * N:
        for current_left_corner in range(right_corner, left_corner - 1, -1):
            a[current_high_bound][current_left_corner] = digit
            digit = (digit + 1) % 10
            k += 1
        lower_bound -= 1
    if k < M * N:
        for current_high_bound in range(lower_bound, high_bound - 1, -1):
            a[current_high_bound][current_left_corner] = digit
            digit = (digit + 1) % 10
            k += 1
        left_corner += 1

for i in range(N):
    print(*a[i])
