for i in range(10):
    for j in range(i + 1, 10):
        if i < 9 or j < 9:
            print("{}{}".format(i, j), end=", ")
        