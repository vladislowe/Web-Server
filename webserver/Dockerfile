FROM python:3.8

#copy source files
COPY ./ /usr/src/app/

#change file permissions
RUN chmod 755 /usr/src/app/*

#open port
EXPOSE 80

#run webserver
CMD ["python", "/usr/src/app/webserver.py"]
