
# python version number:3.9.16
FROM python:3.9.16
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
# code ... directory for python codes.
WORKDIR /code

# copy localcode to container image.
COPY requirements.txt /code

# upgrade pip command
RUN pip install --upgrade pip 

# install python lib 
RUN pip install -r requirements.txt

COPY . /code/

