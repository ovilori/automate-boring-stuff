def my_list(*args):
    t1 = (args)
    t2 = (args[0])
    t3 = (args[1])

    print(type(t1))
    #print(t1)
    print(type(t2))
    #print(t2)
    print(type((t3,)))
    #print(t3)

my_list(1,2,3)