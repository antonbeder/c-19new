FROM centos:latest
#RUN yum install python3 -y
#RUN yum update -y
#RUN pip3 install requests
WORKDIR /src
COPY . /src
CMD ["python3","c-19.py"]
