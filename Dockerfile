FROM python:3.10-slim-bookworm

ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y \
    g++ \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /code

COPY poetry.lock pyproject.toml ./
RUN pip install poetry

RUN poetry config virtualenvs.create false
RUN poetry install -n --no-ansi

COPY . .

CMD tail -f /dev/null
