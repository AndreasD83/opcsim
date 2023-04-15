FROM python:3

ENV COLOR "red"
#RUN apt-get update -y && \
#    apt-get install -y python-pip python-dev

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 4840
ENTRYPOINT [ "python" ]

CMD [ "app.py" ]


#sudo docker build -t opcsimulator:latest .
#oc new-app opcsimulator./oc apply -f opcsimulator/service.yaml
#sudo docker build -t 172.30.1.1:5000/myproject/opcsimulator .
#sudo docker push 172.30.1.1:5000/myproject/opcsimulator:latest


#sudo docker tag opcsimualtor $(minishift openshift registry)/myproject/opcsimulator
#sudo docker push $(minishift openshift registry)/myproject/opcsimulator