# from datetime import datetime
# import os
#
# from apscheduler.schedulers.background import BackgroundScheduler
# from .services import get_upcoming_matches
#
#
# def start():
#     scheduler = BackgroundScheduler()
#     scheduler.add_job(get_upcoming_matches, 'interval', minutes=2)
#     scheduler.start()