FROM python:3.10-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["streamlit", "run", "app.py", "--server.port=5000", "--server.enableCORS=false", "--server.enableXsrfProtection=false"]