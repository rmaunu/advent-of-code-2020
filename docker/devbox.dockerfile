ARG BASE_OS=${BASE_OS:-centos75}
ARG PYTHON_VERSION=${PYTHON_VERSION:-python3.6}
ARG DOCKER_PYTHON_VERSION=${DOCKER_PYTHON_VERSION:-python36}

FROM wayfair/python/${BASE_OS}-${DOCKER_PYTHON_VERSION}-devbox:0.4.0

USER root

#RUN yum install -y openblas-devel atlas-devel git-lfs && yum clean all

RUN groupadd -g 80 www || true \
    && usermod -aG www ${USER}

USER ${USER}

#RUN /pyenv/versions/advent-of-code-2020/bin/pip install --only-binary :all: -r requirements-test.txt

ENV PYTHONPATH="$PYTHONPATH:/app"
