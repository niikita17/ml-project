from django.shortcuts import render,redirect
from django.http import HttpResponse 
from django.contrib.auth import authenticate,login
import os
import pickle
import math
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import seaborn as sns

# Create your views here.
def registration(request):
        return render(request,'home.html')
def result(request):
        if request.method=="POST":
                temp={}
                temp['temp1']=request.POST.get("temp")
                temp['humi1']=request.POST.get("humdity")
                temp['exe1']=request.POST.get("exe")
                temp['step1']=request.POST.get("step")
                model=pickle.load(open("model\classifier.pkl",'rb'))
                testdata=pd.DataFrame({'x':temp}).transpose()

                pred=model.predict(testdata)[0]
                
                if(pred==0):
                        result="You Don't need water !"
                else:
                        result='You Should Drink water !'
                print(pred)
                return render(request,"result.html",{'result':result})
                
        return render(request,"result.html")
        
                
        
 

     
    




    
    
            


