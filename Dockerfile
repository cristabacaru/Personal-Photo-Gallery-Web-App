# Use an official Python runtime as a parent image
FROM python:3.8-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
# ENV FLASK_APP=app.py
# ENV FLASK_RUN_HOST=0.0.0.0
# ENV FLASK_RUN_PORT=5000
ENV NAME="World"

# Run the application
CMD ["python", "app.py"]
