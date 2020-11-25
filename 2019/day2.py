#PART 1
# with open("day2input.txt", 'r') as f:
#     arr = [int(x) for x in f.read().split(",")]

#     # before running the program, replace position 1 with the value 12 and replace position 2 with the value 2.
#     arr[1] = 12
#     arr[2] = 2

#     i = 0
#     while(arr[i] != 99):
#         if(arr[i] == 1):
#             arr[arr[i+3]] = arr[arr[i+1]] + arr[arr[i+2]]
#         elif(arr[i] == 2):
#             arr[arr[i+3]] = arr[arr[i+1]] * arr[arr[i+2]]
#         i+=4
    
#     print(arr[0])

#PART 2
target = 19690720
def func():
    with open("2019/day2input.txt", 'r') as f:
        arr = [int(x) for x in f.read().split(",")]

        for noun in range(100):
            for verb in range(100):
                temp = arr.copy()
                temp[1] = noun
                temp[2] = verb
                
                i = 0
                while(temp[i] != 99):
                    if(temp[i] == 1):
                        temp[temp[i+3]] = temp[temp[i+1]] + temp[temp[i+2]]
                    elif(arr[i] == 2):
                        temp[temp[i+3]] = temp[temp[i+1]] * temp[temp[i+2]]
                    i+=4
                
                if temp[0] == target:
                    return 100 * noun + verb # this is the answer to be submitted


# print(frontback)
print(func())
    