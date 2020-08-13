original_list = [1, 2, 3, 4, 5]


def square(number):
    return number**2


squares = map(square, original_list)

square_list = list(squares)
print(square_list)