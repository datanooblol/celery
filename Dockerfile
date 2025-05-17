FROM python:3.11-slim

WORKDIR /src

RUN pip install uv

COPY pyproject.toml .

COPY app ./app

RUN uv sync