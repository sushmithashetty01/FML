#K nearest
import math

data=[[7,7,'Bad'],[7,4,'Bad'],[3,4,'Good'],[1,4,'Good']]
new=[3,7]
concept={}

def calculateDistance():
	distances=[]
	for item in data:
		total=0
		for i in range(len(item)-1):
			disq=math.pow(item[i]-new[i],2)
			total=total+disq
		distances.append([math.sqrt(total),item[-1]])
	return distances

def predictOutcome(concept):
	values=list(concept.values())
	keys=list(concept.keys())
	maxval=max(values)
	count=0
	for v in values:
		if maxval==v:
			count=count+1
	if count>1:
		return "Uncertain decision"
	else:
		return keys[values.index(maxval)]
	
def KNN(k):
	outcomes=[]
	distances=calculateDistance()
	keys=sorted([d[0] for d in distances])
	for i in range(k):
		outcomes.extend(d[1] for d in distances if d[0]==keys[i])
	
	#get frequency count for each outcome
	concept={x:outcomes.count(x) for x in outcomes}
	return predictOutcome(concept)
	

if __name__=="__main__":
	print "Enter k value(1-4): ",
	k=input()
	if k>4:
		k=4
	print "Outcome: ",KNN(k)
