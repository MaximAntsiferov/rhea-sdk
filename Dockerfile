FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install curl -y

RUN curl --proto '=https' --tlsv1.2 -LsSf https://github.com/near/near-cli-rs/releases/latest/download/near-cli-rs-installer.sh | sh

COPY main.py .

RUN pip install asyncio

COPY . .

CMD ["bash"]