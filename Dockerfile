
FROM python:3.12.0

WORKDIR /app
COPY . /app

ADD requirement.txt .


#copy the current directory contents into the container at /usr/src/app
COPY . .

# Copy the current directory contents into the container
COPY sematic.py . 


RUN Python3 -m pip install requirement.txt


CMD ["python", "sematic.py"] 
