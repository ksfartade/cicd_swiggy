# Use the official Python 3.12.3 image
FROM python:3.12.3-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory in the container
WORKDIR /app

# creating non-root user for this application.
RUN useradd -ms /bin/bash django

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install pip requirements
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project files
COPY . .
RUN chown -R django:django /app

# switching to new user
USER django

# volume for SQlite DB.
VOLUME [ "/app/db" ]

# Collect static files (optional for prod)
# RUN python manage.py collectstatic --noinput

# Expose port 8001
EXPOSE 8001

# Start the Django server on port 8001
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
