FROM python:3

COPY test2.py .

CMD ["python", "test2.py", "5,7"]