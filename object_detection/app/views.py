from django.shortcuts import render, HttpResponse
from app.forms import imageform

# Create your views here.

def home(request):
    if(request.method == 'POST'):
        form = imageform(request.POST, request.FILES)
        if(form.is_valid()):
            filename = form.cleaned_data['image']
            form.save()
        else:
            context = {'form': form}
            return render(request, "home.html", context)
    context = {'form': imageform()}
    return render(request, "home.html", context)