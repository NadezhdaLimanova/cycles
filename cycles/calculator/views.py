import datetime
from datetime import timedelta, datetime
from django.shortcuts import render


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










