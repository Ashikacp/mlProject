FROM python:3.9-slim-buster
WORKDIR /application
COPY . /application
RUN apt update -y && apt install awscli -y
RUN pip install -r requirements.txt
CMD ["python","application.py"]
EXPOSE 5001