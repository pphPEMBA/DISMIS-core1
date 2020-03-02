import time
def delay_print(s):
    import sys
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)
delay_print("Hi, I'm Dismis. Nice to meet you!\n")
time.sleep(0.20)

