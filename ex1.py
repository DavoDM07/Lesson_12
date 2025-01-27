#Write a Python program to square and cube every number in a given list of
#integers using Lambda.


give_me_square = map(lambda x:x ** 2, [1,2,3,4,5,6])
give_me_cube = map(lambda x:x ** 3, [1,2,3,4,5,6])

print(list(give_me_cube))
print(list(give_me_square))
