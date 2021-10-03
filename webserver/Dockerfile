FROM python:3.8

#copy source files
COPY ./ /usr/src/app/

#change file permissions
RUN chmod 777 /usr/src/app/webserver.py
RUN chmod 777 /usr/src/app/index.html
RUN chmod 777 /usr/src/app/github.png
RUN chmod 777 /usr/src/app/background2.jpg

#open port
EXPOSE 80

#run webserver
CMD ["python", "/usr/src/app/webserver.py"]
