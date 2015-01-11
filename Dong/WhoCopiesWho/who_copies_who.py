import os
def main():
	matrix = []
	for i in range(32):
		tmp = []
		for j in range(32):
			tmp.append(0)
		matrix.append(tmp)
	
	#print matrix

	numCopied = {  #copied and copying others 's times
		"News Only Today":[0,0,0],
		"Homeland Illumination":[0,0,1],
		"Kronos Star":[0,0,2],
		"The Abila Post":[0,0,3],
		"Centrum Sentinel":[0,0,4],
		"Tethys News":[0,0,5],
		"Modern Rubicon":[0,0,6],
		"Worldwise":[0,0,7],
		"The Truth":[0,0,8],
		"The Guide":[0,0,9],
		"Daily Pegasus":[0,0,10],
		"The Orb":[0,0,11],
		"The Wrap":[0,0,12],
		"Athena Speaks":[0,0,13],
		"The Explainer":[0,0,14],
		"News Desk":[0,0,15],
		"Central Bulletin":[0,0,16],
		"International News":[0,0,17],
		"The Tulip":[0,0,18],
		"The Light of Truth":[0,0,19],
		"The General Post":[0,0,20],
		"All News Today":[0,0,21],
		"The World":[0,0,22],
		"Who What News":[0,0,23],
		"The Continent":[0,0,24],
		"Everyday News":[0,0,25],
		"World Journal":[0,0,26],
		"International Times":[0,0,27],
		"News Online Today":[0,0,28],
		"World Source":[0,0,29]}
	
	fr = open('..//Pre-Processing/articleTime.csv','r')
	#print matrix
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

	#print needNotToProcess
	#return
	#toBeDeleted = []
	for i in range(845):
		if i in needNotToProcess:
			continue
		for j in range(i+1,845):
			if j in needNotToProcess:
				continue
			#if (j in toBeDeleted) or (i in toBeDeleted):
			#	continue
			fr1 = open('../../MC1 Data/articles/'+str(i)+'.txt','r')
			fr2 = open('../../MC1 Data/articles/'+str(j)+'.txt','r')
			cntLine1 = 0
			cntLine2 = 0
			vect = {}
			for line in fr1:
				cntLine1 += 1
				tmpline = line.replace('"',' ').replace("'",' ').replace('-',' ').replace(',',' ').replace('.',' ').replace('(',' ').replace(')',' ').replace('<',' ').replace('>',' ').replace('\n',' ').replace('\t',' ')
				for word in tmpline.split():
					if vect.has_key(word):
						vect[word][0] += 1
					else:
						vect[word] = [1,0]
			for line in fr2:
				cntLine2 += 1
				tmpline = line.replace('"',' ').replace("'",' ').replace('-',' ').replace(',',' ').replace('.',' ').replace('(',' ').replace(')',' ').replace('<',' ').replace('>',' ').replace('\n',' ').replace('\t',' ')
				for word in tmpline.split():
					if vect.has_key(word):
						vect[word][1] += 1
					else:
						vect[word] = [0,1]
			fr1.close()
			fr2.close()
			length1 = 0
			length2 = 0
			innerProduct = 0
			for key in vect.keys():
				innerProduct += vect[key][0] * vect[key][1]
				length1 += vect[key][0] * vect[key][0]
				length2 += vect[key][1] * vect[key][1]
			simi = innerProduct*innerProduct*1.0 / (length1*length2)
			#print str(i)+' '+str(j)+' '+str(simi)
			if simi>0.7:
				matrix[numCopied[timeDict[i][1]][2]][numCopied[timeDict[j][1]][2]] += 1
				if timeDict[i][0]<timeDict[j][0]:
					numCopied[timeDict[j][1]][0] += 1
					numCopied[timeDict[i][1]][1] += 1
				elif timeDict[j][0]<timeDict[i][0]:
					numCopied[timeDict[i][1]][0] += 1
					numCopied[timeDict[j][1]][1] += 1
				else:
					if cntLine1>cntLine2:
						numCopied[timeDict[i][1]][0] += 1
						numCopied[timeDict[j][1]][1] += 1
					else:
						numCopied[timeDict[j][1]][0] += 1
						numCopied[timeDict[i][1]][1] += 1	
	
	#numCopied = sorted(numCopied.iteritems(),key=lambda d:((d[1][1]+0.1)*1.0/(d[1][0]+0.1)),reverse=True)
	#print numCopied
	#ff = open('copied_times.txt','w')
	#ff.write(str(numCopied)+'\n\n'+str(matrix))
	#ff.close()
	numCopied = sorted(numCopied.iteritems(),key=lambda d:(d[1][2]),reverse=False)
	json = {"nodes":[],"links":[]}
	for paper in numCopied:
		json["nodes"].append({"name":paper[0],"size":((paper[1][1]+0.1)*1.0/(paper[1][0]+0.1))})
	for i in range(32):
		for j in range(32):
			if matrix[i][j]>0:
				json["links"].append({"source":i,"target":j,"value":matrix[i][j]})
	fjson = open('copy.json','w')
	fjson.write(str(json).replace("'",'"'))

if __name__ == '__main__':
	main()
