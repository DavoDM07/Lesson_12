#Write a Python program to find intersection of two given arrays using lambda


list_1 = [1, 2, 3, 5, 7, 8, 9, 10]
list_2 = [1, 2, 4, 8, 9]
intersection = list(filter(lambda x: x in list_2, list_1))
print(intersection)

