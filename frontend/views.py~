from django.shortcuts import render,HttpResponse
from rest_framework.generics import ListAPIView,CreateAPIView
from .models  import DataReact,DataEncadreur
from .serializers import DataSerializers,DataSerializersE
from .utils import send_email_with_html_body
from .outils1 import send_email_with_html_body2
from django.contrib.auth.models import User 
from datetime import datetime
from django.views.decorators.csrf import csrf_protect
from rest_framework.decorators import action

@csrf_protect    
def create_view(request, *arg,**kwargs):
    data = DataReact.objects.all()
 
    i=-1
    a=0
    for datas in data :
        i=i+1
    
  
    day = (data[i].jours).split(";")
    matiere = data[i].matiere.split(";")
    
    count2 = len(day)
    count  = len(matiere) 
    ctxx={
         "data":data[i],
                    'count':count,
                    'count2':count2,
    }
   
    if request.method == "POST":
        email = request.POST.get('email')
        
        subject="test email"
        template = "emil.html"
        context = {
            'date': datetime.today().date,
            'email':email,
            
        }
       
        has_send=send_email_with_html_body (
                                subject,
                                
                                template=template,
                                context=context)
            
        if has_send:
            ctxx = {"msg":"mail envoyer avec succes",
                    "data":data[i],
                    'count':count,
                    'count2':count2,
                    'i':True
                   }
        else:
            ctxx ={"msg":"erreur lors de l'envoi",
                   "data":data[i],
                    'count':count,
                    'count2':count2,
                    'i':False}    

    return  render(request, 'index1.html',ctxx) 





def create_view1(request, *arg,**kwargs):
    data = DataEncadreur.objects.all()
 
    i=-1
   
    for datas in data :
        i=i+1
    

    ctxx={
        "data":data[i],
                 
        
    }
  
   
    if request.method == "POST":
        email = request.POST.get('email')
        
        subject="serad Encardreur"
        template = "email2.html"
        context = {
            'date': datetime.today().date,
            'email':email,
            
        }
       
        has_send=send_email_with_html_body2 (
                                subject,
                                
                                template=template,
                                context=context)
            
        if has_send:
            ctxx = {"msg":"mail envoyer avec succes",
                    "data":data[i],
                 
                    'i':True,
                   }
        else:
            ctxx ={"msg":"une erreur c'est produise veillez ressayer "
                  ,"data":data[i],}    

    return  render(request, 'index2.html',ctxx) 

class ListData(ListAPIView):
    queryset = DataReact.objects.all()
    serializer_class = DataSerializers 

# Create your views here.
class createData(CreateAPIView):
    queryset = DataReact.objects.all()
    serializer_class = DataSerializers
#-------------------------------------------

class ListDataE(ListAPIView):
    queryset =DataEncadreur.objects.all()
    serializer_class = DataSerializersE
    


class CreateDataE(CreateAPIView):
    queryset = DataEncadreur.objects.all()
    serializer_class = DataSerializersE

   
   
     
   
# data = DataReact.objects.all()
# print(data)
    
def create_view2(request, *arg,**kwargs):
  
    data = DataReact.objects.all()
   
  
    i = int
    i=0
    for datas in data :
        i=i+1
    
    if request.method == "POST":
        email = request.POST.get('email')

        subject="test email"
        template = "emil.html"
        context = {
            'date': datetime.today().date,
            "email":email
        }
        receivers=[email]

        has_send=send_email_with_html_body (
                                subject = subject,
                                 receivers= receivers,
                                template =template,
                                context=context)
        
        name ="yves"
        ctx={
           

          }    
        if has_send:
            ctx = { "msg":name,
                   
                   
                   }
            
        else:
            ctx ={"msg":"erreur lors de l'envoi"}    

    return  render(request, 'index.html',ctx) 
        

def test(request,*arg,**kwargs):
    name = 'yves'
    number = '5'
    context ={
        "name":name,
        "num":number
    }

    return render(request,'index.html',context)