FROM allennlp/allennlp:v0.8.5

RUN pip3 install torch

COPY * ./

RUN mkdir -p data/
RUN mkdir -p output/

ENTRYPOINT []
CMD /bin/bash

