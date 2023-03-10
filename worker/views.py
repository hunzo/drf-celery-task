from django.http import JsonResponse
from .tasks import send_to_queue

# Create your views here.

def Home(request):
    return JsonResponse({
        "example": "django celery task"
    })

def CreateTask(request):

    ret = send_to_queue.delay(10)
    print(ret)
    context = {
        "task_id": ret.task_id,
        "url": f"http://localhost:8000/celery-progress/{ret.task_id}"
    }

    return JsonResponse(context)
