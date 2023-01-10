FROM python:3.9
RUN apt-get update -qy
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python3","app.py"]
