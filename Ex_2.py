# Average of elements in the list or tuple.
elems = []
def Avg(*args):
    elems = list(args)
    Average = sum(elems) / len(elems)
    print(Average)

a = 10
b = 5
#Problem
Avg(a,b)
