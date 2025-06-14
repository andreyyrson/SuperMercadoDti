FROM python:3.11-alpine

WORKDIR /main

COPY . /main

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "main.py"]
