import os
import os.path
def dateConvert(date):
	fmonth = ""
	month = date[4:6]
	if "01"==month:
		fmonth = "-Jan-"
	elif "02"==month:
		fmonth = "-Feb-"
	elif "03"==month:
		fmonth = "-Mar-"
	elif "04"==month:
		fmonth = "-Apr-"
	elif "05"==month:
		fmonth = "-May-"
	elif "06"==month:
		fmonth = "-Jun-"
	elif "07"==month:
		fmonth = "-Jul-"
	elif "08"==month:
		fmonth = "-Aug-"
	elif "09"==month:
		fmonth = "-Sep-"
	elif "10"==month:
		fmonth = "-Oct-"
	elif "11"==month:
		fmonth = "-Nov-"
	elif "12"==month:
		fmonth = "-Dec-"
	return date[6:]+fmonth+date[2:4]

def deprecated():
	fr = open('../Pre-Processing/articleTime.csv','r')
	cnt = 0
	dict = {}
	for line in fr:
		if cnt!=0:
			date = line.split(',')[1]
			if date in dict:
				dict[date] += 1
			else:
				dict[date] = 1
		cnt += 1
	fr.close()
	fw = open('data.tsv','w')
	fw.write("date\tclose\n")
	dict = sorted(dict.iteritems(),key=lambda d:int(d[0]),reverse=True)
	#print dict
	for itm in dict:
#		print itm[0]
		if itm[0][0:4]!='2014':
			fw.write(dateConvert(itm[0])+'\t'+str(itm[1])+'\n')

def main():
	freDict = {}
	for parent,dirs,files in os.walk(r'../divideByDay/'):
		for d in dirs:
			path = os.path.join(parent,d)
			if str(parent)=='../divideByDay/ByYear' or str(d)=='ByYear':
				continue
			freDict[str(d)] = 0
			for _parent,_dirs,_files in os.walk(path):
				for f in _files:
					freDict[str(d)] += 1
	#print freDict
	freDict = sorted(freDict.iteritems(),key=lambda d:int(d[0]),reverse=True)
	fw = open('data.tsv','w')
	fw.write("date\tclose\n")
	for itm in freDict:
		fw.write(dateConvert(itm[0])+'\t'+str(itm[1])+'\n')

if __name__=='__main__':
	main()