#Decision tree
import pandas as pd,math
from copy import deepcopy

data=pd.read_csv('dt.csv')

S=['Outlook','Temperature','Humidity','Wind']
A={'Outlook':['Sunny','Rain','Overcast'],'Temperature':['Hot','Mild','Cool'],'Humidity':['High','Normal'],'Wind':['Weak','Strong']}

def entropy(data):
	pos=len(data[data['PlayTennis']=='Yes'])
	neg=len(data[data['PlayTennis']=='No'])
	total=len(data)
	if total==0:
		return 0
	pos=float(pos)/total
	neg=float(neg)/total
	if pos==0:
		pos=1
	if neg==0:
		neg=1
	return -1*(pos*math.log(pos,2)+neg*math.log(neg,2))


def gain(E,data,attr):
	total=len(data)
	value=0
	for item in A[attr]:
		ea=entropy(data[data[attr]==item])
		num=len(data[data[attr]==item])
		value=value+(float(num)/total)*ea
	return E-value


def decisionTree():
	_dt(S,data,0)


def _dt(S,newdata,tabs):
	newS=deepcopy(S)
	
	eS=entropy(newdata)
	if eS==0:
		print "\t",newdata['PlayTennis'].iloc[0]
		return

	if len(newS)!=0:
		gains=[]
		for item in newS:
			gains.append(gain(eS,newdata,item))
		attr=newS[gains.index(max(gains))]
		print "\n","\t"*tabs,
		print attr
		newS.remove(attr)
		for item in A[attr]:
			print "\t"*tabs,
			print "\t",item,
			_dt(newS,newdata[newdata[attr]==item],tabs+2)


if __name__=="__main__":
	decisionTree()
	print "\n"