# syntax=docker/dockerfile:1

## === COMMENT: Tells Docker which Dockerfile syntax/features to use (here, the v1 “modern” syntax). 


## === COMMENT: Uses the official python:3.12-slim image as the base, giving you Python 3.12 on a minimal Debian-based image.
FROM python:3.12-slim

## === COMMENT: Sets an environment variable so Python does not create .pyc bytecode files, keeping the image smaller and the filesystem cleaner.
## === COMMENT: Forces Python to run in unbuffered mode so logs are flushed immediately to stdout/stderr (important for seeing logs in Docker).
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

## === COMMENT: Set work directory
## === COMMENT: Sets /app as the working directory inside the container; all following relative paths and commands run from here.
WORKDIR /app

## === COMMENT: Install dependencies
COPY requirements.txt .

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        gcc \
        libffi-dev \
        libssl-dev \
        python3-dev && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt


## === COMMENT: Copy app code
## === COMMENT: Copies all files from your project directory (on the host) into /app in the container, including your application code.
COPY . .


## === COMMENT: Expose port (inside container)
## === COMMENT: Documents that the container listens on port 8000; used by tooling and for clarity, but does not itself publish the port.
EXPOSE 8000


## === COMMENT: Start the app
## === COMMENT: Defines the default command when the container starts: runs Uvicorn to serve the ASGI app app from the main module, binding on all interfaces at port 8000.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
