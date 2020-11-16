# 17. Write a Python program to print alphabet pattern 'A'.

elem = ""
for row in range(0, 7):
    for col in range(0, 7):
        if (((row == 0 or row == 3) and (col > 0 and col < 6)) or (row != 0 and (col == 0 or col == 6))):
            elem = elem + "*"
        else:
            elem = elem + " "
    elem = elem + "\n"
print(elem)

# 18. Write a Python program to print alphabet pattern 'D'.

elem = ""
for row in range(0, 7):
    for col in range(0, 7):
        if (((row != 0 or row != 6) and col == 6) or (col == 0 or ((row == 0 or row == 6)) and (col > 0 and col < 6))):
            elem = elem + "*"
        else:
            elem = elem + " "
    elem = elem + "\n"
print(elem)

# 19. Write a Python program to print alphabet pattern 'D'.

elem = ""
for row in range(7):
    for col in range(7):
        if ((col == 0 or (row == 0 or row == 6)) or (row == 3 and (col < 6))):
            elem = elem + "*"
        else:
            elem = elem + " "
    elem = elem + "\n"
print(elem)

# 20. Write a Python program to print alphabet pattern 'G'.

elem = ""
for row in range(0, 7):
    for col in range(0, 7):
        if (((row == 0 or row == 6) and (col > 1 and col < 5)) or (row != 2 and (row > 0 and row < 6)) and (col == 0 or col == 6)
            or (col == 0 and row == 2) or (row == 3 and col != 1)):
            elem = elem + "*"
        else:
            elem = elem + " "
    elem = elem + "\n"
print(elem)

# 21. Write a Python program to print alphabet pattern 'L'.

elem = ""
for row in range(0, 7):
    for col in range(0, 7):
        if ((col == 0 and row < 7) or (row == 6 and col < 7)):
            elem = elem + "*"
        else:
            elem = elem + " "
    elem = elem + "\n"
print(elem)

# 22. Write a Python program to print alphabet pattern 'M'

elem = ""
for row in range(0, 7):
    for col in range(0, 7):
        if (((row != 2 or row != 3) and (col == 0 or col == 6)) or ((row == 2) and (col == 2 or col == 4))
            or (row == 3 and col == 3)):
            elem = elem + "*"
        else:
            elem = elem + " "
    elem = elem + "\n"
print(elem)


# 23. Write a Python program to print alphabet pattern 'O'.

elem = ""
for row in range(0, 7):
    for col in range(0, 7):
        if (((row == 0 or row == 6) and (col > 0 and col < 6)) or ((col == 0 or col == 6) and (row > 0 and row < 6))):
            elem = elem + "*"
        else:
            elem = elem + " "
    elem = elem + "\n"
print(elem)

# 24. Write a Python program to print alphabet pattern 'P'.

elem = ""
for row in range(0, 7):
    for col in range(0, 7):
        if (((row == 0 or row == 3) and col < 4) or ((row > 0 and row < 3) and (col == 0 or col == 4)) or 
            (col == 0 and row > 3)):
            elem = elem + "*"
        else:
            elem = elem + " "
    elem = elem + "\n"
print(elem)

# 25. Write a Python program to print alphabet pattern 'R'.

elem = ""
for row in range(0, 7):
    for col in range(0, 7):
        if (((row == 0 or row == 3) and (col < 4)) or ((row > 0 and row < 3) and (col == 0 or col == 4)) or 
            (row == 4 and (col == 2 or col == 0)) or (row == 5 and (col == 3 or col == 0)) or (row == 6) and (col == 4 or col == 0)):
            elem = elem + "*"
        else:
            elem = elem + " "
    elem = elem + "\n"
print(elem)

# 27. Write a Python program to print alphabet pattern 'T'.

elem = ""
for row in range(0, 7):
    for col in range(0, 7):
        if ((row == 0 and (col > 0 and col < 6)) or (col == 3 and (row > 0 and row < 6))):
            elem = elem + "*"
        else:
            elem = elem + " "
    elem = elem + "\n"
print(elem)

# 28. Write a Python program to print alphabet pattern 'U'.

elem = ""
for row in range(0, 7):
    for col in range(0, 7):
        if ((row == 0 and (col == 0 or col == 6)) or (row == 6 and (col > 0 and col < 6)) or
            ((col == 0 or col == 6) and row < 6)):
            elem = elem + "*"
        else:
            elem = elem + " "
    elem = elem + "\n"
print(elem)

# 29. Write a Python program to print alphabet pattern 'X'.

elem = ""
for row in range(0, 7):
    for col in range(0, 5):
        if (((row < 2 or row > 4) and (col == 0 or col == 4)) or ((row == 2 or row == 4) and (col == 1 or col == 3)) or
            (row == 3 and col == 2)):
            elem = elem + "*"
        else:
            elem = elem + " "
    elem = elem + "\n"
print(elem)

# 30. Write a Python program to print alphabet pattern 'Z'.

elem = ""
for row in range(0, 7):
    for col in range(0, 7):
        if (((row == 0 or row == 6)) or (row == 1 and col == 5) or (row == 2 and col == 4) or (row == 3 and col == 3) or
            (row == 4 and col == 2) or (row == 5 and col == 1)):
            elem = elem + "*"
        else:
            elem = elem + " "
    elem = elem + "\n"
print(elem)
