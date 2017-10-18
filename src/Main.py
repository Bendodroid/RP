#!/usr/bin/env python3.5

# Copyright Bendodroid [2017]


import tc
import Engine.EventLoop
import File_Handler as FH

tc.reload_ui(FH.loadbasics())

Engine.EventLoop.EventLoop().run()
