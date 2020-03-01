import time
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def decrypt(msg):
    off = 3
    dec = ""
    for i in msg:
        try:
            dec = dec + a[int((a.index(i)-off)) % 26]
        except ValueError:
            dec += i
    return dec


# Client Side(Receiver)
f = open('server.txt', 'r+')
msg = f.read()
print("Message received is   : %s " % msg)
print()
print("Decrypting...")
time.sleep(2)
dec = decrypt(msg)
print("Decrypted message     : %s " % dec)

