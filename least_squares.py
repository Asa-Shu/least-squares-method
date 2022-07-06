import sys

print("x をスペース区切りで入力してください\n例） 1.0 1.5 2.0")
x = list(map(float, input().split()))
print()

print("y をスペース区切りで入力してください\n例） 12.3 15.6 16.0")
y = list(map(float, input().split()))
print()


def least_squares(x, y):
    n = len(x)

    if n != len(y):
        print("Error: x と y の要素数が一致していません。")
        sys.exit()


    x2_sum = xy_sum = x_sum = y_sum = 0

    for i in range(n):
        x2_sum += x[i]**2
        xy_sum += x[i] * y[i]
        x_sum += x[i]
        y_sum += y[i]

    a = (n * xy_sum - x_sum * y_sum)/(n * x2_sum - x_sum**2)
    b = (x2_sum * y_sum - x_sum * xy_sum)/(n * x2_sum - x_sum**2)
    if b >= 0:
        b_str = "+ " + str(b)
    else:
        b_str = "- " + str(-b)

    print("------最小二乗法の結果------")
    print("y =", a, "x", b_str)
    print('傾き =', a)
    print('切片 =', b)


least_squares(x, y)
