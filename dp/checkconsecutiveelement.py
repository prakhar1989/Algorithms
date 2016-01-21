# this program check if the elements of the input array are consecutive or not
def are_consecutive(input):

    min = 2 ** 31 - 1

    for i in range(len(input)):
        if input[i] < min:
            min = input[i]

    for i in range(len(input)):
        if abs(input[i]) - min >= len(input):
            return False
        if input[abs(input[i]) - min] < 0:
            return False
        input[abs(input[i]) - min] = - input[abs(input[i]) - min]

    for i in range(len(input)):
        input[i] = abs(input[i])

    return True

input = [76, 78, 76, 77, 73, 74]
print(are_consecutive(input)) # return false

input = [76, 77, 78, 79,80]
print(are_consecutive(input)) # return true
