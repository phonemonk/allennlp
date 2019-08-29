FROM allennlp/allennlp:v0.8.5

COPY * ./

RUN mkdir -p data/

CMD /bin/bash
ENTRYPOINT /bin/bash

