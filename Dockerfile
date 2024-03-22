# Set base image (host OS)
FROM python:3.11-alpine

# By default, listen on port 8000
EXPOSE 8000/tcp

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY ./requirements.txt /app

# Install any dependencies
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
ADD flaskrapi_app.py  .
COPY flaskrapi flaskrapi

# Specify the command to run on container start
CMD ["gunicorn"  , "-b", "0.0.0.0:8000", "flaskrapi:create_app()", "--access-logfile=gunicorn.http.log", "--error-logfile=gunicorn.error.log"]