from django.core.mail import send_mail
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic.edit import FormView
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from django.core.urlresolvers import reverse_lazy
from django.template import loader
from rest_framework.response import Response
from main.permissions import PublicEndpoint

from main.forms import ContactForm
from aroma.models import Aroma
from main.serializers import UpdatedAromasListSerializer, NewCommentsListSerializer
from activity.models import Comment


def tos(request):
    return render(request, 'tos.html')


class ContactView(SuccessMessageMixin, FormView):
    form_class = ContactForm
    template_name = 'contact/contact_form.html'
    success_message = 'Ваше обращение было успешно отправлено'
    success_url = reverse_lazy('contacts')

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            html_message = loader.render_to_string(form.html_email_template_name, self.get_context_data())
            send_mail(form.subject, request.POST.get('msg'), form.from_email, [form.to_email],
                      html_message=html_message)
        return super(ContactView, self).post(request, *args, **kwargs)


class HomePageView(generics.GenericAPIView):
    template_name = 'home/layout.html'
    queryset = Aroma.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = (PublicEndpoint,)

    def get(self, request, *args, **kwargs):
        context = {"request": request}
        updated_aromas = Aroma.objects.filter(guise__isnull=False).order_by('-updated_at')[:3]
        aromas_serializer = UpdatedAromasListSerializer(updated_aromas, many=True, context=context)
        new_comments = Comment.objects.all().order_by('-created_at')[:3]
        comments_serializer = NewCommentsListSerializer(new_comments, many=True, context=context)
        r = {'updated_aromas': aromas_serializer.data, 'new_comments': comments_serializer.data}
        return Response(r, template_name='home/layout.html')


