
'''
CODE CHALLENGE: Cyclopeptide Sequencing Problem.

Image: https://ucarecdn.com/cd7fb54f-631a-4a61-8eb3-8cba63c0cb23/


Sample Input:

0 113 128 186 241 299 314 427
Sample Output:

113-128-186 113-186-128 128-113-186 128-186-113 186-113-128 186-128-113
'''

def ParentMass(Spectrum):
	return max(Spectrum)

def Expand1(Peptides):
	M=[57,71,87,97,99,101,103,113,114,115,128,129,131,137,147,156,163,186]
	Peptides1=[]
	#Peptides1.append(0)
	tmp=[]
	for i in range (len(Peptides)):
		for j in range (len(M)):
			tmp.append(Peptides[i])
			tmp.append(M[j])
			Peptides1.append(tmp)
			tmp=[]
	#print('Peptides1',Peptides1)
	return Peptides1	

def Expand(Peptides,Spectrum):
	M=[57,71,87,97,99,101,103,113,114,115,128,129,131,137,147,156,163,186]
	Peptides1=[]
	#if Peptides1.count(0)==0:
		#Peptides1.append(0)
	tmp=[]
	tmp1=[]
	for i in range (len(Peptides)):
		tmp=Peptides[i].copy()
		for j in range (len(M)):
			if M[j] in Spectrum:
				tmp1=tmp.copy()
				tmp1.append(M[j])
				Peptides1.append(tmp1)
				tmp1=[]
	#print('Peptides1',Peptides1)
	return Peptides1  

def Cyclospectrum(Peptid):
	Cyclospec = [0]
	for i in range(1,len(Peptid)):
		for j in range(len(Peptid)):
			if i+j >= len(Peptid):
				k = i+j-len(Peptid)
				Cyclospec.append(sum(Peptid[j:])+sum(Peptid[:k]))
			else:
				Cyclospec.append(sum(Peptid[j:i+j]))
	Cyclospec.append(sum(Peptid))
	Cyclospec.sort()
	
	return Cyclospec	
	
def Cyclospectrumcmp(Peptid,Spectrum):
	if Peptid==0:
		return False
	Cyclospec=Cyclospectrum(Peptid)
	if(len(Cyclospec) == len(Spectrum)):
		for i in range(len(Cyclospec)):
			if Cyclospec[i] != Spectrum[i]:
				return False
	return True

def Mass(Peptid):
	if Peptid==0:
		return 0
	sum=0
	for i in range (len(Peptid)):
		sum += Peptid[i]
	return sum

def Consistent1(Peptid, Spectrum):
	if Peptid==0:
		return False
	
	Spectrum1=Spectrum[:]
	for i in Peptid:
		if i not in Spectrum1:
			return False
		else:
			Spectrum1.remove(i)
		if Mass(Peptid) not in Spectrum1:
			return False
	return True

def Consistent(Peptid, Spectrum):
	if Peptid==0:
		return False
	#print('Peptid',Peptid)
	Peptid1 = []
	#sum=0
	for i in range(len(Peptid)):
		for j in range(1,len(Peptid)):
			if i+j <= len(Peptid):
				Peptid1.append(sum(Peptid[i:i+j]))
				
	#Peptid1.append(Mass(Peptid))
	Peptid1.sort()	
	#print('Peptid1',Peptid1)
	Spectrum1=Spectrum[:]
	for i in Peptid1:
		if i not in Spectrum1:
			return False
		else:
			Spectrum1.remove(i)
		if Mass(Peptid) not in Spectrum1:
			return False
	return True
								 



####################################################################################################
Spectrum = list(map(int, input().split()))
#print(Spectrum)
#print(ParentMass(Spectrum))
MASS=[57,71,87,97,99,101,103,113,114,115,128,129,131,137,147,156,163,186]

#i=0
Peptides=[[]]
#Peptides.append(0)
for i in range(len(Spectrum)):
	if Spectrum[i] in MASS:
		Peptides.append(Spectrum[i])
		
#print(Peptides)


Peptides=Expand1(Peptides)
for i in range(len(Peptides)-1,-1,-1):
	if (Consistent1(Peptides[i], Spectrum)==False):
		Peptides.remove(Peptides[i])

tmplist=[[]]
for i in range(len(Peptides)-1,-1,-1):
	if (Mass(Peptides[i])==ParentMass(Spectrum)):
		if(tmplist.count(Peptides[i])==0):
			tmplist.append(Peptides[i])
			print('-'.join(map(str,Peptides[i])))
#c=2			
while (len(Peptides)!=0):
	Peptides=Expand(Peptides,Spectrum)
	#c+=1
	for i in range(len(Peptides)-1,-1,-1):
		if (Mass(Peptides[i])==ParentMass(Spectrum)):
			if (Cyclospectrumcmp(Peptides[i],Spectrum)==True):
				if(tmplist.count(Peptides[i])==0):
					tmplist.append(Peptides[i])
					#print(Peptides[i])
					print('-'.join(map(str,Peptides[i])))
			Peptides.remove(Peptides[i])
		else:
			if (Consistent(Peptides[i], Spectrum)==False):
				#print('c= ',c)
				Peptides.remove(Peptides[i])
if(len(tmplist)==0):
	print(0)
#for i in range (len(tmplist)-1,-1,-1):
	#print('-'.join(map(str,tmplist[i])))
