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
start=time.clock()
l=[]
tokens=[]                          
d={}
ref=[]
et=[]
cat=[]
#stopwords = [
#        'a', 'an', 'and', 'are', 'as', 'about','at', 'be', 'but', 'by',
 #       'for', 'if', 'in', 'into', 'is', 'it',
  #      'no', 'not', 'of', 'on', 'or', 's', 'such',
   #     't', 'that', 'the', 'their', 'then', 'there', 'these',
    #    'they', 'this', 'to', 'was', 'will', 'with'
    #]
stopwords=['this','that','about','their', 'them', 'there','cite', 'these','then','such','because','between','cannot','from','each','have','having','will','shall','here','more','other','should','same',
'those','very','whom','with','where','what','whose','when','which','your','while','link','wikitext','beyond','rather','both','like','likes','just','some','respect','name','know']


	
#PUNCTUATION = re.compile('[~`!@#$%-^&*()+={\[}\]|\\:;"\',<.>/?]')
porter_stemmer=PorterStemmer()
d=defaultdict(dict)

p='.,;/\"\'_)('
PUNCTUATION='[~`!@#$%-^*+{\[}\]\|\\<>/?]'

	


def create(docid,word,c):
	global d,w,flag
	
	if c in d[word]:
		#print 'before',time.clock()
		if docid in d[word][c]:
			#print 'after',time.clock()
			d[word][c][docid]=d[word][c][docid]+1
		else:
			#print 'after',time.clock()
			d[word][c].update({docid:1})
		
	else:
		d[word].update({c:{docid:1}})
	#else:
	#	d[word]={c:{docid:1}}
	#	w=w+1
	

class ABC(xml.sax.ContentHandler):
	def __init__(self):
            self.text=0
	    self.doc_id=1
	    self.title=0
	    self.redirect=0
	    self.ch=''
	    self.flag=0
	    self.tit=''
	
	def startElement(self,name,attrs):
            if name=="text":
                    self.text=1
		    self.ch=''
	    if name=="title":
                    self.title=1
		    self.flag=1
		    self.ch=''
	    if name=="redirect":
                    self.redirect=1
	    if name=="page":
                    self.doc_id=self.doc_id+1
	    if name=="id" and self.flag==1:
                     self.ch='' 
		    
		   
        def endElement(self,name):
            if name=="text":
                    self.text=0
		    character(self.ch,0,1,self.doc_id)
		    self.ch=''
	    if name=="title":
                    self.title=0
		    character(self.ch,1,0,self.doc_id)
		    self.tit=self.ch
		    self.ch=''
		    
	    if name=="redirect":
                    self.redirect=0
	    if name=="id" and self.flag==1:
		     try:
                     	docc.write(str(self.doc_id)+':'+self.tit+':'+self.ch+'\n') 
		     except:
			docc.write(str(self.doc_id)+':'+(self.tit).encode('utf-8')+':'+(self.ch).encode('utf-8')+'\n')
		     self.ch=''
		     self.flag=0
        def characters(self,content):
	    self.ch=self.ch+content
	    
			
	            #print cat
def character(ch,title,text,doc_id):
	
	global d,l,flag
	flag=0
	    
	#print d
	e=len(ch)
	
	ch=ch.lower()

	ch2=[]
	#print 'b4',time.clock()
	#if doc_id==3:
	#ch=re.sub(r'{{(.*?)}}','',ch,flags=re.DOTALL)
	ch = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', ch, 10000,re.DOTALL)
	ch = re.sub( '{\|(.*?)\|}','', ch, 10000,re.DOTALL)
	ch=re.sub(r'\[\[file:(.*?)\]\]','',ch,10000,re.DOTALL)
	ch=re.sub(r'{{v?cite(.*?)}}','',ch,10000,re.DOTALL)
	ch=re.sub(r'<(.*?)>','',ch,10000,re.DOTALL)
	#ch = re.sub( '<!--(.*?)-->', '',ch, re.DOTALL)
	#print 'after',time.clock()
	ch=re.sub(r'[.,;_()"/\']',' ',ch,10000000,re.DOTALL)
	#print ch
	#print d
        if title==1:
		for word in ch.split():
			word=re.sub("[~`!@#$%-^*+{\[}\]\|\\<>/?]",' ',word)
			if word.isalpha():
				create(doc_id,word,'t')
	    
			
        if text==1:
		    
	        tokens=[]
		ref=[]
		#body=''
		et=[]
		cat=[]
		info=[]
		etindex=0
		refindex=0
		catindex=e
		cat=re.findall(r'\[\[category:(.*?)\]\]',ch,flags=re.MULTILINE)
		info=re.findall ( '{{infobox(.*?)}}', ch,re.DOTALL)
		ch=re.sub( '{{infobox(.*?)}}','', ch, 10000,re.DOTALL)
		try:
			etindex=ch.index('=external links=')+20
		except:
			pass
		try:
			catindex=ch.index('[[category:')+20
		except:
			pass
		if etindex:
			et=ch[etindex:catindex]
			et=re.findall(r'\[(.*?)\]',et,flags=re.MULTILINE)
		ref=re.findall(r'== ?references ?==(.*?)==',ch,flags=re.DOTALL)
		ch=re.sub(r'== ?references ?==(.*?)==','',ch,flags=re.DOTALL)
		ch=re.sub(r'{{(.*?)}}','',ch,1000000,re.DOTALL)
			#ch[i]=''
		et=list(et)
		##############################################################################################
		#print ref
		    #ch=ch.lower()
		#reference(ch)   
		#externallink(ch)
		#category(ch)
		#ch=re.sub(r'\[\[Category:(.*?)\]\]','',ch,flags=re.MULTILINE)
		#ch=re.sub(r'<(.*?)>','',ch,flags=re.MULTILINE)
		#ch=ch.replace(ch[e:len(ch)],'')
                   # ch=PUNCTUATION.sub(' ',ch)
		    #ch=ch.translate(p,'        ')
	        #externallink(ch)
		    #ch=ch.replace('==External links==','')
		#ch=ch.replace('==References==','')
		    #ch=ch.replace('[[Category','')
		############################################################################################
		#finding external links
		if etindex:
			ch=ch[0:etindex]
		ch=re.sub("[~`!@#$%-^*+{\[}\]\|\\<>/?]",' ',ch,10000000,re.DOTALL)
		    #ch=ch.lower()
		ch2=ch.split()
		for token in ch2:
     			token=token.strip()
			if token.isalpha() and len(token)>3 and token not in stopwords:

				#print 'accept',token
				tokens.append(token)
			
		    #stemmed=[]
		for token in tokens:
			stemmedword=porter_stemmer.stem(token)
      			l.append(stemmedword)
		for word in l:
			create(doc_id,word,'b')
		l=[]
		    #print et	
		for token in et:
			#print 'et=',token
			
			
		    	token=re.sub("[~`!@#$%-^*+{\[}\]\|\\<>/?]",' ',token,100,re.DOTALL)
			for j in token.split():
				j=j.strip()
				
				if j.isalpha() and len(j)>3 and j not in stopwords:
					stemmedword=porter_stemmer.stem(j)
		      			l.append(stemmedword)
					#print 'accept',j
				
		    #k=list(set(tokens)-set(l))
		for word in l:
		
			create(doc_id,word,'e')
		     
		    
		l=[]
		for token in cat:
			
			
		    	token=re.sub("[~`!@#$%-^*+{\[}\]\|\\<>/?]",' ',token,100,re.DOTALL)
			for j in token.split():
				j=j.strip()
				
				if j.isalpha and len(j)>3 and j not in stopwords:
					stemmedword=porter_stemmer.stem(j)
	      				l.append(stemmedword)
					#print 'accept',j
				
		for word in l:
			#print word
			create(doc_id,word,'c')
		     
		    
		l=[]
		for token in ref:
			
			
		    	token=re.sub("[~`!@#$%-^*+{\[}\]\|\\<>/?]",' ',token,100,re.DOTALL)
			for j in token.split():
				j=j.strip()
				
				if j!='reflist' and j.isalpha and len(j)>3 and j not in stopwords:
					stemmedword=porter_stemmer.stem(j)
	      				l.append(stemmedword)
					#print 'accept',j
				
		for word in l:
			#print word
			create(doc_id,word,'r')
		l=[]
		
		for token in info:
			s=[]
			s=re.findall(r'=(.*?)\|',token,re.DOTALL)
			for k in s:
				k=re.sub("[~`!@#$%-^*+{\[}\]\|\\<>/?]",' ',k,100,re.DOTALL)
				for j in k.split():
					
					j=j.strip()
					if j.isalpha and len(j)>3 and j not in stopwords:
						stemmedword=porter_stemmer.stem(j)
	      					l.append(stemmedword)
		for word in l:
			#print word
			create(doc_id,word,'i')		
		l=[]
		#print '*******************************'
		
		#print d
		if doc_id%100==0:
			f=open(str(doc_id),'a')
			for word in sorted(d.keys()):
				f.write(json.dumps(word,separators=(',',':'))+':')
				if 'b' in d[word]:
					#f.write('\"b\"'+':'+json.dumps(d[word]['b'],separators=(',',':')))
					f.write('\"b\"'+':'+ str(sorted(d[word]['b'].items(),key=itemgetter(1),reverse=True)[:500]).replace('(','').replace(')','').replace(' ',''))
				if 'c' in d[word]:
					#f.write('\"c\"'+':'+json.dumps(d[word]['c'],separators=(',',':')))
					f.write('\"c\"'+':'+ str(sorted(d[word]['c'].items(),key=itemgetter(1),reverse=True)[:500]).replace('(','').replace(')','').replace(' ',''))
				if 'e' in d[word]:
					#f.write('\"e\"'+':'+json.dumps(d[word]['e'],separators=(',',':')))
					f.write('\"e\"'+':'+ str(sorted(d[word]['e'].items(),key=itemgetter(1),reverse=True)[:500]).replace('(','').replace(')','').replace(' ',''))
				if 'i' in d[word]:
					#f.write('\"i\"'+':'+json.dumps(d[word]['i'],separators=(',',':')))
					f.write('\"i\"'+':'+ str(sorted(d[word]['i'].items(),key=itemgetter(1),reverse=True)[:500]).replace('(','').replace(')','').replace(' ',''))
				if 'r' in d[word]:
					#f.write('\"c\"'+':'+json.dumps(d[word]['r'],separators=(',',':')))
					f.write('\"r\"'+':'+ str(sorted(d[word]['r'].items(),key=itemgetter(1),reverse=True)[:500]).replace('(','').replace(')','').replace(' ',''))
				if 't' in d[word]:
					#f.write('\"t\"'+':'+json.dumps(d[word]['t'],separators=(',',':')))
					f.write('\"t\"'+':'+ str(sorted(d[word]['t'].items(),key=itemgetter(1),reverse=True)[:500]).replace('(','').replace(')','').replace(' ',''))
				f.write('\n')
				#f.write(json.dumps(word,separators=(',',':'))+':'+json.dumps(d[word],separators=(',',':'))+'\n')
			f.close()
			d=defaultdict(dict)
docc=open('docindex','a')		
parser=xml.sax.make_parser()
#parser.setFeature(xml.sax.handler.feature_namespaces, 0)
parser.setContentHandler(ABC())
#try:
parser.parse(open('test_dump.xml',"r"))

#j=''
#j=json.dumps(d,separators=(',',':'))
#f=open(sys.argv[2],'w')
#f.write(j)
#f.close()

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


