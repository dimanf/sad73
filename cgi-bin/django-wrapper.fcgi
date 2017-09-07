#!/home/u26831/python/bin/python
# -*- coding: utf-8 -*-
import sys, os

# Add a custom Python path.
sys.path.insert(0, "/home/u26831/detsky-sad73.ru/tg")

# Switch to the directory of your project. (Optional.)
# os.chdir("/home/u26831/detsky-sad73.ru/tg")

# Set the DJANGO_SETTINGS_MODULE environment variable.
os.environ['DJANGO_SETTINGS_MODULE'] = "settings"

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="prefork", daemonize="false",
    minspare=1, maxspare=1, maxchildren=1)
