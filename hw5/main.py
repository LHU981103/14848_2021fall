import sys
import re
from pyspark import SparkContext, SparkConf

conf = SparkConf()
# create Spark context with necessary configuration
sc = SparkContext.getOrCreate(conf=conf)

stop_word_list = ["they", "she", "he", "it", "the", "as", "is", "and"]

# Conduct MapReduce and write the output to folder
wordCounts = sc.wholeTextFiles("Data").flatMap(lambda file:((word, file[0]) for word in re.findall(r"[\w']+", file[1])))\
    .filter(lambda words: words[0] not in stop_word_list)\
    .map(lambda words: (words, 1))\
    .reduceByKey(lambda a,b: a+b)\
    .map(lambda words: (words[0][0], (words[0][1], words[1])))\
    .reduceByKey(lambda a,b: a+b).saveAsTextFile("output")

