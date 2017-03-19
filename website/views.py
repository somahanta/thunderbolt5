from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView
from website.forms import ContactForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template
from .models import Response


# Create your views here.
class MainView(TemplateView):
    template_name = "website/main.html"
class TeamView(TemplateView):
    template_name = "website/team.html"

class GalleryView(TemplateView):
    template_name = "website/gallery.html"
class SponsView(TemplateView):
    template_name = "website/sponsors.html"
class ContactView(TemplateView):
    template_name = "website/contact.html"
def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'Name'
                , '')
            contact_email = request.POST.get(
                'Email'
                , '')
            form_content = request.POST.get('Message', '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
            context = Context({
            'Name': contact_name,
            'Email': contact_email,
            'Message': form_content,
            })
            content = template.render(context)

            a =Response()
            a.name=contact_name
            a.email=contact_email
            a.message=form_content
            a.save()


            email = EmailMessage(
            "New contact form submission",
            content,
            "Your website" + '',
            ['youremail@gmail.com'],
            headers={'Reply-To': contact_email}
            )
            email.send()
            return redirect('website:contact')

    return render(request, 'website/contact.html',{'form':form_class})