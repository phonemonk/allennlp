#!/bin/python

import sys
import os
import json


outfile = sys.argv[1]

os.exec("allennlp predict --silent --use-dataset-reader --cuda-device 0 output/crf_model/model.tar.gz data/infile.conll --silent --output-file /tmp/out")

with open(outfile) as j:
    data = json.load(j)
    words = data['words']
    tags = data['tags']
    
if len(words) != len(tags):
    print("Improper!")
    sys.exit(1)

for i in range(len(words)):
    print("%s %s" % (words[i], tags[i]))




