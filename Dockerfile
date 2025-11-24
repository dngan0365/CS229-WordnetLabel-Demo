FROM python:3.12

RUN apt-get update && apt-get install -y swi-prolog

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /app
WORKDIR /app

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]