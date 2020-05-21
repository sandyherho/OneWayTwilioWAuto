from apscheduler.schedulers.blocking import BlockingScheduler
from family import send_news

# Start the scheduler
sched = BlockingScheduler()


# Schedule job_function to be called every ten seconds
sched.add_job(send_news, "interval", hours=24)

sched.start()
