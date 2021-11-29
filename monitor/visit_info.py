from .models import *
from django.utils import timezone


def change_info(request):       # Модифицировать информацию, такую ​​как посещаемость сайта и IP
    # Для каждого посещения добавьте 1 к общему количеству посещений.
    count_nums = VisitNumber.objects.filter(id=1)   
    if count_nums:
        count_nums = count_nums[0]
        count_nums.count += 1
    else:
        count_nums = VisitNumber()
        count_nums.count = 1
    count_nums.save()

    # Запишите количество посещений ip и каждого ip
    if 'HTTP_X_FORWARDED_FOR' in request.META:  # Получить IP
        client_ip = request.META['HTTP_X_FORWARDED_FOR']
        client_ip = client_ip.split(",")[0]  # Так вот настоящий айпи
    else:
        client_ip = request.META['REMOTE_ADDR']  # Получить IP прокси здесь
    # print(client_ip)

    ip_exist = Userip.objects.filter(ip=str(client_ip))
    if ip_exist:  # Определить, существует ли ip
        uobj = ip_exist[0]
        uobj.count += 1
    else:
        uobj = Userip()
        uobj.ip = client_ip
        uobj.count = 1
    uobj.save()

    # Увеличение сегодняшних посещений
    date = timezone.now().date()
    today = DayNumber.objects.filter(day=date)
    if today:
        temp = today[0]
        temp.count += 1
    else:
        temp = DayNumber()
        temp.dayTime = date
        temp.count = 1
    temp.save()