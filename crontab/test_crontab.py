
from crontab import CronTab

cron = CronTab(user=True)

for job in cron:
    print(job)

for line in cron.lines:
    print(line)
