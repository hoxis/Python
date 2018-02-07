def collatz(num):
    if num % 2 == 0:
        return num // 2
    else:
        return num * 3 + 1

try:
    input_num = int(raw_input())
    while input_num != 1:
        print(collatz(input_num))
except expression as identifier:
    print "please input a num"