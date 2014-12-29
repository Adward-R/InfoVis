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
    
    for item in num:
        fileWriter.write(item+'\n')
    fileWriter.close();

def main():
    paperStat()
    relevantArticleNum()
    
if __name__=="__main__":
    main()