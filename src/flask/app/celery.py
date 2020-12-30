from celery import Celery

from . import create_celery_app

include = [
    'app.functions',
]


def make_celery(app):
    celery = Celery('app', broker=app.config["CELERY_BROKER_URL"], backend=app.config["CELERY_RESULT_BACKEND"],
                    include=include)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery

flask = create_celery_app()
celery = make_celery(flask)

if __name__ == "__main__":
    flask.app_context().push()
    celery.start()
