FROM python:3
  
    ENV PYTHONUNBUFFERED 1
    RUN mkdir /code
    WORKDIR /code
    COPY requirements.txt /code/
    RUN rm ~/.cache/pip -rf && pip install -r requirements.txt
    COPY . /code/

    EXPOSE 8000
    
    WORKDIR /code/django_src

    CMD ["python", "manage.py", "runserver","0.0.0.0:8000"]