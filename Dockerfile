# start with a light weight bas python image
FROM python:3.8-slim-buster 

# set the working DIR
WORKDIR /app

# copy the application files
COPY requirements.txt requirements.txt

# install dependecies
RUN pip3 install -r requirements.txt

# copy all the files
COPY . .

# command to run the application
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]