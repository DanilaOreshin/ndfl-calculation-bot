FROM python:3.13

WORKDIR /opt/ndfl-calculation-bot

COPY requirements.txt .
RUN /venv/bin/pip install --no-cache-dir -r requirements.txt

COPY src ./src
COPY main.py .

RUN python3 -m venv /venv

CMD ["/venv/bin/python", "main.py"]
