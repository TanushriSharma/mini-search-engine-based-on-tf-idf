#!/usr/bin/python
from nltk.stem import PorterStemmer
from collections import defaultdict
from operator import itemgetter
import re,thread,threading,time
import math

n=12339000
#global result
result={}
result=defaultdict(lambda:[0,0],result)
f=open('secindex1','r')
f2=open('indexfile1','r')
f3=open('docindex','r')
docs=f3.readlines()
f3.close()
seclst=f.readlines()
f.close()
def search(seclst):
	flag=0
	global result
	high=len(seclst)
	low=0
	mid=(high+low)/2
	s=seclst[mid]	
	while low<=high:
		if s.split(':')[0]==word:
			flag=1
			bytes=int(s.split(':')[1].replace('\n',''))
			f2.seek(bytes,0)
			ch5=f2.readline()
			ch=re.findall( '[0-9]{1,}', ch5,re.DOTALL)
			tit=re.findall( r'\"t\":\[(.*?)\]', ch5,re.DOTALL)
		
			if len(tit)>0:
				ch6=re.findall( r'[0-9]{1,}', tit[0],re.DOTALL)
				tit=ch6
				tit=ch6[0:-1:2]
			else:
				tit=[]
			ch3=ch[0:-1:2]
			ch2=[]
			freq=[]
			ch7=[]
			freq7=[]
			for i in range(0,len(ch3)):
				if ch3[i] not in ch2:
					ch2.append(ch3[i])
					freq.append(int(ch[i+1]))
				else:
					j=ch2.index(ch3[i])
					freq[j]+=1
			for i in range(0,len(tit)):
				if tit[i] not in ch7:
					ch7.append(tit[i])
					freq7.append(int(ch6[i+1]))
				else:
					j=ch7.index(tit[i])
					freq7[j]+=1
			ch=[]
			chtit=[]
			#print len(freq),len(ch2)
			for i in range(0,len(ch2)):
				ch.append(ch2[i])
				ch.append(freq[i])
			l=len(ch)/2
			#print ch2
			for i in range(0,len(ch),2):
				result[ch[i]][1]+=int(ch[i+1])*math.log(n/l,2)*0.3
				result[ch[i]][0]+=1
			for i in range(0,len(ch7)):
				chtit.append(ch7[i])
				chtit.append(freq7[i])
								
			for i in range(0,len(chtit),2):
				result[chtit[i]][1]+=int(chtit[i+1])*math.log(n/l,2)*0.7
				result[chtit[i]][0]+=1
			#for i in ch[0:-1:2]:
			#	print docs[int(i)-2]
			f2.seek(0,0)
			
			break
		elif s.split(':')[0]<word:
			low=mid+1
			mid=low + (high-low)/2
			
		else:
			high=mid-1
			mid=low + (high-low)/2
		s=seclst[mid]
	if flag==0:
		for s in seclst:
			if s.split(':')[0]==word:
				bytes=int(s.split(':')[1].replace('\n',''))
				f2.seek(bytes,0)
				ch5=f2.readline()
				ch=re.findall( '[0-9]{1,}', ch5,re.DOTALL)
				tit=re.findall( r'\"t\":\[(.*?)\]', ch5,re.DOTALL)
				print tit
				if len(tit)>0:
					ch6=re.findall( r'[0-9]{1,}', tit[0],re.DOTALL)
					tit=ch6
					tit=ch6[0:-1:2]
				else:
					tit=[]
				ch3=ch[0:-1:2]
				ch2=[]
				freq=[]
				ch7=[]
				freq7=[]
				for i in range(0,len(ch3)):
					if ch3[i] not in ch2:
						ch2.append(ch3[i])
						freq.append(int(ch[i+1]))
					else:
						j=ch2.index(ch3[i])
						freq[j]+=1
				for i in range(0,len(tit)):
					if tit[i] not in ch7:
						ch7.append(tit[i])
						freq7.append(int(ch6[i+1]))
					else:
						j=ch7.index(tit[i])
						freq7[j]+=1
				ch=[]
				chtit=[]
				#print len(freq),len(ch2)
				for i in range(0,len(ch2)):
					ch.append(ch2[i])
					ch.append(freq[i])
	
				l=len(ch)/2
				#print ch2
				for i in range(0,len(ch),2):
					result[ch[i]][1]+=int(ch[i+1])*math.log(n/l,2)*0.3
					result[ch[i]][0]+=2
				for i in range(0,len(ch7)):
					chtit.append(ch7[i])
					chtit.append(freq7[i])
	
				
				for i in range(0,len(chtit),2):
					result[chtit[i]][1]+=int(chtit[i+1])*math.log(n/l,2)*0.7
					result[chtit[i]][0]+=5
				#for i in ch[0:-1:2]:
				#	print docs[int(i)-2]
				f2.seek(0,0)
				
				break
def search2(ch):
	ch3=ch[0:-1:2]
	ch2=[]
	freq=[]
	global result
	for i in range(0,len(ch3)):
		if ch3[i] not in ch2:
			ch2.append(ch3[i])
			freq.append(int(ch[i+1]))
		else:
			j=ch2.index(ch3[i])
			freq[j]+=1
	ch=[]
		
	for i in range(0,len(ch2)):
		ch.append(ch2[i])
		ch.append(freq[i])
	l=len(ch)/2
	for i in range(0,len(ch),2):
		result[ch[i]][1]+=int(ch[i+1])*math.log(n/l,2)
		result[ch[i]][0]+=1
				
	f2.seek(0,0)
	
				
def title(titleq,seclst):
	
	#qw=titleq.split()
	querywords=[]
	for word in titleq:
		word=word.strip()
		#stemmedword=porter_stemmer.stem(word)
		#####
	      	querywords.append(word)
	

	
	for word in querywords:
		#f.seek(0,0)
		flag=0
		high=len(seclst)
		low=0
		mid=(high+low)/2
		s=seclst[mid]
		while low<=high:
			if s.split(':')[0]==word:
		
				flag=1
				bytes=int(s.split(':')[1].replace('\n',''))
				f2.seek(bytes,0)
				ch=f2.readline()
				
				ch=re.findall( r'\"t\":\[(.*?)\]', ch,re.MULTILINE)
				
				
				ch2=[]
				if len(ch)>0:
					ch2=re.findall( r'[0-9]{1,}', ch[0],re.DOTALL)
				
				ch=ch2
				
				search2(ch)
				break
			elif s.split(':')[0]<word:
				low=mid+1
				mid=low + (high-low)/2
			#print 'hii1',seclst[mid]
			else:
				high=mid-1
				mid=low + (high-low)/2
			#print 'hii2',seclst[mid]
			s=seclst[mid]
		if flag==0:
			for s in seclst:
				if s.split(':')[0]==word:
					bytes=int(s.split(':')[1].replace('\n',''))
					f2.seek(bytes,0)
					ch=f2.readline()
				
					ch=re.findall( r'\"t\":\[(.*?)\]', ch,re.DOTALL)
					ch2=[]
					if len(ch)>0:
						ch2=re.findall( r'[0-9]{1,}', ch[0],re.DOTALL)
					ch=ch2
					
					search2(ch)
					break
		
def body(bodyq,seclst):
	
	#qw=titleq.split()
	querywords=[]
	for word in bodyq:
		word=word.strip()
		stemmedword=porter_stemmer.stem(word)
		if word.isalpha() :#####
	      		querywords.append(stemmedword)
	

	for word in querywords:
		#f.seek(0,0)
		flag=0
		high=len(seclst)
		low=0
		mid=(high+low)/2
		s=seclst[mid]
		while low<=high:
			if s.split(':')[0]==word:
				flag=1
				bytes=int(s.split(':')[1].replace('\n',''))
				f2.seek(bytes,0)
				ch=f2.readline()
				ch=re.findall( r'\"b\":\[(.*?)\]', ch,re.DOTALL)
				ch2=[]
				if len(ch)>0:
					ch2=re.findall( r'[0-9]{1,}', ch[0],re.DOTALL)
				ch=ch2
				search2(ch)
				break
			elif s.split(':')[0]<word:
				low=mid+1
				mid=low + (high-low)/2
			#print 'hii1',seclst[mid]
			else:
				high=mid-1
				mid=low + (high-low)/2
			#print 'hii2',seclst[mid]
			s=seclst[mid]
		if flag==0:
			for s in seclst:
				if s.split(':')[0]==word:
					bytes=int(s.split(':')[1].replace('\n',''))
					f2.seek(bytes,0)
					ch=f2.readline()
					ch=re.findall( r'\"b\":\[(.*?)\]', ch,re.DOTALL)
					ch2=[]
					if len(ch)>0:
						ch2=re.findall( r'[0-9]{1,}', ch[0],re.DOTALL)
					ch=ch2
					search2(ch)
					break	
	

def cat(catq,seclst):
	
	#qw=titleq.split()
	querywords=[]
	for word in catq:
		word=word.strip()
		stemmedword=porter_stemmer.stem(word)
		if word.isalpha() :#####
	      		querywords.append(stemmedword)
	


	for word in querywords:
		#f.seek(0,0)
		flag=0
		high=len(seclst)
		low=0
		mid=(high+low)/2
		s=seclst[mid]
		while low<=high:
			if s.split(':')[0]==word:
				flag=1
				bytes=int(s.split(':')[1].replace('\n',''))
				f2.seek(bytes,0)
				ch=f2.readline()
				ch=re.findall( r'\"c\":\[(.*?)\]', ch,re.DOTALL)
				ch2=[]
				if len(ch)>0:
					ch2=re.findall( r'[0-9]{1,}', ch[0],re.DOTALL)
				ch=ch2
				search2(ch)
				break
			elif s.split(':')[0]<word:
				low=mid+1
				mid=low + (high-low)/2
			#print 'hii1',seclst[mid]
			else:
				high=mid-1
				mid=low + (high-low)/2
			#print 'hii2',seclst[mid]
			s=seclst[mid]
		if flag==0:
			for s in seclst:
				if s.split(':')[0]==word:
					bytes=int(s.split(':')[1].replace('\n',''))
					f2.seek(bytes,0)
					ch=f2.readline()
					ch=re.findall( r'\"c\":\[(.*?)\]', ch,re.DOTALL)
					ch2=[]
					if len(ch)>0:
						ch2=re.findall( r'[0-9]{1,}', ch[0],re.DOTALL)
					ch=ch2
					search2(ch)
					break

def ext(extq,seclst):
	
	#qw=titleq.split()
	querywords=[]
	for word in extq:
		word=word.strip()
		stemmedword=porter_stemmer.stem(word)
		if word.isalpha() :#####
	      		querywords.append(stemmedword)
	

	for word in querywords:
		#f.seek(0,0)
		flag=0
		high=len(seclst)
		low=0
		mid=(high+low)/2
		s=seclst[mid]
		while low<=high:
			if s.split(':')[0]==word:
				flag=1
				bytes=int(s.split(':')[1].replace('\n',''))
				f2.seek(bytes,0)
				ch=f2.readline()
				ch=re.findall( r'\"e\":\[(.*?)\]', ch,re.DOTALL)
				ch2=[]
				if len(ch)>0:
					ch2=re.findall( r'[0-9]{1,}', ch[0],re.DOTALL)
				ch=ch2
				search2(ch)
				break
			elif s.split(':')[0]<word:
				low=mid+1
				mid=low + (high-low)/2
			#print 'hii1',seclst[mid]
			else:
				high=mid-1
				mid=low + (high-low)/2
			#print 'hii2',seclst[mid]
			s=seclst[mid]
		if flag==0:
			for s in seclst:
				if s.split(':')[0]==word:
					bytes=int(s.split(':')[1].replace('\n',''))
					f2.seek(bytes,0)
					ch=f2.readline()
					ch=re.findall( r'\"e\":\[(.*?)\]', ch,re.DOTALL)
					ch2=[]
					if len(ch)>0:
						ch2=re.findall( r'[0-9]{1,}', ch[0],re.DOTALL)
					ch=ch2
					search2(ch)
					break
	
def ref(refq,seclst):
	
	#qw=titleq.split()
	querywords=[]
	for word in refq:
		word=word.strip()
		stemmedword=porter_stemmer.stem(word)
		if word.isalpha() :#####
	      		querywords.append(stemmedword)
	

	for word in querywords:
		#f.seek(0,0)
		flag=0
		high=len(seclst)
		low=0
		mid=(high+low)/2
		s=seclst[mid]
		while low<=high:
			if s.split(':')[0]==word:
				flag=1
				bytes=int(s.split(':')[1].replace('\n',''))
				f2.seek(bytes,0)
				ch=f2.readline()
				ch=re.findall( r'\"r\":\[(.*?)\]', ch,re.DOTALL)
				ch2=[]
				if len(ch)>0:
					ch2=re.findall( r'[0-9]{1,}', ch[0],re.DOTALL)
				ch=ch2
				search2(ch)
				break
			elif s.split(':')[0]<word:
				low=mid+1
				mid=low + (high-low)/2
			#print 'hii1',seclst[mid]
			else:
				high=mid-1
				mid=low + (high-low)/2
			#print 'hii2',seclst[mid]
			s=seclst[mid]
		if flag==0:
			for s in seclst:
				if s.split(':')[0]==word:
					bytes=int(s.split(':')[1].replace('\n',''))
					f2.seek(bytes,0)
					ch=f2.readline()
					ch=re.findall( r'\"r\":\[(.*?)\]', ch,re.DOTALL)
					ch2=[]
					if len(ch)>0:
						ch2=re.findall( r'[0-9]{1,}', ch[0],re.DOTALL)
					ch=ch2
					search2(ch)
					break
	

def info(infoq,seclst):
	
	#qw=titleq.split()
	querywords=[]
	for word in infoq:
		word=word.strip()
		stemmedword=porter_stemmer.stem(word)
		if word.isalpha() :#####
	      		querywords.append(stemmedword)
	

	for word in querywords:
		#f.seek(0,0)
		flag=0
		high=len(seclst)
		low=0
		mid=(high+low)/2
		s=seclst[mid]
		while low<=high:
			if s.split(':')[0]==word:
				flag=1
				bytes=int(s.split(':')[1].replace('\n',''))
				f2.seek(bytes,0)
				ch=f2.readline()
				ch=re.findall( r'\"i\":\[(.*?)\]', ch,re.DOTALL)
				ch2=[]
				if len(ch)>0:
					ch2=re.findall( r'[0-9]{1,}', ch[0],re.DOTALL)
				ch=ch2
				search2(ch)
				break
			elif s.split(':')[0]<word:
				low=mid+1
				mid=low + (high-low)/2
			#print 'hii1',seclst[mid]
			else:
				high=mid-1
				mid=low + (high-low)/2
			#print 'hii2',seclst[mid]
			s=seclst[mid]
		if flag==0:
			for s in seclst:
				if s.split(':')[0]==word:
					bytes=int(s.split(':')[1].replace('\n',''))
					f2.seek(bytes,0)
					ch=f2.readline()
					ch=re.findall( r'\"i\":\[(.*?)\]', ch,re.DOTALL)
					ch2=[]
					if len(ch)>0:
						ch2=re.findall( r'[0-9]{1,}', ch[0],re.DOTALL)
					ch=ch2
					search2(ch)
					break
	
def field(query,seclst):
	queryfields=query.split(':')
	mainlist=[]
	for word in queryfields:
		lst=word.split()
		for w in lst:
			mainlist.append(w)
		lst=[]
	for i in range(0,len(mainlist)):
		if mainlist[i]=='t':
			titleq=[]
			i+=1
			while i<len(mainlist) and mainlist[i]!='b' and mainlist[i]!='e' and mainlist[i]!='c' and mainlist[i]!='i' and mainlist[i]!='r':
				titleq.append(mainlist[i])
				i+=1
			
			title(titleq,seclst)
		elif mainlist[i]=='b':
			bodyq=[]
			i+=1
			while i<len(mainlist) and mainlist[i]!='t' and mainlist[i]!='e' and mainlist[i]!='c' and mainlist[i]!='i' and mainlist[i]!='r':
				bodyq.append(mainlist[i])
				i+=1
			body(bodyq,seclst)
		elif mainlist[i]=='i':
			infoq=[]
			i+=1
			while i<len(mainlist) and mainlist[i]!='b' and mainlist[i]!='e' and mainlist[i]!='c' and mainlist[i]!='t' and mainlist[i]!='r':
				infoq.append(mainlist[i])
				i+=1
			info(infoq,seclst)
		elif mainlist[i]=='r':
			refq=[]
			i+=1
			while i<len(mainlist) and mainlist[i]!='b' and mainlist[i]!='e' and mainlist[i]!='c' and mainlist[i]!='i' and mainlist[i]!='t':
				refq.append(mainlist[i])
				i+=1
			ref(refq,seclst)
		elif mainlist[i]=='e':
			extq=[]
			i+=1
			while i<len(mainlist) and mainlist[i]!='b' and mainlist[i]!='r' and mainlist[i]!='c' and mainlist[i]!='i' and mainlist[i]!='t':
				extq.append(mainlist[i])
				i+=1
			ext(extq,seclst)
		elif mainlist[i]=='c':
			catq=[]
			i+=1
			while i<len(mainlist) and mainlist[i]!='b' and mainlist[i]!='e' and mainlist[i]!='r' and mainlist[i]!='i' and mainlist[i]!='t':
				catq.append(mainlist[i])
				i+=1
			cat(catq,seclst)	
while 1:
	porter_stemmer=PorterStemmer()
	#global result
	result={}
	result=defaultdict(lambda:[0,0],result)
	
	query=input()
	query=query.lower()
#	print query
	#query=re.sub("[~`!@#$%-^*+{\[}\]\|\\<>/?]",' ',query,10000000,re.DOTALL)
#	print query
	if ':' in query:
		query=re.sub("[~`!@#$%-^*+{\[}\]\|\\<>/?]",' ',query,10000000,re.DOTALL)
		
		field(query,seclst)
		lst= sorted(result.items(),key=itemgetter(1),reverse=True)[:10]
		for i in lst:
			print docs[int(i[0])-2]
		
		f2.close()
	else:
		query=re.sub("[~`!@#$%-^*+{\[}\]\|\\<>/?]",' ',query,10000000,re.DOTALL)		
		qw=query.split()
		
		querywords=[]
		p='.,;/\"\'_)('
		PUNCTUATION='[~`!@#$%-^*+{\[}\]\|\\<>/?]'
		stopwords=['this','that','about','their', 'them', 'there','cite', 'these','then','such','because','between','cannot','from','each','have','having','will','shall','here','more','other','should','same',
		'those','very','whom','with','where','what','whose','when','which','your','while','link','wikitext','beyond','rather','both','like','likes','just','some','respect','name','know']
		for word in qw:
			word=word.strip()
			stemmedword=porter_stemmer.stem(word)
			if word.isalpha() and len(word)>2 and word not in stopwords:#####
		      		querywords.append(stemmedword)
		
		print querywords
		n=5311##########################################################################################
		#results=defaultdict(dict)
		
		
		for word in querywords:
			search(seclst)
			
			
		lst= sorted(result.items(),key=itemgetter(1),reverse=True)[:10]
	
		for i in lst:
			print docs[int(i[0])-2]

f2.close()
