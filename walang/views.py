from django.shortcuts import render
from django.views.generic import TemplateView, View
from .forms import ImageUploadForm
from django.http import HttpResponse


# Create your views here.
class WalangHomeView(TemplateView):
    template_name = "walang/home.html"

    def get_context_data(self, *args):
        return super(WalangHomeView, self).get_context_data(*args)


#Image upload
class ImageUploadView(View):

    def post(self, request, **kwargs):
        imageform = ImageUploadForm(data=self.request.POST or None, files=self.request.FILES or None, instance=self.request.user.person)

        image_source = False
        if imageform.is_valid():
            person = imageform.save()
            image_source = person.image.url
        else:
            print imageform.errors

        return HttpResponse(image_source)
