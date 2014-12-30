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
def relevantArticleNum():
    num = []
    fileWriter = open('relevantArticleNum.txt','w')
    path = "../../MC1 Data/MC1 Data/articles/"
    for i in range(0,845):
        fileReader = open(path+str(i)+'.txt','r')
        cnt = 0;
        for line in fileReader:
            if (cnt==0):
                cnt+=1
                continue
            else:
                if (line.strip('\n').strip('\r').strip(' ')==''):
                    continue
                elif (cnt>=2):
                    if (line[0].isdigit()):
                        num.append(line.strip('\n').strip('\r'))
                        break
                    else:
                        continue
                else:
                    cnt+=1
        fileReader.close()

    time = []
    for item in num:
        if (len(item.split('/'))==3):
            if (int(item.split('/')[0])>=2014):
                time.append(item.split('/'))
        else:
            tmp = item.split(' ')
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
            if (tmp[0]>=2014):
                time.append(tmp)
            
    row = 0
    for item in time:
        fileWriter.write(str(row)+': '+item[0]+' '+item[1]+' '+item[-1]+'\n')
        row += 1
    fileWriter.close();

def main():
    paperStat()
    relevantArticleNum()
    
if __name__=="__main__":
    main()