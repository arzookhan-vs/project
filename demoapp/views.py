from django.conf import settings
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from demoapp.models import Demo
from django.contrib import messages

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def index (request):
  submit_form(request)        
  return render(request, 'index.html')

def submit_form(request):
  def getResult(text):
    return 'Your input text was [{}]'.format(text)

  if request.method == 'POST':
    emailTo = request.POST.get('email')
    text = request.POST.get('text')

    if emailTo and text:
      results = getResult(text)
      htmlMessage = render_to_string('emailTemplate.html', {'text': text, 'result': results})
      textMessage = strip_tags(htmlMessage)
      email = EmailMultiAlternatives(
          "Here's your result",
          textMessage,
          'Demo 📨 <' + settings.EMAIL_HOST_USER + '>',
          [emailTo]
      )
      email.attach_alternative(htmlMessage, 'text/html')
      
      demo = Demo(
          email=emailTo,
          text=text,
          result=results,
          date=timezone.now()
      )
      
      demo.save()
      email.send()
      
      messages.success(request, 'Submitted successfully!')
      
    else:
      messages.warning(request, 'Please fill all fields!')

    return HttpResponseRedirect(reverse('demo'))
