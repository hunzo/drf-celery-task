from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .tasks import send_to_queue


class WorkerApi(APIView):
    def post(self, request, *args, **kwargs):

        data = {
            "count": request.data.get("count"),
        }

        if request.data.get("count") == None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        ret = send_to_queue.delay(data["count"])

        url = "http://localhost:8000/celery-progress/"

        context = {
            "task_id": ret.task_id,
            "progress_url": f"{url}{ret.task_id}"

        }
        return Response(context)
