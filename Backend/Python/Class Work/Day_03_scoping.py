'''s = 9
def globale():
    sl = 10
    print(sl)
    def inloc():
        print(sl)
    inloc()
    print(s)

globale()
print(sl)
'''

var1 = 25

def sample2():

    global var1
    var1 += 5
    print(var1)

sample2()
print(var1)