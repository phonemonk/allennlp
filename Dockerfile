FROM allennlp/allennlp:v0.8.5

RUN pip3 uninstall torch -y 
RUN pip3 install torch -y

COPY * ./

RUN mkdir -p data/
RUN mkdir -p output/

ENTRYPOINT []
CMD /bin/bash

