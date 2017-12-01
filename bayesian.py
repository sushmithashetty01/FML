#Bayesian network
import pandas as pd
rain={ 'True':[0.2],
		'False':[0.8]
	 }

Hose={
	'vhose':['T','F','T','F'],
	'vrain':['T','F','F','T'],
	'values':[0.01,0.6,0.4,0.99]
    }

Yard={
	'Hose':['F','F','T','T'],
	'rain':['F','T','F','T'],
	'True':[0.0,0.8,0.9,0.99],
	'False':[1.0,0.2,0.1,0.01]
	}

df=pd.DataFrame(rain)
df1=pd.DataFrame(Hose)
df2=pd.DataFrame(Yard)

def jointprob1(df,df1,df2):
	print("probability of yard being wet given hose is true and rain is true is")
	a=(df.True).item()
	b=(df1.loc[((df1['vrain'] == 'T') & (df1['vhose'] == 'T')),'values']).item()
	c=(df2.loc[((df2['rain'] == 'T') & (df2['Hose'] == 'T')),'True']).item()
	res1= float(a*b*c)
	print(res1)
	return res1


def jointprob2(df,df1,df2):
	print("probability of yard being wet given hose is false and rain is true is")
	d=(df.True).item()
	e=(df1.loc[((df1['vrain'] == 'T') & (df1['vhose'] == 'F')),'values']).item()
	f=(df2.loc[((df2['rain'] == 'T') & (df2['Hose'] == 'F')),'True']).item()
	#print(a,b,c)
	res2=float(d*e*f)
	print(res2)
	return res2

def jointprob3(df,df1,df2):
	print("probability of yard being wet given hose is true and rain is false is")
	g=(df.False).item()
	h=(df1.loc[((df1['vrain'] == 'F') & (df1['vhose'] == 'T')),'values']).item()
	i=(df2.loc[((df2['rain'] == 'F') & (df2['Hose'] == 'T')),'True']).item()
	#print(a,b,c)
	res3= float(g*h*i)
	print(res3)
	return res3


def jointprob4(df,df1,df2):
	print("probability of yard being wet given hose is false and rain is false is")
	j=(df.False).item()
	k=(df1.loc[((df1['vrain'] == 'F') & (df1['vhose'] == 'F')),'values']).item()
	l=(df2.loc[((df2['rain'] == 'F') & (df2['Hose'] == 'F')),'True']).item()
	#print(a,b,c)
	res4=float(j*k*l)
	print(res4)
	return res4


def compute(df,df1,df2):
	res1=jointprob1(df,df1,df2)
	res2=jointprob2(df,df1,df2)
	res3=jointprob3(df,df1,df2)
	res4=jointprob4(df,df1,df2)
	print("total prob of yard being wet when raining is")
	total=float((res1+res2)/(res1+res2+res3+res4))
	print(total)
	return total

def callfunctions():
	compute(df,df1,df2)
	

if __name__ == '__main__':
	callfunctions()

	

















