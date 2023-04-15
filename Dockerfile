FROM python:3

COPY opcsimulator.py /

EXPOSE 4840
RUN pip install opcua flask requests
CMD ["python", "/opcsimulator.py"]

#sudo docker build -t opcsimulator:latest .
#oc new-app opcsimulator./oc apply -f opcsimulator/service.yaml
#sudo docker build -t 172.30.1.1:5000/myproject/opcsimulator .
#sudo docker push 172.30.1.1:5000/myproject/opcsimulator:latest


#sudo docker tag opcsimualtor $(minishift openshift registry)/myproject/opcsimulator
#sudo docker push $(minishift openshift registry)/myproject/opcsimulator