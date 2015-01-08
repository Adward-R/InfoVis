def main():
	json = [
		{
			"name":"pok",
			"articles":[]
		},
		{
			"name":"abila",
			"articles":[]
		},
		{
			"name":"gastech",
			"articles":[]
		},
		{
			"name":"elodis",
			"articles":[]
		},
		{
			"name":"kronos",
			"articles":[]
		},
		{
			"name":"tethys",
			"articles":[]
		},
		{
			"name":"karen",
			"articles":[]
		},
		{
			"name":"elian",
			"articles":[]
		},
		{
			"name":"sanjorge",
			"articles":[]
		},
		{
			"name":"use",
			"articles":[]
		},
		{
			"name":"ceo",
			"articles":[]
		},
		{
			"name":"government",
			"articles":[]
		},
		{
			"name":"died",
			"articles":[]
		},
		{
			"name":"sten",
			"articles":[]
		},
		{
			"name":"drug",
			"articles":[]
		},
		{
			"name":"vann",
			"articles":[]
		}
	]
	hotwords = ("pok","abila","gastech","elodis","kronos","tethys","karen","elian","sanjorge","use","ceo","government","died","sten","drug","vann")
	ftime = open('/Users/Adward/Github/InfoVis/Data Processing/Report/articleTime.csv')
	time = []
	cnt = 0
	for line in ftime:
		if cnt!=0:
			time.append(line.split(',')[1])
		cnt += 1

	for i in range(len(time)):
		if time[i][0:4]=='2014':
			fr = open('/Users/Adward/Github/InfoVis/MC1 Data/MC1 Data/articles/'+str(i)+'.txt','r')
			for line in fr:
				line= line.replace('"',' ')
				line= line.replace("'",' ')
				line= line.replace(',',' ')
				line= line.replace('.',' ')
				line= line.replace(':',' ')
				line= line.replace(';',' ')
				line= line.replace('=',' ')
				line= line.replace('?',' ')	
				line= line.replace('~',' ')
				line= line.replace('`',' ')
				line= line.replace('_',' ')
				line= line.replace('+',' ')
				line= line.replace('-',' ')
				line= line.replace('*',' ')
				line= line.replace('@',' ')
				line= line.replace('$',' ')
				line= line.replace('#',' ')
				line= line.replace('%',' ')
				line= line.replace('^',' ')
				line= line.replace('&',' ')
				line= line.replace('|',' ')
				line= line.replace('!',' ')
				line= line.replace('/',' ')
				line= line.replace('\\',' ')
				line= line.replace('(',' ')
				line= line.replace(')',' ')
				line= line.replace(']',' ')
				line= line.replace('[',' ')
				line= line.replace('}',' ')
				line= line.replace('{',' ')
				line= line.replace('<',' ')
				line= line.replace('>',' ')
				line= line.replace('0',' ')
				line= line.replace('1',' ')
				line= line.replace('2',' ')
				line= line.replace('3',' ')
				line= line.replace('4',' ')
				line= line.replace('5',' ')
				line= line.replace('6',' ')
				line= line.replace('7',' ')
				line= line.replace('8',' ')
				line= line.replace('9',' ')
				line= line.split()
				for word in line:
					if word.lower() in hotwords:
						for itm in json:
							if itm["name"]==word.lower():
								flag = 0
								for date in itm["articles"]:
									if int(time[i][6:])==date[0]:
										date[1] += 1
										flag += 1
										break
								if flag==0:
									itm["articles"].append([int(time[i][6:]),1])
								break
			fr.close()
	fw = open("test.json",'w')
	fw.write(str(json))
	fw.close()

	fr = open("test.json",'r')
	result = ""
	for line in fr:
		result += line+'\n'
	fr.close()
	fw = open("test.json",'w')
	fw.write(result.replace('\'','\"'))
	fw.close()

if __name__ == '__main__':
	main()