FROM python:3.12-slim

RUN apt-get update && apt-get install -y swi-prolog

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Render sets $PORT automatically (do not hardcode 8501)
EXPOSE 8501

CMD ["bash", "-c", "streamlit run app.py --server.port=$PORT --server.address=0.0.0.0"]
