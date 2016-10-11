#!/usr/bin/python
import xml.sax
import nltk,sys,time
from nltk.stem import PorterStemmer
from collections import defaultdict
from operator import itemgetter
#nltk.download('corpus')
#from nltk.corpus import wordnet
import re
import json
from heapq import heapify, heappush, heappop
start=time.clock()



def merge(alist):
	global flag
	while len(alist)>0:
		
	
		s2=''
		
		
		(s2,w3)=heappop(alist)#smallest
		
		heapify(alist)
		if len(s2)<=1:
			continue
		sb=''
		w2=open('buffer','r')
		s=w2.readline()
		w2.close()
		#print len(s)
		
		if len(s)<=1:
			w2=open('buffer','w')
			w2.write(s2)
			w2.close()
			
		else :
			#if s and s2 have same words but not same corresponding indexes
			if s!='' and s.split(':')[0].strip('"').strip("'")==s2.split(':')[0].strip('"').strip("'") and s!=s2 :	
				if s.split(':')[0].strip('"').strip("'").isalpha() or s.split(':')[0].strip('"').strip("'").isdigit():
					if "\"b\"" in s and "\"b\"" in s2:
						j1=s.index("\"b\"")
						j2=s2.index("\"b\"")
						for i in range(j1,len(s)):
							if s[i]==']':
								k1=i
								break
						for i in range(j2,len(s2)):
							if s2[i]=='[':
								k2=i
							if s2[i]==']':
								k3=i
								break
						#sb=s[j1:k1]+','+s2[k2+1:k3+1]
						s5=(s[j1:k1]+','+s2[k2+1:k3+1]).split(':')[1]
						token=[]
						token=s5.split(',')
						#token is of the form [1:5,2:2,3:1]
						print token
						exit()
						for i in range(0,len(token)):
							token[i]=token[i].replace('[','').replace(']','').strip('"').strip("'")
						d={}
						d=dict(zip(token[::2],token[1::2]))
						for k in d.keys():
							d[k]=int(d[k])
						sb="\"b\""+':'+str(sorted(d.items(),key=itemgetter(1),reverse=True)[:300]).replace('(','').replace(')','').replace(' ','')
				
					if "\"b\"" in s and "\"b\"" not in s2:
						j1=s.index("\"b\"")
						for i in range(j1,len(s)):
							if s[i]==']':
								k1=i
								break
						sb=sb+s[j1:k1+1]
			
					if "\"b\"" not in s and "\"b\""  in s2:
						j1=s2.index("\"b\"")
						for i in range(j1,len(s2)):
							if s2[i]==']':
								k1=i
								break
						sb=sb+s2[j1:k1+1]
				
					if "\"c\"" in s and "\"c\"" in s2:
						j1=s.index("\"c\"")
						j2=s2.index("\"c\"")
						for i in range(j1,len(s)):
							if s[i]==']':
								k1=i
								break
						for i in range(j2,len(s2)):
							if s2[i]=='[':
								k2=i
							if s2[i]==']':
								k3=i
								break
			
						#sb=sb+s[j1:k1]+','+s2[k2+1:k3+1]
						s5=(s[j1:k1]+','+s2[k2+1:k3+1]).split(':')[1]
						token=[]
						token=s5.split(',')
						for i in range(0,len(token)):
							token[i]=token[i].replace('[','').replace(']','').strip('"').strip("'")
						d={}
						d=dict(zip(token[::2],token[1::2]))
						for k in d.keys():
							d[k]=int(d[k])
						sb=sb+"\"c\""+':'+str(sorted(d.items(),key=itemgetter(1),reverse=True)[:300]).replace('(','').replace(')','').replace(' ','')
					#	print sb
				
					if "\"c\"" in s and "\"c\"" not in s2:
						j1=s.index("\"c\"")
						for i in range(j1,len(s)):
							if s[i]==']':
								k1=i
								break
						sb=sb+s[j1:k1+1]
				
					if "\"c\"" not in s and "\"c\""  in s2:
						j1=s2.index("\"c\"")
						for i in range(j1,len(s2)):
							if s2[i]==']':
								k1=i
								break
						sb=sb+s2[j1:k1+1]
				
				
					if "\"e\"" in s and "\"e\"" in s2:
						j1=s.index("\"e\"")
						j2=s2.index("\"e\"")
						for i in range(j1,len(s)):
							if s[i]==']':
								k1=i
								break
						for i in range(j2,len(s2)):
							if s2[i]=='[':
								k2=i
							if s2[i]==']':
								k3=i
								break
			
						#sb=sb+s[j1:k1]+','+s2[k2+1:k3+1]
						s5=(s[j1:k1]+','+s2[k2+1:k3+1]).split(':')[1]
						token=[]
						token=s5.split(',')
						for i in range(0,len(token)):
							token[i]=token[i].replace('[','').replace(']','').strip('"').strip("'")
						d={}
						d=dict(zip(token[::2],token[1::2]))
						for k in d.keys():
							d[k]=int(d[k])
						sb=sb+"\"e\""+':'+str(sorted(d.items(),key=itemgetter(1),reverse=True)[:300]).replace('(','').replace(')','').replace(' ','')
				
					if "\"e\"" in s and "\"e\"" not in s2:
						j1=s.index("\"e\"")
						for i in range(j1,len(s)):
							if s[i]==']':
								k1=i
								break
						sb=sb+s[j1:k1+1]
				
					if "\"e\"" not in s and "\"e\""  in s2:
						j1=s2.index("\"e\"")
						for i in range(j1,len(s2)):
							if s2[i]==']':
								k1=i
								break
						sb=sb+s2[j1:k1+1]
				
					if "\"i\"" in s and "\"i\"" in s2:
						j1=s.index("\"i\"")
						j2=s2.index("\"i\"")
						for i in range(j1,len(s)):
							if s[i]==']':
								k1=i
								break
						for i in range(j2,len(s2)):
							if s2[i]=='[':
								k2=i
							if s2[i]==']':
								k3=i
								break
			
						#sb=sb+s[j1:k1]+','+s2[k2+1:k3+1]
						s5=(s[j1:k1]+','+s2[k2+1:k3+1]).split(':')[1]
						token=[]
						token=s5.split(',')
						for i in range(0,len(token)):
							token[i]=token[i].replace('[','').replace(']','').strip('"').strip("'")
						d={}
						d=dict(zip(token[::2],token[1::2]))
						for k in d.keys():
							d[k]=int(d[k])
						sb=sb+"\"i\""+':'+str(sorted(d.items(),key=itemgetter(1),reverse=True)[:300]).replace('(','').replace(')','').replace(' ','')
						#print sb
				
					if "\"i\"" in s and "\"i\"" not in s2:
						j1=s.index("\"i\"")
						for i in range(j1,len(s)):
							if s[i]==']':
								k1=i
								break
						sb=sb+s[j1:k1+1]
				
					if "\"i\"" not in s and "\"i\""  in s2:
						j1=s2.index("\"i\"")
						for i in range(j1,len(s2)):
							if s2[i]==']':
								k1=i
								break
						sb=sb+s2[j1:k1+1]
							
					if "\"r\"" in s and "\"r\"" in s2:
						j1=s.index("\"r\"")
						j2=s2.index("\"r\"")
						for i in range(j1,len(s)):
							if s[i]==']':
								k1=i
								break
						for i in range(j2,len(s2)):
							if s2[i]=='[':
								k2=i
							if s2[i]==']':
								k3=i
								break
						#sb=sb+s[j1:k1]+','+s2[k2+1:k3+1]
			
						s5 =(s[j1:k1]+','+s2[k2+1:k3+1]).split(':')[1]
			
				
						token=[]
						token=s5.split(',')
						for i in range(0,len(token)):
							token[i]=token[i].replace('[','').replace(']','').strip('"').strip("'")
						d={}
						d=dict(zip(token[::2],token[1::2]))
						for k in d.keys():
							d[k]=int(d[k])
						sb=sb+"\"r\""+':'+str(sorted(d.items(),key=itemgetter(1),reverse=True)[:300]).replace('(','').replace(')','').replace(' ','')
						#print sb
				
					if "\"r\"" in s and "\"r\"" not in s2:
						j1=s.index("\"r\"")
						for i in range(j1,len(s)):
							if s[i]==']':
								k1=i
								break
						sb=sb+s[j1:k1+1]
				
					if "\"r\"" not in s and "\"r\""  in s2:
						j1=s2.index("\"r\"")
						for i in range(j1,len(s2)):
							if s2[i]==']':
								k1=i
								break
						sb=sb+s2[j1:k1+1]
				
					if "\"t\"" in s and "\"t\"" in s2:
						j1=s.index("\"t\"")
						j2=s2.index("\"t\"")
						for i in range(j1,len(s)):
							if s[i]==']':
								k1=i
								break
						for i in range(j2,len(s2)):
							if s2[i]=='[':
								k2=i
							if s2[i]==']':
								k3=i
								break
						#sb=sb+s[j1:k1]+','+s2[k2+1:k3+1]
						s5=(s[j1:k1]+','+s2[k2+1:k3+1]).split(':')[1]
						token=[]
						token=s5.split(',')
						for i in range(0,len(token)):
							token[i]=token[i].replace('[','').replace(']','').strip('"').strip("'")
						d={}
						d=dict(zip(token[::2],token[1::2]))
						for k in d.keys():
							d[k]=int(d[k])
						sb=sb+"\"t\""+':'+str(sorted(d.items(),key=itemgetter(1),reverse=True)[:300]).replace('(','').replace(')','').replace(' ','')
						#print sb
			
					if "\"t\"" in s and "\"t\"" not in s2:
						j1=s.index("\"t\"")
						for i in range(j1,len(s)):
							if s[i]==']':
								k1=i
								break
						sb=sb+s[j1:k1+1]
			
					if "\"t\"" not in s and "\"t\""  in s2:
						j1=s2.index("\"t\"")
						for i in range(j1,len(s2)):
							if s2[i]==']':
								k1=i
								break
						sb=sb+s2[j1:k1+1]
				
					sb=sb.replace('\n','')
					w2=open('buffer','w')
					w2.write(s.split(':')[0]+':'+sb)
					#print s.split(':')[0]+':'+sb
					w2.close()
			else:
				if s!=s2:				
					w2=open('buffer','r')
					w.seek(0,2)
					size=w.tell()
					
			
					w.write(w2.readline().replace('\n','').strip('"').strip("'")+'\n')
					w4.write(s.split(':')[0].strip('"').strip("'")+':'+str(size)+'\n')
					w2.close()
					w2=open('buffer','w')	
					w2.seek(0,0)
						
					w2.write(s2)
					w2.close()
		s3=w3.readline()
		
		heappush(alist,(s3,w3))
		#print alist
		#w2.close()
	w2=open('buffer','r')
	s3=w2.readline()
	w2.close()
	if s3!='':
		
		w.write(s3)

import glob
files=glob.glob('/home/tanushri/Documents/IRE/phase3/*')
print len(files)
l={}
alist=[]
for f in files:
	g=open(f,'r')
	s=g.readline()
	
				
	#if s.split(':')[0].strip('"').strip("'").isalpha() or s.split(':')[0].strip('"').strip("'").isdigit():
	#pushing into the heap the string and its corresponding file handler
	heappush(alist,(s,g))
	
w=open('indexfile1','a')
w4=open('secindex1','a')
#w2=open('buffer','r')

	#alist.append(word)	
flag=0
merge(alist)
w.close()
w4.close()
#w2.close()
print time.clock()-start
#with open('op4.txt','wb') as handle:
#	pickle.dump(d,handle) 
#mydict_as_string = cPickle.dumps(d)

#print w

#print ig
#print 'pickle=',sys.getsizeof(mydict_as_string)
exit()

	#handle stopwords
# 203805
#315.345862
#334.916309
#203792
#339.776227

