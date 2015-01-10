Pre-Processing
====
& 重要的中间结果等

----

 - ##*pre.py*
 
 	包含统计出paperStat.txt、articleTime.csv的两个功能模块，还有一个本来想用于统计CrossFilter需要的数据的makeWordFreCsv()函数，但是那玩意儿太难学（细节有点多），暂且不用了；
 	
 - ###paperStat.txt
 
 	各报社发文总数的统计，没啥用，稍微改一下统计方法可能有用；
 	
 - ###totalWordsFrequency.txt
 
 	之前统计的出现十次以上的各词词频，没啥用；
 	
 - ##articleTime.csv
 
 	每篇报道的[编号，时间，报社名]，狂有用，各种脚本处理前读取它一下都会减小工作量；
 	
 - ##*indexer.py*
 
 	读取所有articles/建term的倒排索引的脚本，有用；
 	
 - ##wordIndex/
 
 	建好的索引文件都放在这里，一个词一个文件（无后缀名）；
 	
 - ###*words_fre_json_generator.py*
 
 	读索引建词频索引给词云用的脚本，有了自动词云生成器好像基本没啥用了；