#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glib
import os
import dbus
from dbus.mainloop.glib import DBusGMainLoop

def print_notification(bus, message):
  keys = ["app_name", "replaces_id", "app_icon", "summary",
          "body", "actions", "hints", "expire_timeout"]
  args = message.get_args_list()
  if len(args) == 8:
    notification = dict([(keys[i], args[i]) for i in range(8)])
    if all( ["PomoDoneApp" in notification["summary"], "STOP!" in notification["body"]] ):
    	os.popen('gnome-screensaver-command --lock')
    print notification["summary"], notification["body"]

loop = DBusGMainLoop(set_as_default=True)
session_bus = dbus.SessionBus()
session_bus.add_match_string("type='method_call',interface='org.freedesktop.Notifications',member='Notify',eavesdrop=true")
session_bus.add_message_filter(print_notification)

glib.MainLoop().run()