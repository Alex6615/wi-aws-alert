# Base image
FROM python:3.9.16-alpine

# Install dependencies
RUN apk upgrade
#RUN apk --update \
#    add gcc \
#    make \
#    build-base \
#    bind-tools\
#    g++

COPY . /wi-aws-alert
WORKDIR /wi-aws-alert
RUN pip3 install -r requirements.txt
RUN rm -r ~/.cache/pip    


# Run the application
ENTRYPOINT ["python3", "appdev.py"]