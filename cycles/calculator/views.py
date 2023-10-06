import datetime
from datetime import date, timedelta, datetime
import os

from django.http import HttpResponse
from django.shortcuts import render, reverse


def process_input(request):

    if request.method == 'POST':
        try:
            day = str(request.POST.get('day'))
            longing = int(request.POST.get('longing'))
            months = int(request.POST.get('months'))

            cycles_dict = {}

            for i in range(months):
                day_format = datetime.strptime(day, '%d.%m.%Y')
                first_month_result = day_format + timedelta(days=longing * i)
                first_month = datetime.strftime(first_month_result, '%d.%m.%Y')
                cycles_dict[i] = first_month

            context = {
                'cycles_dict': cycles_dict
            }

            return render(request, 'cycles_result.html', context)
        except ValueError:
            error_message = 'Ошибка, неправильно введены данные'
            context = {
                'error_message': error_message
            }
            return render(request, 'cycles_result.html', context)
    return render(request, 'cycles_2.html')











# def home_view(request):
#     template_name = 'app/home.html'
#     pages = {
#         'Главная страница': reverse('home'),
#         'Показать текущее время': reverse('time'),
#         'Показать содержимое рабочей директории': reverse('workdir'),
#     }
#
#     # context и параметры render менять не нужно
#     # подробнее о них мы поговорим на следующих лекциях
#     context = {
#         'pages': pages
#     }
#     return render(request, template_name, context)
#
#
# def time_view(request):
#     current_time = datetime.datetime.now()
#     msg = f'Текущее время: {current_time}'
#     return HttpResponse(msg)
#
#
# def workdir_view(request):
#     path = '.'
#     result = sorted(os.listdir(path))
#     msg = f'Список файлов в рабочей директории: {result}'
#     return HttpResponse(msg)
#     raise NotImplemented