# Описание репозитория

- content - директория с статическими файлами (на машине хранится в /home/Stifeev/LR2/content);

- unicorn - Python-исходники для бэкенд-сервера;

- default - файл конфигурации nginx (на машине хранится в /etc/nginx/sites-available);

- nginx.conf - файл конфигурации nginx (хранится в /etc/nginx)

  Если требует запуск исходников на вашей машине, то необходимо убедиться в существовании указанных выше файлов в нужных директориях.

# Замеры производительности с помощью утилиты ab

## Отдача статики

$ ab -n 10 -c 2 -t 1 -v 2 http://192.168.31.211/public/index.html

Finished 1062 requests


Server Software:        nginx/1.10.3
Server Hostname:        192.168.31.211
Server Port:            80

Document Path:          /public/index.html
Document Length:        388 bytes

Concurrency Level:      2
Time taken for tests:   1.001 seconds
Complete requests:      1062
Failed requests:        0
Total transferred:      669060 bytes
HTML transferred:       412056 bytes
Requests per second:    1060.59 [#/sec] (mean)
Time per request:       1.886 [ms] (mean)
Time per request:       0.943 [ms] (mean, across all concurrent requests)
Transfer rate:          652.51 [Kbytes/sec] received

Connection Times (ms)

|             | min  | mean | [+/-sd] | median | max  |
| ----------- | ---- | ---- | ------- | ------ | ---- |
| Connect:    | 0    | 0    | 0.4     | 0      | 2    |
| Processing: | 1    | 1    | 0.4     | 1      | 3    |
| Waiting:    | 0    | 0    | 0.4     | 0      | 2    |
| Total:      | 1    | 2    | 0.3     | 2      | 3    |

Percentage of the requests served within a certain time (ms)

50%      2

66%      2

75%      2

80%      2

90%      2

95%      2

98%      3

99%      3

100%      3 (longest request)

## Бэкенд сервер unicorn напрямую

$ ab -n 10 -c 2 -t 1 -v 2 http://localhost:8000/

Finished 1214 requests

Server Software:        gunicorn
Server Hostname:        localhost
Server Port:            8000

Document Path:          /
Document Length:        54 bytes

Concurrency Level:      2
Time taken for tests:   1.001 seconds
Complete requests:      1220
Failed requests:        0
Total transferred:      235460 bytes
HTML transferred:       65880 bytes
Requests per second:    1219.04 [#/sec] (mean)
Time per request:       1.641 [ms] (mean)
Time per request:       0.820 [ms] (mean, across all concurrent requests)
Transfer rate:          229.76 [Kbytes/sec] received

Connection Times (ms)
|             | min  | mean | [+/-sd] | median | max  |
| ----------- | ---- | ---- | ------- | ------ | ---- |
| Connect:    |   0  |  0  | 0.9      |0      |15    |
| Processing: | 1    |1  | 0.4     | 1   |   12    |
| Waiting:    | 0   | 1  | 0.4   |   1    |  11    |
| Total:      |  1  |  2 |  1.1    |  1   |   18    |

Percentage of the requests served within a certain time (ms)

50%      1

66%      1

75%      2

80%      2

90%      2

95%      2

98%      2

99%      3

100%     18 (longest request)

## Бэкенд сервер unicorn через проксирование в nginx

$ ab -n 10 -c 2 -t 1 -v 2 http://192.168.31.211/backend/

Finished 959 requests


Server Software:        nginx/1.10.3
Server Hostname:        192.168.31.211
Server Port:            80

Document Path:          /backend/
Document Length:        54 bytes

Concurrency Level:      2
Time taken for tests:   1.001 seconds
Complete requests:      959
Failed requests:        0
Total transferred:      197760 bytes
HTML transferred:       51840 bytes
Requests per second:    958.42 [#/sec] (mean)
Time per request:       2.087 [ms] (mean)
Time per request:       1.043 [ms] (mean, across all concurrent requests)
Transfer rate:          193.01 [Kbytes/sec] received

Connection Times (ms)
|             | min  | mean | [+/-sd] | median | max  |
| ----------- | ---- | ---- | ------- | ------ | ---- |
| Connect:    |   0  |  0  | 0.6    |  0   |   16    |
| Processing: | 1  |  2 |  1.3   |   2   |   18    |
| Waiting:    | 1  |  1  | 1.1  |    1   |   16    |
| Total:      |  1  |  2 |  1.6  |    2  |    19    |

Percentage of the requests served within a certain time (ms)

50%      2

66%      2

75%      2

80%      2

90%      2

95%      2

98%      7

99%     11

100%    19 (longest request)
