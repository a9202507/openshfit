from apscheduler.schedulers.blocking import BlockingScheduler
import requests


# 定義排程 : 在周一至周五，每 20 分鐘就做一次 def scheduled_jog()
sched = BlockingScheduler()


@sched.scheduled_job('cron', day_of_week='mon-sun', minute='*/28')
def scheduled_job():
    # 宣告一個排程
    sched = BlockingScheduler()
    url_str = "http://oc12-web-efficiency.ap-sg-1.icp.infineon.com/api/tasks"
    connect = requests.get(url_str)


if __name__ == "__main__":
    scheduled_job()
    sched.start()  # 啟動排程
