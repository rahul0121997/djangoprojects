from django.shortcuts import render
from .forms import simpleForm, ContactForm
from .models import Contact

# Create your views here.
def form(request):
    if request.method == 'POST':
        form = simpleForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            info = Contact.objects.create(
                name=name,
                email=email,
                message=message
            )
            return render(request, 'success.html', {'name': name, 'info':info ,'email': email, 'message': message})
    else:
        form = simpleForm()

    return render(request, 'forms.html', {'form': form})

def models(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    else:
        form = ContactForm()

    return render(request, 'modelsforms.html', {'form': form})