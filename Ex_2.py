# Average of elements in the list or tuple.
elems = []
def Avg(args):
    elems = list(args)
    Average = sum(elems) / len(elems)
    print(Average)

a = [10,10,10,10,9]
b = (1,3,2,4,5)
Avg(a)
Avg(b)
