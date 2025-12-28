#FROM python:3.9.0-slim-buster
#
#WORKDIR /app
#
#COPY requirements.txt /app/
#
#RUN apt-get update && \
#    apt-get install --no-install-recommends -y && \
#    rm -rf /var/lib/apt/lists/* && \
#    pip install --no-cache-dir --upgrade pip && \
#    pip install --no-cache-dir -r requirements.txt
#
#COPY . /app/
#
#CMD ["python", "bot.py"]
FROM python:3.10-slim-bookworm

WORKDIR /app

# (Optional) system deps: build tools only if you need to compile something
# Most of your deps have wheels, so you can often skip build-essential.
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      ca-certificates \
      gcc \
      libpq-dev \
 && rm -rf /var/lib/apt/lists/*


COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt


COPY . .

CMD ["python", "bot.py"]
