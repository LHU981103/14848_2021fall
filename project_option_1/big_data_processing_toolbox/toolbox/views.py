from django.shortcuts import render, redirect

APACHE_HADOOP_URL= "http://35.222.116.101:9870"
APACHE_SPARK_URL= "http://34.66.239.17:8080"
JUPYTER_NOTEBOOK_URL= "http://34.66.245.121:8888"
SONARQUBE_URL= "http://34.66.14.55:9000"


# Create your views here.
def openHadoop(request):
    return redirect(APACHE_HADOOP_URL)


def openSpark(request):
    return redirect(APACHE_SPARK_URL)


def openJupyNotebook(request):
    return redirect(JUPYTER_NOTEBOOK_URL)


def openSonar(request):
    return redirect(SONARQUBE_URL)

def start(request):
    return render(request, 'toolbox/toolbox.html')
