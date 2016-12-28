# While running this, mount this directory inside the container at /data

FROM mysql:latest

COPY ["create_tables.py", "pop_tables.py", "rds_config.py", "wfd_full.sql", "/tmp/"]

RUN apt-get update && apt-get install -y mysql-client \
                                         vim \
					 wget \
					 python

RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py
RUN pip install pymysql
RUN db_pass=`cat /tmp/rds_config.py | grep db_password | awk -F'"' '{print $2}'` && \
    echo $db_pass && \
    bash -c 'debconf-set-selections <<< "mysql-server mysql-server/root_password password $db_pass"' && \
    bash -c 'debconf-set-selections <<< "mysql-server mysql-server/root_password_again password $db_pass"' && \
    sleep 10 && \ 
    service mysql start && \ 
    ps -ef | grep mysql

WORKDIR /tmp
RUN db_pass=`cat /tmp/rds_config.py | grep db_password | awk -F'"' '{print $2}'` && service mysql start && sleep 5 && mysql < wfd_full.sql

CMD service mysql start
