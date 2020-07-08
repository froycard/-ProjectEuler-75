import time
t0 = time.time()
#acc=107876 #for p<=1000000
acc=0
for p in range(12,10001,2):
    aMax=int(p*(1-1/2**(.5)))+1
    #print(p,aMax)
    count=0
    tmpA=0
    for a in range(1,aMax):
        if (p * (p - 2 * a)) % (2 * (p - a)) == 0:
            count+=1
            tmpA=a
            #if p==12: print("**",p,a)
            if count > 1: break
            #b=p*(p-2*a)//(2*(p-a))
            #c=(a*a+b*b)**(.5)
            #print(a,b,c,a+b+c)
    #print()
    
    #a=tmpA
    if count == 1:
        #b=p*(p-2*a)//(2*(p-a))
        #c=(a*a+b*b)**(.5)
        #print(a,b,c,a+b+c)
        acc+=1
print(acc)

t1 = time.time()
print(f'p = {acc} solutions in {"%.4f" % (t1 - t0)} seconds')
