# this is my base image
FROM python:3.7

# Install python and pip
RUN pip install --upgrade setuptools
RUN pip install --upgrade pip
RUN pip install pickle-mixin
# RUN pip install python3-sklearn
# RUN apk add --update py3-pip


# install Python modules needed by the Python app
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

# copy files required for the app to run
COPY app.py /usr/src/app/
COPY data.csv /usr/src/app/
COPY model.pickle /usr/src/app/
COPY logo.png /usr/src/app/
# COPY templates/index.html /usr/src/app/templates/

# tell the port number the container should expose
EXPOSE 5000

# run the application
CMD ["streamlit", "run", "/usr/src/app/app.py","--server.port=5000", "--server.address=0.0.0.0"]
