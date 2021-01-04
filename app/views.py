from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django import forms
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os


class FileUploadForm(forms.Form):
    file_source = forms.FileField()


def ajax_upload(request):
    if request.method == 'POST':
        form = FileUploadForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            if request.POST['directory']:
                directory = request.POST['directory']
            else:
                directory = "base"
            file = request.FILES['file_source']
            if format_check(file.name):
                fs = FileSystemStorage()
                if fs.exists('uploads/' + directory + '/' + file.name):
                    return JsonResponse({'error': True, 'errors': ['فایل با این نام وجود دارد']})
                else:
                    fs.save('uploads/' + directory + '/' + file.name, file)
                return JsonResponse({'error': False, 'message': 'Uploaded Successfully',
                                     'file-path': settings.MEDIA_URL + 'uploads/' + directory + '/' + file.name})
            else:
                return JsonResponse({'error': True, 'errors': ['فرمت فایل باید jpg ویا png  باشد']})
        else:
            return JsonResponse({'error': True, 'errors': form.errors})

    return HttpResponseRedirect("/")


def format_check(file):
    name, ext = os.path.splitext(file)
    if ext in settings.ALLOWED_FILE_FORMATS:
        return True


def delete_file(request, directory, id):
    try:
        print(id)
        os.remove('media/uploads/' + directory + '/' + id)
        return JsonResponse({'error': False, 'message': 'file have been deleted'})
    except:
        return JsonResponse({'error': True, 'errors': 'some thing went wrong'})

    return HttpResponseRedirect("/")
