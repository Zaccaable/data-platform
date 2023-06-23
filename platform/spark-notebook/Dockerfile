FROM jupyter/pyspark-notebook:spark-3.1.2

# Add AWS jars needed for minio
COPY ./jars/* /usr/local/spark/jars/

ENV HADOOP_HOME=/usr/local/hadoop
ENV HIVE_HOME=/usr/local/hive

ENV METASTORE_HADOOP_VERSION=3.2.0
ENV METASTORE_VERSION=3.0.0

USER root

# install core packages 
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
      sudo \
      curl \
      unzip \
      make \
      openjdk-11-jdk \
      build-essential \
      software-properties-common \
      libpq-dev \
      gcc \
      g++ \
      libsasl2-dev \
      unixodbc-dev \
      ssh \
      postgresql-client 

RUN mkdir -p ${HADOOP_HOME} ${HIVE_HOME}
# Install hive to be used as metastore
RUN curl https://archive.apache.org/dist/hadoop/common/hadoop-${METASTORE_HADOOP_VERSION}/hadoop-${METASTORE_HADOOP_VERSION}.tar.gz -Lo hadoop.tgz \
    && tar xvzf hadoop.tgz --directory ${HADOOP_HOME} --strip-components 1 \
    && rm hadoop.tgz 

RUN curl https://downloads.apache.org/hive/hive-standalone-metastore-${METASTORE_VERSION}/hive-standalone-metastore-${METASTORE_VERSION}-bin.tar.gz -Lo hive.tgz \ 
    && tar xvzf hive.tgz --directory ${HIVE_HOME} --strip-components 1 \
    && rm hive.tgz

# postgres driver for hive
RUN curl https://repo1.maven.org/maven2/org/postgresql/postgresql/42.4.0/postgresql-42.4.0.jar -Lo pgsql.jar \ 
    && mv pgsql.jar ${HIVE_HOME}/lib 

# Install delta
RUN pip install delta-spark==1.0.0
RUN pip install minio pandas requests

# Transfer config files
#COPY conf/spark-defaults.conf ${SPARK_HOME}/conf
COPY metastore-site.xml ${HIVE_HOME}/conf

USER jovyan
