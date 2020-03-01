#hotword = "hey"
#
#voice_text = input('write comment with hotword: ')
#if voice_text in hotword > 0:
#    print(hotword + voice_text)
#    print(voice_text)
#    print('im ready to listen the actual query')
#if text.count(WAKE) > 0:
hotword = str("hey")
user_number = input ("Enter your number")
try:
   val = str(user_number)
   if val.count(hotword) > 0:
   #if(val > 0):
       print("User number is positive ")
   else:
       print("User number is negative ")
except ValueError:
   print("No.. input string is not a number. It's a string")
