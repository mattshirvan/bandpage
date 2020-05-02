from django import forms


# Band contact form
class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
    
    def __repr__(self):
        return f'{self.subject} {self.message} {self.sender} {self.cc_myself}'