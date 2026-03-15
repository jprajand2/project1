FROM python:3.11
WORKDIR ./project1
COPY . /project1
RUN pip install -r requirements.txt
CMD ["python","program5.py"]