FROM python:3.8

COPY . /app
WORKDIR /app
# Build project inside of docker file
RUN pip install -r requirements.txt

# Command to run container on start
CMD ["python", "app.py"]