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
	return date[2:4]+fmonth+date[6:]

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
	fr = open('../Pre-Processing/articleTime.csv','r')
	timeDict = []
	needNotToProcess = []
	cnt = 0
	for line in fr:
		if cnt!=0:
			if line.split(',')[-1].strip('\n').strip(' ')=='':
				needNotToProcess.append(cnt-1)
			timeDict.append((int(line.split(',')[1]),line.split(',')[2].strip('\n').strip(' ')))
		cnt += 1
	fr.close()

	freDict = {}
	for parent,dirs,files in os.walk(r'../divideByDay/'):
		for d in dirs:
			path = os.path.join(parent,d)
			if str(parent)=='../divideByDay/ByYear' or str(d)=='ByYear':
				continue
			freDict[str(d)] = {  #copied and copying others 's times
				#"News Only Today":0,
				"Homeland Illumination":0,
				"Kronos Star":0,
				"The Abila Post":0,
				"Centrum Sentinel":0,
				#"Tethys News":0,
				#"Modern Rubicon":0,
				#"Worldwise":0,
				#"The Truth":0,
				#"The Guide":0,
				#"Daily Pegasus":0,
				#"The Orb":0,
				#"The Wrap":0,
				#"Athena Speaks":0,
				#"The Explainer":0,
				#"News Desk":0,
				#"Central Bulletin":0,
				#"International News":0,
				#"The Tulip":0,
				#"The Light of Truth":0,
				#"The General Post":0,
				#"All News Today":0,
				#"The World":0,
				#"Who What News":0,
				#"The Continent":0,
				#"Everyday News":0,
				#"World Journal":0,
				#"International Times":0,
				"News Online Today":0,
				"total":0}
				#"World Source":0}
			for _parent,_dirs,_files in os.walk(path):
				for f in _files:
					if freDict[str(d)].has_key(timeDict[int(str(f).strip('.txt'))][1]):
						freDict[str(d)]["total"] += 1
						freDict[str(d)][timeDict[int(str(f).strip('.txt'))][1]] += 1
#					freDict[str(d)] += 1
	#print freDict
	freDict = sorted(freDict.iteritems(),key=lambda d:int(d[0]),reverse=False)
	fw = open('muchdata.tsv','w')
	fw.write("date")
	for paper in freDict[0][1].keys():
		if paper=="total":
			continue
		fw.write("\t"+paper)
	for itm in freDict:
		fw.write('\n'+dateConvert(itm[0]))
		for paper in itm[1].keys():
			if paper=="total":
				continue
			if itm[1]["total"]==0:
				fw.write('\t'+str(0))
			else:
				fw.write('\t'+str(itm[1][paper]*100.0/itm[1]["total"]))
	#for itm in freDict:
	#	fw.write(dateConvert(itm[0])+'\t'+str(itm[1])+'\n')
	#print freDict
	#fw.write(str(freDict).replace("'",'"'))
	fw.close()

if __name__=='__main__':
	main()