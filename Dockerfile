FROM python:3.9-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:${PATH}"

COPY ./pyproject.toml ./poetry.lock ./.flake8 /app/

RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

COPY ./app /app

EXPOSE 8000

RUN apt-get autoremove -y gcc curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]