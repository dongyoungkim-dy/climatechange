# output = []
# iterate = 10
# for i in range(iterate):
#     output.append(2*(i+1))

# print(output)

# Fizz is a multiplier of 3
# Buzz is a multiplier of 5
# FizzBuzz is a common multiplier of 3 and 5
# a = 10 % 5
# print(a)
n = 100
for k in range(n):
    i = k+1
    if i % 3 == 0 and i % 5 != 0:
        print("Fizz")
    elif i % 5 == 0 and i % 3 != 0:
        print("Buzz")
    elif i % 3 == 0 and i % 5 == 0 :
        print("FizzBuzz") 
    else : print(i)

