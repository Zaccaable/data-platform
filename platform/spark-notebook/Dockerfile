FROM jupyter/pyspark-notebook:spark-3.1.2

COPY ./jars/* /usr/local/spark/jars/

RUN pip install delta-spark==1.0.0
