def draw_tree(levels):
    for i in range(levels):
        print(" " * (levels - i - 1) + "*" + " " * (i))
        for j in range(i + 1):
            print(" " * (levels - j - 1) + "/" + "|" * (j * 2) + "\\")
    print(" " * (levels - 1) + "|")
    print(" " * (levels - 1) + "*")

draw_tree(5)
