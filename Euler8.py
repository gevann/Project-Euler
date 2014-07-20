file = open( "euler8source.txt", "r")
source = []

#read the input
while 1:
    char = file.read(1)
    if char == "\n": continue
    if not char: break
    val = int( char )
    source.append( val )

#set vars
i = 1
t = source[0:13]
ts = t[:]
ts.sort()
n = source[1:14]
ns = []

#checks if given array of 13 will be larger or smaller
# than the current largest
def check():
    k = i + 13
    n = source[i: k]
    ns = n[:]
    ns.sort()
    for x in range(0, 13):
        if ns[x] < ts[x]:
            return False
        else:
            return True

for i in range( 1, 1000-13):
    #advance counter until num bigger curr array minimum
    while source[i] < ts[0]:
        i += 1
    #if check if larger, reassign curr array if so
    if check():
        t = source[i: i+13]
        ts = t[:]
        ts.sort()

answer = reduce( lambda x, y: x*y, t)
print answer
