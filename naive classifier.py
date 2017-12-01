#Naive bayes classifier
#import pandas as pd

#data=pd.read_csv('data.csv')
#data=data.values.tolist()
data=[['Sunny','Hot','High','Weak','No'],
['Sunny','Hot','High','Strong','No'],
['Overcast','Hot','High','Weak','Yes'],
['Rain','Mild','High','Weak','Yes'],
['Rain','Cool','Normal','Weak','Yes'],
['Rain','Cool','Normal','Strong','No'],
['Overcast','Cool','Normal','Strong','Yes'],
['Sunny','Mild','High','Weak','No'],
['Sunny','Cool','Normal','Weak','Yes'],
['Rain','Mild','Normal','Weak','Yes'],
['Sunny','Mild','Normal','Strong','Yes'],
['Overcast','Mild','High','Strong','Yes'],
['Overcast','Hot','Normal','Weak','Yes'],
['Rain','Mild','High','Strong','No']]


attributes=['Sunny','Cool','High','Strong']
concept=['Yes','No']

def conceptProbability(value):
	total=len(data)
	total_value=len([item for item in data if item[-1]==value])
	return float(total_value)/total

def attributeProbability(index,value):
	total=len([item for item in data if item[-1]==value])
	attribute_total=len([item for item in data if item[-1]==value and attributes[index]==item[index]])
	return float(attribute_total)/total

def naiveBayes():
	values=[]
	for value in concept:
		cp=conceptProbability(value)
		ap=1
		for i in range(len(attributes)):
			ap=ap*attributeProbability(i,value)
		values.append(ap*cp)

	nsum=sum(values)
	nvalues=[format(v/nsum,'.5f') for v in values]
	print "Normalised values:",nvalues
	return nvalues.index(max(nvalues))

if __name__=="__main__":
	index=naiveBayes()
	print attributes,"--> Play Tennis:",concept[index]