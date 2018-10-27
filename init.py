import os
os.environ["DJANGO_SETTINGS_MODULE"] = "dappstore.settings"

import django
django.setup()
from app.models import State

d = State(key="block", value=0)
d.save()