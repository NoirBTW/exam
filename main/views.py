from django.shortcuts import render
from .models import asexam

# Create your views here.

def asexam_list(request):
    exams = asexam.objects.filter(is_public=True).select_related().prefetch_related('users')
    return render(request, 'main/asexam_list.html', {
        'exams': exams,
        'fio': 'Смирнов Александр Сергеевич',
        'group': '231-323',
    })
