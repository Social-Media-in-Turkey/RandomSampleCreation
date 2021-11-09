# -*- coding: utf-8 -*-
"""sample_generation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/137U9KoYpawePXQ72C7fZkrgFyE_b8REd
"""

import json
import random

NSAMPLE = 10000 #Enter how many items you want in your sample.
DATAFILE = "" #Enter your file path. 

def iterate_over_file(datafile):
	with open(datafile, 'r') as fl:
		for line in fl:
			try:
				dpoint = json.loads(line)
				yield dpoint # "yield" keyword will send object one by one
			except Exception as e:
				print('Error parsing data: {}'.format(e))

random.seed(1000102)
def sample_datastream(stream, nSample):
	samples = list()
	for c,item in enumerate(stream):
		if len(samples) < nSample:
			samples.append(item)
		else:
			r = random.randint(0,c+1)
			if r < nSample:
				samples[r] = item
	return samples, c

dataIterator = iterate_over_file(DATAFILE)
mySample, count = sample_datastream(dataIterator, NSAMPLE)
print('{} items processed and {} samples collected'.format(count, len(mySample)))

with open("month_sample_1.json", "w") as random_sample:
    for i in mySample:
        random_sample.write(json.dumps(i))
        random_sample.write("\n")
