from django.shortcuts import render, redirect

APACHE_HADOOP_URL= "https://hadoop.apache.org/"
APACHE_SPARK_URL= "https://en.wikipedia.org/wiki/Apache_Spark"
JUPYTER_NOTEBOOK_URL= "http://localhost:8888"
SONARQUBE_URL= "http://localhost:9000"


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
