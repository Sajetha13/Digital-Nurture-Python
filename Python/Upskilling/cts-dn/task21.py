def fun():
    if True:
        if True:
            print("nested")
        else:
            print("not nested")
    else:
        print("not nested")
fun()