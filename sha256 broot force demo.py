import time
import hashlib

loopCounter = 0
for i in range(100000,999999):
    H = hashlib.sha256(str(i).encode("utf-8")).hexdigest()
    print("possible bin: " + str(i) + " corseponding sha256 hash: " + H)
    loopCounter = +1
    if H == "53c924604b15a3a0711f02aa818bd639984e58e69cf86ca440b1b41eb0818678":
        print("it's a match!")
        time.sleep(100)
        break 