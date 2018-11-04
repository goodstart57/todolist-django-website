from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

from .models import Schedule

from datetime import datetime


def index(request):
    context = {'schedule': Schedule.objects.all()}
    return render(request, 'scheduler/index.html', context)


@csrf_exempt
def post_schedule(request):
    if request.method=="POST":
        diff_today_start = (timezone.localtime().now() - datetime.strptime(request.POST.get("dt_start"), "%Y-%m-%d %H:%M")).total_seconds()
        diff_today_end = (timezone.localtime().now() - datetime.strptime(request.POST.get("dt_end"), "%Y-%m-%d %H:%M")).total_seconds()
        if diff_today_start<0:
            status = "Planned"
        elif diff_today_end<0:
            status = "Running"
        else:
            status = "Done"
        # 저장
        saved_obj = Schedule.objects.create(title = request.POST.get("title"),\
                                            text = request.POST.get("text"),\
                                            status = status,\
                                            dt_start = request.POST.get("dt_start"),\
                                            dt_end = request.POST.get("dt_end"),
                    )
        context = {'saved_key':saved_obj.id, 'schedule':request.POST}
    else:
        context = {'saved_key':None, 'schedule':None}
    return JsonResponse(context)