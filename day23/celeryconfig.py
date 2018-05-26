#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/26 10:32
# @Author  : yangyuanqiang
# @File    : celeryconfig.py



from kombu import Exchange,Queue

BROKER_URL = "redis://192.168.3.11:6379/1"
CELERY_RESULT_BACKEND = "redis://192.168.3.11:6379/2"

CELERY_QUEUES = (
Queue("default",Exchange("default"),routing_key="default"),
Queue("for_task_A",Exchange("for_task_A"),routing_key="for_task_A"),
Queue("for_task_B",Exchange("for_task_B"),routing_key="for_task_B")
)

CELERY_ROUTES = {
'tasks.taskA':{"queue":"for_task_A","routing_key":"for_task_A"},
'tasks.taskB':{"queue":"for_task_B","routing_key":"for_task_B"}
}
