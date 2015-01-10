#Ignored all appeared words with their frequency less than 10
#and filter out their index files
import os
import os.path

def main():
    fileWriter = open("./WordsFrequency.json",'w')
    frequency = {}
    path = r'./wordIndex/'
    for parent, dirs, files in os.walk(path):
        for f in files:
            if str(f)=='.DS_Store':
                continue
            s = os.path.join(parent,f)
            #print s
            fileReader = open(s,'r')
            #print "processing file No."+str(f)
            cnt = 0
            for line in fileReader:
                ss = line.split(':')[1]
                if (ss!=''): #handle special cases
                    cnt += int(line.split(':')[1])
            if (cnt>=100):
                frequency[str(f)] = cnt
            #else:
                #os.remove(s)
            fileReader.close()
    frequency = sorted(frequency.iteritems(),key = lambda d:d[1],reverse = True)

    fileWriter.write('{\n "word": [')
    for i in range(len(frequency)):
        if i!=0 :
            fileWriter.write(',')
        fileWriter.write('"'+frequency[i][0]+'"')
    fileWriter.write('],\n "fre": [')
    for i in range(len(frequency)):
        if i!=0 :
            fileWriter.write(',')
        fileWriter.write(str(frequency[i][1]))
    fileWriter.write(']\n}')
    fileWriter.close()

    

if __name__ == '__main__':
    main()