import time
from playsound import playsound

def focus_timer(minutes):
    start_time = time.time()
    end_time = start_time + minutes * 60

    while time.time() < end_time:
        time_left = int(end_time - time.time())
        print("Time left:", time_left // 60, "minutes", time_left % 60, "seconds\r", end="")
        time.sleep(1)

    playsound('path/to/sound/file.mp3') #替换成提示音文件的路径
    print("Time's up! Good job!")
    
if __name__ == "__main__":
    focus_timer(25) # 25分钟专注时间
