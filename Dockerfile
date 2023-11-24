# Use an official Alpine Linux image as the base image
FROM python:3.11-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt /app/

# Install dependencies for the image and the project
RUN apk update \
    && apk add --no-cache postgresql-libs \
    && apk add --no-cache --virtual .build-deps \
        gcc \
        musl-dev \
        postgresql-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && apk --purge del .build-deps

# Copy the project files to the working directory
COPY . /app/

# collect static files
RUN python manage.py collectstatic --noinput

# Expose the port the search app runs on
EXPOSE 8000

# Run the application using wsgi
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "core.wsgi:application"]
