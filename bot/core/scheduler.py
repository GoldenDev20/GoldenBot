# bot/core/scheduler.py

from apscheduler.schedulers.asyncio import AsyncIOScheduler

class TaskScheduler:
    def __init__(self):
        self.scheduler = AsyncIOScheduler()

    def start(self):
        self.scheduler.start()

    def add_task(self, func, trigger, **kwargs):
        self.scheduler.add_job(func, trigger, **kwargs)
