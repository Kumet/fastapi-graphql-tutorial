# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to PATH
ENV PATH="/root/.local/bin:${PATH}"

# Copy pyproject.toml and poetry.lock to the container
COPY ./pyproject.toml ./poetry.lock /app/

# Install the dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

# Copy the application code to the container
COPY ./app /app

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Remove unnecessary dependencies and clean up cache
RUN apt-get autoremove -y gcc curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Run uvicorn when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]