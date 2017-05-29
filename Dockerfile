FROM python:3.6.1-onbuild
MAINTAINER Marina Polyakova <iefendra@gmail.com>
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code
RUN python3 manage.py collectstatic --noinput
CMD python3 manage.py runserver 0.0.0.0:80
EXPOSE 80