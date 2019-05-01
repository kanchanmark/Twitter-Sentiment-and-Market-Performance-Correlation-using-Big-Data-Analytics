import sys

from pyspark import SparkContext
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.stat import Statistics
from pyspark.mllib.util import MLUtils

#sc = SparkContext("local", "Simple App")

if __name__ == "__main__":

	sc = SparkContext(appName="PythonPearsonCorrelation")
	corrType= 'pearson'
	arr1 = []
	arr2 = []
	data =  sc.textFile('file:/')
	arr1 = [x for x in data.toLocalIterator()]
	data1 =  sc.textFile('file:/')
	arr2 = [x for x in data1.toLocalIterator()]
	
	
	print(arr1)
	print(arr2)

	
	
	sentiment_aggregate = sc.parallelize(arr1)
	stocks_open = sc.parallelize(arr2)
	
	
	corr = Statistics.corr(sentiment_aggregate, stocks_open, corrType)
	print 'Pearson Correlation: \t%g' %(corr)
	
	corrType='spearman'
	corr = Statistics.corr(sentiment_aggregate, stocks_open, corrType)
	print 'Spearman Correlation: \t%g' %(corr)

	sc.stop()
