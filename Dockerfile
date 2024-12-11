# Use the official Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install the required dependencies
RUN pip install -r /app/requirements.txt

CMD ["python", "consumer.py", "user1"]
