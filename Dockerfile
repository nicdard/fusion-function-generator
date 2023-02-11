FROM ubuntu:20.04 AS build

SHELL ["/bin/bash", "-c"]
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get -y install tzdata && \
    apt-get -y install \
    clang \
    cmake \
    creduce \
    cron \
    curl \
    doxygen \
    default-jdk \
    flex \
    g++ \
    git \
    graphviz \
    libgmp-dev \
    make \
    nano \
    ninja-build \
    python3 \
    python3-pip \
    python3-setuptools \
    python-is-python3 \
    sudo

RUN pip3 install toml ddsmt antlr4-python3-runtime==4.9.2 gcovr slack_sdk ffg pyparsing

WORKDIR /app/

RUN git clone https://github.com/testsmt/yinyang.git

RUN git clone https://github.com/testsmt/semantic-fusion-seeds.git

# Clone cvc5 on changes to the master branch
RUN git clone https://github.com/cvc5/cvc5
RUN cd cvc5 && \
    CXXFLAGS="-fprofile-arcs -ftest-coverage" CFLAGS="-fprofile-arcs -ftest-coverage" LDFLAGS="-fprofile-arcs -ftest-coverage" ./configure.sh  debug --coverage --auto-download --poly --cryptominisat --kissat && \
    cd build && \
    make && \
    make install

# Clone z3 on changes to the master branch
RUN git clone https://github.com/Z3Prover/z3
RUN cd z3 && \
    CXXFLAGS="-fprofile-arcs -ftest-coverage" CFLAGS="-fprofile-arcs -ftest-coverage" LDFLAGS="-fprofile-arcs -ftest-coverage" ./configure --debug && \
    cd build && \
    make && \
    make install

# Fix missclassification bug.
RUN mv semantic-fusion-seeds/LIA/unsat/NUM899-1.smt2 semantic-fusion-seeds/LIA/sat/NUM899-1.smt2 && \ 
    mv semantic-fusion-seeds/LIA/sat/NUM889-1.smt2  semantic-fusion-seeds/LIA/unsat/NUM889-1.smt2

# Copy the project
COPY . .
RUN chmod +x scripts/* scripts/reduce/*
