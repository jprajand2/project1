FROM python:3.11
WORKDIR /c/Users/george chellappa/project1
COPY . .
RUN pip install -r requirements.txt
CMD ["python","program1.py"]