# syntax=docker/dockerfile:1
FROM ubuntu:18.04
WORKDIR /app
ENV FLASK_APP=softdes.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV FLASK_RUN_PORT=8080
EXPOSE 8080
COPY requirements.txt requirements.txt
RUN apt update -y && \
    apt-get install python3-pip -y && \
    pip3 install -r requirements.txt && \
    apt install sqlite3 -y
COPY src/ src/
RUN if [ -f "src/users.csv" ] ; then echo "Users exist." ; else echo "admin, admin" > src/users.csv ; fi && \
    if [ -f "src/quiz.db" ] ; then echo "Database exists." ; else sqlite3 src/quiz.db < src/quiz.sql ; fi
WORKDIR src
RUN python3 adduser.py
CMD ["flask", "run"]