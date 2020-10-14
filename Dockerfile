FROM python:3.8-slim

#set up working dir
WORKDIR /app

#copy flask app into work dir
COPY . /app

#install any needed packages with pip
RUN pip install --trusted-host pypi.python.org -r requirments.txt 
RUN pip install slackclient
# make p 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
    # the command is 'python3 app.py'
CMD ["python3", "app.py"]