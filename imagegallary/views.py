from django.shortcuts import render
from .forms import imageForm
from .models import imagegallary

# Create your views here.
def index(request):
    if request.method=="POST":
        form=imageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
    else:
        form=imageForm()
    img=imagegallary.objects.all()
    dic_form={
        'form':form,
        'img':img
    }
    return render(request,"imagegallary.html",dic_form)