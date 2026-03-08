FROM apache/spark:3.5.1

USER root

WORKDIR /app

RUN pip install pyspark boto3

COPY ingest_bronze.py /app/

CMD ["sleep", "infinity"]