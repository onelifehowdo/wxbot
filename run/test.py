import time
week = time.strftime('%a', time.localtime())
hor=int(time.strftime('%H', time.localtime()))
print(week)
print(hor)
if not week in ["Sat", "Sun"]:
    # 非工作日
    pass
else:
    pass
