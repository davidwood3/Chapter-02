message = "Hello Python world!"
print(message)

favorite_language = 'python '
favorite_language = favorite_language.rstrip()
print(favorite_language)

#hello

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

byThrees = []
byThrees = range(3,31,3)
for three in byThrees:
    print(three)

cubes = [three**3 for three in byThrees]
for three in cubes:
    print(three)