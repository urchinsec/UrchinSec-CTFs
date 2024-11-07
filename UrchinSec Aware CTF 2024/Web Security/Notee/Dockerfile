# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY app.py .
COPY flag.txt /secret_flag_here_48195.txt
COPY templates/index.html ./templates/index.html
COPY model.py .
COPY helpers.py .

# Expose the port the app runs on
EXPOSE 5003

# Define the command to run the app
CMD ["python", "app.py"]