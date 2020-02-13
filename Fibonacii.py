def get_fib():
    a = 1
    b = 2
    count = 0
    new_num = 0
    fib_list = [a,b]
    while new_num < 4000000:
        count += 1
        new_num = a + b
        #print(new_num)
        fib_list.append(new_num)
        a = fib_list[1+count]
        b = fib_list[count]
    fib_list.remove(fib_list[-1])
    return fib_list
    
def get_sum(fibi):
    sum = 0
    for i in fibi:
        if i % 2 != 0:
            #print(i)
            sum += i
    print("The sum of the odd numbers are",sum)

get_fib()
get_sum(get_fib())