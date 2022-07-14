FROM centos
# Switching to root to install the required packages
USER root

RUN sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*
RUN sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*
#RUN dnf update && apt upgrade -y
RUN yum install -y gcc gcc-c++ libffi-devel python3-devel python3-pip python3-wheel openssl-devel cyrus-sasl-devel openldap-devel
RUN yum install -y unixODBC
RUN yum install -y unixODBC-devel
RUN yum install -y libatomic
RUN yum install -y libnsl.x86_64

RUN pip3 install --upgrade pip

#RUN apt install -y alien
# Example: installing the MySQL driver to connect to the metadata database
# if you prefer Postgres, you may want to use `psycopg2-binary` instead

RUN pip install psycopg2-binary

# Example: installing a driver to connect to Redshift
# Find which driver you need based on the analytics database
# you want to connect to here:
# https://superset.apache.org/installation.html#database-dependencies
RUN yum install -y wget
RUN wget https://download.dremio.com/arrow-flight-sql-odbc-driver/arrow-flight-sql-odbc-driver-LATEST.x86_64.rpm
#RUN alien --to-deb arrow-flight-sql-odbc-driver-LATEST.x86_64.rpm

RUN rpm -i arrow-flight*.rpm


# TO fix import bug? sqlalchemy
RUN pip install itsdangerous==1.1.0
RUN pip install sqlalchemy==1.3.24
RUN pip install flask-appbuilder==3.1.1
RUN pip install werkzeug==0.16.1
RUN pip install flask-WTF==0.14.2
RUN pip install wtforms==2.3.3
RUN pip install dataclasses
RUN pip install sqlalchemy-dremio
RUN pip install apache-superset
# Switching back to using the `superset` user
#USER superset

RUN export FLASK_APP=superset
RUN superset fab create-admin \
              --username admin \
              --firstname Superset \
              --lastname Admin \
              --email admin@superset.com \
              --password admin

RUN superset db upgrade
RUN superset init

#CMD["superset", "run", "-p 8088 --with-threads --reload --debugger"]
#CMD["superset run -p 8088 --with-threads --reload --debugger"]
COPY start.sh /app/
#CMD ["./start.sh"]
