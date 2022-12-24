from django.shortcuts import render
from .models import Post
from .forms import Postform
# Create your views here.
def home(request):
    form=Postform()
    data={'form':form}
    return render(request,'home.html',data)