
#get sorted paper offices and the number of articles they have issued
def paperStat():
    title = {}
    fileWriter = open('paperStat.txt','w')
    path = "../../MC1 Data/MC1 Data/articles/"
    for i in range(0,845) :
        fileReader = open(path+str(i)+'.txt','r')
        for line in fileReader:
            if (line in title):
                title[line] += 1
            else:
                title[line] = 1
            #fileWriter.write(line+'\n')
            break
        fileReader.close();

    title = sorted(title.iteritems(),key=lambda d:d[1],reverse=True)
#    for paper in title.keys():
    for paper in title:
        fileWriter.write(paper[0].strip('\n').strip('\r') + '---' + str(paper[1]) +'\n')
    fileWriter.close();

#get time relevant reports that may correspond to the vanishing incident
def getArticleTime():
    num = []
    fileWriter = open('articleTime.csv','w')
    path = "../../MC1 Data/MC1 Data/articles/"
    for i in range(0,845):
        fileReader = open(path+str(i)+'.txt','r')
        org = ""
        for line in fileReader:
            org = line.strip('\n')
            break
        cnt = 0
        for line in fileReader:
            if (cnt==0):
                cnt+=1
                continue
            else:
                if (line.strip('\n').strip('\r').strip(' ')==''):
                    continue
                elif (cnt>=1):
                    if (line[0].isdigit()):
                        num.append([line.strip('\n').strip('\r'),i,org])
                        break
                    else:
                        continue
                else:
                    cnt+=1
        fileReader.close()

    time = []
    for item in num: #raw time data, doc num
        if (len(item[0].split('/'))==3):
            #filtering
            #if (int(item[0].split('/')[0])>=2014):
                time.append([item[0].split('/'),item[1],item[2]])
        else:
            tmp = item[0].split(' ')
            if (len(tmp)>=4):
                tmp = tmp[0:3]
            if (len(tmp)<=2):
                continue
            tmp.reverse();
            if ("January"==tmp[1]):
                tmp[1] = "01"
            elif ("February"==tmp[1]):
                tmp[1] = "02"
            elif ("March"==tmp[1]):
                tmp[1] = "03"
            elif ("April"==tmp[1]):
                tmp[1] = "04"
            elif ("May"==tmp[1]):
                tmp[1] = "05"
            elif ("June"==tmp[1]):
                tmp[1] = "06"
            elif ("July"==tmp[1]):
                tmp[1] = "07"
            elif ("August"==tmp[1]):
                tmp[1] = "08"
            elif ("September"==tmp[1]):
                tmp[1] = "09"
            elif ("October"==tmp[1]):
                tmp[1] = "10"
            elif ("November"==tmp[1]):
                tmp[1] = "11"
            elif ("December"==tmp[1]):
                tmp[1] = "12"
            else:
                tmp[1] = "00"
            try:
                if (int(tmp[2])<10):
                    tmp[2] = '0'+str(int(tmp[2]))
            except ValueError:
                print tmp
            #filter articles that may be relevant in time 
            try:
                #if (int(tmp[0])>=2014):
                    time.append([tmp,item[1],item[2]])
            except ValueError:
                print tmp
    
    fileWriter.write('num,time,paper\n')
    for item in time:
        fileWriter.write(str(item[1])+','+item[0][0]+item[0][1]+item[0][-1]+','+item[2]+'\n')
    fileWriter.close();

def makeWordFreCsv():
    timeReader = open('articleTime.csv','r')
    freReader = open('./wordIndex/pok','r')
    csvLines = []
    timeLines = []
    for line in timeReader:
        if (line=='' or line=='\n'):
            pass
        else:
            timeLines.append(line.strip('\n').split(':')[1])

    for line in freReader:
        if (line=='' or line=='\n'):
            pass
        else:
            tmp1 = line.split(':')
            tmp2 = [int(tmp1[0]),int(tmp1[1])]
            csvLines.append([timeLines[tmp2[0]],'0',str(tmp2[1]),'ha','la'])
    timeReader.close()
    freReader.close()
    csvWriter = open('wordFre.csv','w')
    csvWriter.write("date,delay,distance,origin,destination\n")
    for line in csvLines:
        csvWriter.write(line[0]+','+line[1]+','+line[2]+','+line[3]+','+line[4]+'\n')
    csvWriter.close()

def main():
    getArticleTime()
    #makeWordFreCsv()
    
if __name__=="__main__":
    main()