# https://www.youtube.com/watch?v=SqvVm3QiQVk&t=1992s
import time


def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02}'.format(mins, secs)
        print(timer, end="\n")
        time.sleep(1)
        t -= 1
    print("Timer completed!")


t = int(input("Enter the time in seconds: "))
countdown(t)
