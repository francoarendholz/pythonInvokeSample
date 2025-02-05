import os
from invoke import task
from pythonModuleSample.Sample1.Sample1 import Sample1

##################
#      Tasks     #
##################

@task
def printHelloWorld(c):
    sampleModule = Sample1()
    print(sampleModule.hello_world())
    
@task
def printHelloString(c):
    os.environ["HELLO_STRING"] = "Hello String!"
    sampleModule = Sample1()
    print(sampleModule.hello_world())