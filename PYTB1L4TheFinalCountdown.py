import time
def countdown(t):
    while t > 0:
        print(t)
        t -= 1
        time.sleep(1)
    print("BOOOOOOOOOM!")

print("How many seconds to count down?:")
seconds = input()
while not seconds.isdigit():
    print("That wasn't an number:")
    seconds = input()
seconds = int(seconds)
countdown(seconds)