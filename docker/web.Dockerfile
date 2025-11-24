FROM python:3.11-slim

WORKDIR /app

# Copy only requirements first for caching
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy all code
COPY . /app/

# Make entrypoint executable
RUN chmod +x /app/docker/django-entrypoint.sh

ENTRYPOINT ["/app/docker/django-entrypoint.sh"]
