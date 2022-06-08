import time

print("[현재시각]", time.strftime("%H:%M:%S"))
alarm_time = input("알람 시각 : ")
alarm_hms = alarm_time.split(':')
if len(alarm_hms) == 3 and 0 <= int(alarm_hms[0]) \
    and 0 <= int(alarm_hms[1]) < 60 and 0 <= int(alarm_hms[2]) < 60:
    time.sleep(int(alarm_hms[0]) * 60 * 60 \
        + int(alarm_hms[1]) * 60 + int(alarm_hms[2]))
    print("Beep!")
else:
    print("입력한 알람 시각 표기에 오류가 있습니다.")
