FROM python:3.11-slim
WORKDIR /root/task
COPY requirements.txt /root/task
RUN pip install --no-cache-dir -r requirements.txt
COPY . /root/task
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
