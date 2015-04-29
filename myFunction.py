import numpy as np

def add_one(x):
	return x+1

def similarity_conditional(freqUV,freqU, u, v):
    # log= logging.getLogger( "SomeTest.testSomething" )
    # log.debug( "this= %r", freqU[u])
    if (freqU[u] == 0) or (freqU[v] == 0):
        print("WARNING: Cannot calculate conditional similarity (divide by zero?). Return 0")
        return 0
    else:
        return freqUV[u,v] / (freqU[u] * freqU[v])


def myDivide(a,b):
	try:
		return a/b
	except:
		return 0
# print(myDivide(1,0))

# if __name__ == '__main__':
#     print("Hello %s" % (some_function()))