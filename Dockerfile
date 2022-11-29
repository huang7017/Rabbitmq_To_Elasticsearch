# Pull base image.
FROM ubuntu:18.04

# Set default WORKDIR in container
WORKDIR /usr/src/app

# Update the repository
COPY . .

# For log message in container
ENV production ${production}
ENV host ${host}
ENV port ${port}
ENV rabbitmqName ${rabbitmqName}
ENV rabbitmqPassword ${rabbitmqPassword}
ENV queue ${queue}
# Install python 3.7
RUN apt-get update -y && \
    apt-get install -y python3.7 python3-pip python3.7-dev

# Install package requirements
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# set datetime
RUN apt-get update \
    &&  DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends tzdata
    
RUN TZ=Asia/Taipei \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone \
    && dpkg-reconfigure -f noninteractive tzdata 

RUN ["chmod", "+x", "/usr/src/app/docker-entrypoint.sh"]
ENTRYPOINT ["/usr/src/app/docker-entrypoint.sh"]