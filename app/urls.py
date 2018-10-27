from django.urls import path
import dappstore.event_watcher
from . import views
from threading import Thread

app_name = "app"

urlpatterns = [
    path("", views.home, name="home"),
    path("feedback/<str:name>", views.feedback, name="feedback"),
]

thread = Thread(target=dappstore.event_watcher.loop)
thread.daemon = True
thread.start()
