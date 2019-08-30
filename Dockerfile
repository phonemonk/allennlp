FROM allennlp/allennlp:v0.8.5

COPY * ./

RUN mkdir -p data/
RUN mkdir -p output/

ENTRYPOINT []
CMD /bin/bash

