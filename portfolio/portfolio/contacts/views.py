from django.shortcuts import render, redirect
from portfolio.contacts.forms import ContactForm
from django.core.mail import send_mail

def index(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            email_subject = form.cleaned_data['email_subject']
            message = form.cleaned_data['message']
            
            form.save()

            # Send email
            subject = email_subject
            message = f"Sender Name: {first_name} {last_name}\nSender Email: {email}\nSubject: {subject}\n\n{message}"
            from_email = email
            recipient_list = ['alex.lemuel@gmail.com']  
            send_mail(subject, message, from_email, recipient_list)

            return redirect('index')
        
    context = {
        'form': form
    }

    return render(request, 'index.html', context=context)
