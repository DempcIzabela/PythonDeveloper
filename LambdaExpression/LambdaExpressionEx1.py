# function
def my_function(x):
    if x < 0:
        y = -1
    else:
        y = 1
    return y


# lambda expression
firstexpression = (lambda x: -1 if x < 0 else 1)(-1)
