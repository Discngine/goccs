FROM continuumio/miniconda:4.7.12
COPY . /opt/goccs

ENV TINI_VERSION v0.16.1
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini

RUN conda config --add channels conda-forge && conda config --add channels omnia && conda install -y nomkl openmm rdkit pdbfixer biopython
WORKDIR /opt/goccs

ENTRYPOINT [ "/usr/bin/tini", "--" ]``
CMD "python goccs.py"
