From python:latest
COPY . /usr/src/myapp
WORKDIR /usr/src/myapp
RUN python -m pip install --upgrade pip --user
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["sh", "-c","python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]