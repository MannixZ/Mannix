#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@time: 2019/4/2 19:50

@author: ZMJ

@file: Locust.py

'''

from locust import HttpLocust, TaskSet, task

class WebsiteTasks(TaskSet):
    @task
    def index(self):
        self.client.get("/")

class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    min_wait = 5000
    max_wait = 15000