def sum_even(mylist):
    mylist =[1,3,5,6,8,10,34,2,0,3]
    result = 0
    for i in mylist:
        if not i % 2:
            result += i
            print(result)
