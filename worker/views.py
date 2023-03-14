from rest_framework.decorators import api_view
from rest_framework.response import Response
from .tasks import send_to_queue


@api_view(["GET"])
def Home(request):
    context = {
        "home": "api worker"
    }
    return Response(context)


@api_view(["POST"])
def queue_worker(request):

    try:
        count = request.data["count"]
    except Exception as e:
        return Response(e)

    ret = send_to_queue.delay(count)

    context = {
        "task_id": ret.task_id,
        "url": f"http://localhost:8000/celery-progress/{ret.task_id}"

    }
    return Response(context)
