# app/Dockerfile

FROM python:3.10.6-slim-bullseye

EXPOSE 8501

WORKDIR /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt

# RUN apt-get update && apt-get install -y \
#     build-essential \
#     software-properties-common \
#     git \
#     && rm -rf /var/lib/apt/lists/*

COPY . /app/

ENV PYTHONPATH=/app
ENTRYPOINT ["streamlit", "run", "/app/core/runner.py", "--server.port=8501", "--server.address=0.0.0.0"]