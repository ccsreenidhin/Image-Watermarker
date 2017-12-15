from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import user_passes_test, login_required
from django.conf import settings

from .models import Document
from .forms import DocumentForm
import glob, os

###### For image processing ###########
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from django.core.files.base import ContentFile
import StringIO



def index(request):
    return render(request, 'index.html',{})



def about(request):
    return render(request, 'about.html',{})



def gallery(request):
    documents = []
    documents = Document.objects.all()
    return render(request, 'gallery.html', {'documents': documents})


@login_required
def wmarked(request):
    watermkd = Document.objects.filter(user=request.user, user__is_active = True)
    return render(request, 'wmarked.html', {'watermkd':watermkd})


def watermark(imagin, writes, x, y, color, size):
    fontsize = int(size)
    img = Image.open(imagin)
    img_io = StringIO.StringIO()
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(settings.MEDIA_ROOT+'/font/arial.ttf', fontsize)
    draw.text((x, y),writes,(color),font=font)
    img.seek(0)
    img.save(img_io, "jpeg")
    img_content = ContentFile(img_io.getvalue(), 'img5.jpg')
    return img_content


@login_required
def upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
	    document.user = request.user
	    document.dupimage = watermark(imagin = document.orimage, writes = document.text, x = document.x, y = document.y, color = document.color, size = document.fontsize)
	    document.save()
        return HttpResponseRedirect(reverse('wmarked'))
    else:
        form = DocumentForm()
    return render(request, 'upload.html', { 'form': form,})

