import os
import os.path
import shutil

stopwords = ("meet","illumination","thanks","little","caused","held","ends","work","way","care","city","gastech","pok","abila","elodis","kronos","end","time","pm","am","ii","january","ago","today","and","or","one","day","man","bring","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the","happen","chance","chances","people","like","good","bad","new","old","news","year","years",);

def dividing():
	fpok = open('../../MC1 Data/pok','r')
	ftime = open('../Pre-Processing/articleTime.csv','r')
	articleTime = []
	hasTheWord = []
	for line in fpok:
		hasTheWord.append(int(line.split(':')[0]))
	cnt = 0
	for line in ftime:
		if cnt!=0:
			articleTime.append(int(line.split(',')[1]))
		cnt += 1	

	#print hasTheWord
	for i in range(845):
		if not os.path.exists('./ByYear/'+str(articleTime[i])[0:4]):
			os.mkdir('./ByYear/'+str(articleTime[i])[0:4])
		shutil.copy('../../MC1 Data/articles/'+str(i)+'.txt','./ByYear/'+str(articleTime[i])[0:4]+'/'+str(i)+'.txt')

def statNames(): #by year before 2014 will be better(less redundant info)
	#stopwords = ('pok','meet','of','the','with','he','i','she','this')
	stat = open('./ByYear/statByYear.txt','w')
	#path = r'./'
	for parent,dirs,files in os.walk(r'./ByYear/'):
		for d in dirs: #each day
			namedict = {}
			path = os.path.join(parent,d)
			stat.write(path.strip('.').strip('./')+':\n')
			for _parent,_dirs,_files in os.walk(path):
				for f in _files:
					if str(f)=='.DS_Store':
						continue
					s = os.path.join(_parent,f)
					f = open(s,'r')
					for line in f:
						for word in line.replace('"',' ').replace("'",' ').replace('-',' ').replace('<',' ').replace(':',' ').replace(',',' ').replace('.',' ').replace('!',' ').replace('(',' ').replace(')',' ').replace('[',' ').replace(']',' ').split():
							if word.lower()!=word :
								key = word
								if key.lower() not in stopwords:
									if namedict.has_key(key):
										namedict[key] += 1
									else:
										namedict[key] = 1
				toBeDel = []
				for key in namedict.keys():
					if namedict[key]<=2 :
						toBeDel.append(key)
				for key in toBeDel:
					del(namedict[key])
				stat.write(str(namedict).replace("'",'"')+'\n')

def main():
	dividing()
	statNames()

if __name__=='__main__':
	main()