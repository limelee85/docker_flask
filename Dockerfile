FROM python:3.10.12-slim

RUN adduser --system --no-create-home flaskuser

COPY . /app

RUN pip3 install flask 

WORKDIR /app

USER flaskuser
EXPOSE 5000
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
