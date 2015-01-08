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

def main():
	fr = open('articleTime.csv','r')
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
	fw = open('date.tsv','w')
	fw.write("date\tclose\n")
	for key in dict.keys():
		if key[0]=='2':
			fw.write(dateConvert(key)+'\t'+str(dict[key])+'\n')

if __name__=='__main__':
	main()