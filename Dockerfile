FROM allennlp/allennlp:v0.8.5

COPY * ./

RUN mkdir -p data/

ENTRYPOINT []
CMD /bin/bash

