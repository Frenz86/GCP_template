FROM python:3.10-slim

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

# Copy local code to the container image.
COPY . /app
WORKDIR /app

# Install Python Requirements
RUN python -m pip install --upgrade pip \
    && pip install --trusted-host pypi.python.org -r requirements.txt


EXPOSE 80 

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
