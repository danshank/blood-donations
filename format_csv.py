import csv

with open("train\9db113a1-cdbe-4b1c-98c2-11590f124dd8.csv", "r") as f:
	d_reader = csv.DictReader(f)
	
#	print "printing d_reader," 
#	print d_reader

#	headers = d_reader.fieldnames
#	print "printing headers,"
#	print headers

	for line in d_reader:
		print line