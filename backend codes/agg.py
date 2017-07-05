from pyspark import SparkContext
#from pyspark import operator
sc = SparkContext("local", "Simple App")



if __name__ == "__main__":
	data = []
	rdd1 = sc.textFile("hdfs://localhost/user/jinaligandhi/input/united-final.txt")
	links = rdd1.map(lambda line:line.split(' ')).map(lambda pages: (pages[0],pages[1])).distinct().groupByKey().persist()
	for link in  links.collect(): 
		sum = 0
		n = 0
		for i in link[1]:
			i = float(i)
			if i == 0.0:
				print (i)
				continue
			else:
				n = n+1
				sum = sum + float(i)
				avg = sum/n
		data.append((link[0], avg))
	print data
		
		
			