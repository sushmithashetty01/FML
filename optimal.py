#Bayes optimal Classifier
hID=[0.4,0.3,0.3]
pIh=[1,0,0]
nIh=[0,1,1]

values=['positive','negative']

def hMap(num):
	mapvalues=[]
	for value in values:
		total=0
		for i in range(num):
			if value[0]=='p':
				total=total+(hID[i]*pIh[i])
			else:
				total=total+(hID[i]*nIh[i])
		mapvalues.append(total)
	return mapvalues.index(max(mapvalues))


def bayesOptimumClassifier():
	print values[hMap(3)]

if __name__=="__main__":
	bayesOptimumClassifier()