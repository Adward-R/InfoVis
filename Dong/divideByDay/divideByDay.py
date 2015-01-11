import os
import os.path
import shutil
def main():
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
	for i in hasTheWord:
		if not os.path.exists(str(articleTime[i])):
			os.mkdir(str(articleTime[i]))
		shutil.copy('../../MC1 Data/articles/'+str(i)+'.txt',str(articleTime[i])+'/'+str(i)+'.txt')

if __name__=='__main__':
	main()