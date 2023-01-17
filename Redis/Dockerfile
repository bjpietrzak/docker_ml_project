FROM redis:7

RUN apt-get update && apt-get install redis-tools -y

RUN echo "0 0 * * * redis-dump -u redis > /data/backup.rdb" >> /etc/crontab