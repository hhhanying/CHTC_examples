from sum import mysum, mymul
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
outname = sys.argv[3]

res1 = mysum(a,b)
res2 = mymul(a,b)
print("finish")

f = open(outname+str(a)+".txt", "w")
f.write(str(res1)+","+str(res2))
f.close()
