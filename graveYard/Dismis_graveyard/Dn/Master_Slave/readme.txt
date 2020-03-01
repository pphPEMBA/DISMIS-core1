Shutdown and Reboot fuction works properly other don't.



from socket import gaierror
except (gaierror, ConnectionRefusedError):
  # tell the script to report if your message was sent or which errors need to be fixed
  print('Failed to connect to the server. Bad connection settings?')