from django.shortcuts import render

# Create your views here.
def openHadoop(request):
    print ("open hadoop")
    return render(request, 'toolbox/toolbox.html')


def openSpark(request):
    print ("open spark")
    return render(request, 'toolbox/toolbox.html')


def openJupyNotebook(request):
    print ("open Jupyter notebook")
    return render(request, 'toolbox/toolbox.html')


def openSonar(request):
    print ("open sonar")
    return render(request, 'toolbox/toolbox.html')

def start(request):
    return render(request, 'toolbox/toolbox.html')
