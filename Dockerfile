# syntax=docker/dockerfile:1
FROM ubuntu:18.04
WORKDIR /app
ENV FLASK_APP=softdes.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY requirements.txt requirements.txt
COPY src/ src/
RUN apt update -y
RUN apt-get install python3-pip -y
RUN pip3 install -r requirements.txt
RUN apt install sqlite3 -y
RUN if [ -f "src/users.csv" ] ; then echo "Users exist." ; else echo "admin, admin" > src/users.csv ; fi
RUN if [ -f "src/quiz.db" ] ; then echo "Database exists." ; else sqlite3 src/quiz.db < src/quiz.sql ; fi
WORKDIR src
RUN python3 adduser.py
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV FLASK_RUN_PORT=8080
EXPOSE 8080
CMD ["flask", "run"]