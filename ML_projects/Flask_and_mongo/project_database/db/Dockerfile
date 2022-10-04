FROM python:3.8-slim

# mention workdir
WORKDIR /usr/src/app

# copy requirements 
COPY requirements.txt .

# run commands 

RUN pip install --no-cache-dir -r requirements.txt 

# copy current files into the current workding dir 

COPY . . 

# CMD to run in docker 

CMD python app.py