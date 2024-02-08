import time
import datetime

import os

# 读取环境变量中的 finalday 变量
finalday_var = os.getenv("finalday")

if finalday_var:
    d = 8
else :
    d = 9

def get_time():
    return (time.time() - datetime.datetime(2024, 2, d, 11, 0, 0, 0).timestamp())