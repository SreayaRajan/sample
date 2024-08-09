from django.shortcuts import render
from .models import ImageForm
from .models import imagegallary
# Create your views here.
def index(request):
    if request.method=="POST":
       form=ImageForm(data=request.POST,files=request.FILES) 
    if form.is_valid():
        form.save()
    else:
        forms =ImageForm()
    dic_form={
        'from' :form
    } 
    return render(request,"imagegallary.html",dic_form)    
