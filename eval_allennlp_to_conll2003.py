#!/bin/python

import sys
import os
import json
import subprocess


outfile = sys.argv[1]

with open("/tmp/err", "w") as f:
    subprocess.run(["allennlp", "predict", "--silent", "--output-file", outfile, "--use-dataset-reader", "--cuda-device", "0", "output/crf_model/model.tar.gz", "data/infile.conll"], stderr=f, stdout=f)

with open(outfile) as j:
    data = json.load(j)
    words = data['words']
    tags = data['tags']
    
if len(words) != len(tags):
    print("Improper!")
    sys.exit(1)

for i in range(len(words)):
    print("%s %s" % (words[i], tags[i]))




