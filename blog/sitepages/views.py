from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.contrib import messages


def about(request):
    return render(request, 'sitepages/about.html')

def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)
        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')
            send_mail('Blog contact' + contact_name, form_content, contact_email, ['gabriel.juraj@gmail.com'], fail_silently=False)
            return redirect('contact')
    return render(request, 'sitepages/contact.html', {
        'form': form_class,
    })
