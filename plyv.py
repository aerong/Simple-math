def plyv(coef,num,x)
    u=coef[-1]
	for i in xrange(num-2,0,-1)
	    u=u*x+coef[i]
	return u