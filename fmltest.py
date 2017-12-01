import random

attributes = [['Sunny','Overcast','Rainy'],['Hot','Mild','Cold'],['Normal','High'],['Strong','Weak']]
num_attributes=len(attributes)

S = [['0']*num_attributes] 
G = [['?']*num_attributes] 


def pConsistent(instance):
	global G
	glist=[]
	for i in range(len(G)):
		for j in range(num_attributes):
			if G[i][j] != '?' and instance[j] != G[i][j]:
				glist.append(G[i])
				break
	for item in glist:
		G.remove(item)



def nConsistent(instance):
	global S
	slist=[]
	for i in range(len(S)):
		flag=True
		for j in range(num_attributes):
			if instance[j] != S[i][j]:
				flag=False
				break
		if flag:
			slist.append(S[i])
	for item in slist:
		S.remove(item)


def getOtherValues(index,value):
	global attributes
	return [x for x in attributes[index] if x!=value]


def generaliseS(instance):
	global S
	for sitem in S:
		if '0' in sitem:
			S.pop()
			S.append(instance)
			break
		else:
			for j in range(num_attributes):
				if sitem[j] != instance[j]:
					sitem[j]='?'
	
	
	newlist=[]
	for item in S:
		if item not in newlist:
			newlist.append(item)
	S=newlist



def specialiseG(instance):
	global G
	glist=[]
	newg=[]
	for gitem in G:
		for j in range(num_attributes):
			if gitem[j]=='?':
				vals=getOtherValues(j,instance[j])
				for v in vals:
					newitem=list(gitem)
					newitem[j]=v
					newg.append(newitem)
				if gitem not in glist:
					glist.append(gitem)
	for item in glist:
		G.remove(item)
	for item in newg:
		G.append(item)
	
	
	newlist=[]
	for item in G:
		if item not in newlist:
			newlist.append(item)
	G=newlist



def checkBoundaries(type):
	global G,S

	if type == "G": 
		glist=[] 
		for gitem in G:
			for sitem in S:
				for j in range(num_attributes):
					if sitem[j]!=gitem[j] and gitem[j]!='?' and sitem[j] != '0':
						glist.append(gitem)
						break
		for item in glist:
			G.remove(item)
	
	elif type == "S": 
		slist=[]
		for sitem in S:
			for gitem in G:
				for j in range(num_attributes):
					if sitem[j]!=gitem[j] and gitem[j]!='?' and sitem[j] != '0':
						slist.append(sitem)
						break
		for item in slist:
			S.remove(item)
	
	
	if len(G)==0:
		S=[]
	elif len(S)==0:
		G=[]



def CEA(instance,target):
	global S,G
	print "\nX:\t",instance,"\t",target,"\n"
	if target:
		pConsistent(instance)
		generaliseS(instance)
		checkBoundaries("S")
	else:
		nConsistent(instance)
		specialiseG(instance)
		checkBoundaries("G")
	print "G:\t",G	
	print "S:\t",S,"\n"



def main():
	target_concept=['Sunny','Warm','?','Strong','?','?']
	training_examples=[(['Sunny','Hot','High','Weak'],False),
	(['Sunny','Hot','High','Strong'],False),
	(['Overcast','Hot','High','Weak'],True),
	(['Rain','Mild','High','Weak'],True),
	(['Rain','Cool','Normal','Weak'],True),
	(['Rain','Cool','Normal','Strong'],False),
	(['Overcast','Cool','Normal','Strong'],True),
	(['Sunny','Mild','High','Weak'],False),
	(['Sunny','Cool','Normal','Weak'],True),
	(['Rain','Mild','Normal','Weak'],True),
	(['Sunny','Mild','Normal','Strong'],True),
	(['Overcast','Mild','High','Strong'],True),
	(['Overcast','Hot','Normal','Weak'],True),
	(['Rain','Mild','High','Strong'],False)]


	print "G:\t",G	
	print "S:\t",S,"\n"
	for i in range(4):
		CEA(training_examples[i][0],training_examples[i][1])


if __name__=="__main__":
	main()
