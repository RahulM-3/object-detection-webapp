from django.shortcuts import render, HttpResponse
from app.forms import imageform

# Create your views here.

def home(request):
    uploaded_image = None
    if(request.method == 'POST'):
        form = imageform(request.POST, request.FILES)
        if(form.is_valid()):
            filename = form.cleaned_data['image']
            uploaded_image = form.save()
        else:
            context = {'form': form}
            return render(request, "home.html", context)
    context = {'form': imageform(), "uploaded_image": uploaded_image}
    return render(request, "home.html", context)