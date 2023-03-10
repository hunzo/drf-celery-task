from celery import shared_task
from celery_progress.backend import ProgressRecorder

from time import sleep

@shared_task(bind=True)
def send_to_queue(self, n):

    progress_recorder = ProgressRecorder(self)
    
    for i in range(n):
        print(f'task_id: {self.request.id} count: {i}')
        sleep(1)
        progress_recorder.set_progress(i + 1, n, f'On iteration {i}' )

    return "success"