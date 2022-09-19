# Python image to use.
FROM python:3.10-slim

ARG PORT
# Set the working directory to /app
WORKDIR /app

# copy the requirements file used for dependencies
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the working directory contents into the container at /app
COPY . .

# Run main.py when the container launches
# CMD uvicorn main:app --host 0.0.0.0 --port $PORT
#CMD exec uvicorn --port $PORT --host 0.0.0.0 main:app

ENTRYPOINT ["uvicorn", "main:app", "--port", "$PORT"]