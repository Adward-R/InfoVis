#Ignored all appeared words with their frequency less than 10
import os
import os.path
def main():
    fileWriter = open("./index_analyzer_result.txt",'w')
    frequency = {}
    path = r'./wordIndex/'
    for parent, dirs, files in os.walk(path):
        for f in files:
            s = os.path.join(parent,f)
            #print s
            fileReader = open(s,'r')
            cnt = 0
            for line in fileReader:
                ss = line.split(':')[1]
                if (ss!=''): #handle special cases
                    cnt += int(line.split(':')[1])
            if (cnt>=10):
                frequency[str(f)] = cnt
            fileReader.close()
    frequency = sorted(frequency.iteritems(),key = lambda d:d[1],reverse = True)
    for fre in frequency:
        fileWriter.write(fre[0]+': '+str(fre[1])+'\n')
    fileWriter.close()

if __name__ == '__main__':
    main()