FROM nginx:1.13

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN mkdir -p /data/nginx/cache
COPY default.conf /etc/nginx/conf.d
