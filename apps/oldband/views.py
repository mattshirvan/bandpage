from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView
from django.core.mail import send_mail
from .forms import ContactForm
from django.contrib import messages


# Band homepage.
class IndexView(TemplateView):
    template_name = "oldband/index.html"


# Band About page
class AboutView(TemplateView):
    template_name = "oldband/about.html"


# Band discrography page
class DiscographyView(TemplateView):
    template_name = "oldband/discography.html"


# Band tour page
class TourView(TemplateView):
    template_name = "oldband/tour.html"


# Band videos page
class VideoView(TemplateView):
    template_name = "oldband/video.html"


# Band games page
class GameView(TemplateView):
    template_name = "oldband/game.html"


# Band contact form page
class ContactView(TemplateView):
    form_class = ContactForm
    initial = {'key': 'value'}
    template_name = "oldband/contact.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['reficulmusic@gmail.com']
            if cc_myself:
                recipients.append(sender)

            send_mail(subject, message, sender, recipients)
            messages.add_message(request, messages.INFO, "Thanks for contacting us!")
            return redirect(reverse("oldband:contact"))