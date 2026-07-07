FROM python:3.11-slim AS builder

WORKDIR /build

COPY requirements.txt .

RUN pip install \
    --no-cache-dir \
    --prefix=/install \
    -r requirements.txt



# stage 2
FROM python:3.11-slim

WORKDIR /app

COPY --from=builder /install /usr/local

COPY . . 

EXPOSE 5000

CMD [ "python", "app.py" ]



# docker run -it --rm --network url-network  postgres:16  psql -h postgres-db -U admin -d url_db