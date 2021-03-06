# -*- coding: utf-8 -*-
"""learned index demo2.ipynb


Generate some simple dataset in csv format
"""

print("Learned Index Models, by piaoxirui")
print("This program comes with ABSOLUTELY NO WARRANTY;")
print("This is comparison of different learning indexes")
print("======================================================================================")

import os
import codecs
import random
#function: data_generation
#usage: generate a simple dataset
#parameters:
#1.len_num: the size of dataset
#2.range_min: the minimum key
#3.range_max: the maximun key
#output dataset: two columns (key,location)
import os
import codecs
import random
#function: data_generation
#usage: generate a simple dataset
#parameters:
#1.len_num: the size of dataset
#2.range_min: the minimum key
#3.range_max: the maximun key
#output dataset: two columns (key,location)
def data_generation(len_num,range_min,range_max):
	dataset=set()
	for i in range(0,len_num):
		x=random.randint(range_min,range_max)
		while x in dataset:
			x=random.randint(range_min,range_max)
		dataset.add(x)
	# for i in range(0,len(datalist)):
	# 	temp=False
	# 	for j in range(0,len(datalist)-i-1):
	# 		if datalist[j]>datalist[j+1]:
	# 			t=datalist[j]
	# 			datalist[j]=datalist[j+1]
	# 			datalist[j+1]=t
	# 			temp=True
	# 	if not temp:
	# 		break
	current_path=os.path.abspath(os.curdir)
	f=codecs.open(os.path.join(current_path,"data.csv"), "w", "utf-8")
	i=0
	datalist=list(dataset)
	datalist.sort()
	for ele in datalist:
		f.write(str(ele)+","+str(int(i/(len_num/100)))+"\n")
		i=i+1
	f.close()
	return


"""Provide some value and generate the dataset"""

minkey=0
maxkey=2147483647
keynum=5000000
data_generation(keynum,minkey,maxkey)


