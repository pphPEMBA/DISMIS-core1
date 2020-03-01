#Window

@require(platform=WINDOWS)
@plugin('systeminfo')  
def systeminfo_win(jarvis, s):  #windows
    #Display system infomation
    os.system("systeminfo")

@require(platform=WINDOWS) 
@plugin("check ram")
def check_ram__WINDOWS(jarvis, s):  #Windows

    #checks your system\'s RAM stats. -- Examples: check ram

    import psutil
    mem = psutil.virtual_memory()

    def format(size):
        mb, _ = divmod(size, 1024 * 1024)
        gb, mb = divmod(mb, 1024)
        return "%s GB %s MB" % (gb, mb)
    print("Total RAM: %s" % (format(mem.total)), Fore.BLUE)
    if mem.percent > 80:
        color = Fore.RED
    elif mem.percent > 60:
        color = Fore.YELLOW
    else:
        color = Fore.GREEN
    print("Available RAM: %s" % (format(mem.available)), color)
    print("RAM used: %s%%" % (mem.percent), color)


@require(platform=WINDOWS)
@plugin('shutdown')
def shutdown_WIN32(jarvis, s):
    """
    Shutdown the system
    Uses:
    shutdown : asks for time
    shutdown -c : cancels shutdown
    """
    if s == '':
        s = jarvis.input('In how many seconds?: ')
    if s == '-c':
        os.system('shutdown /a')
        jarvis.say('Shutdown operation cancelled')
        return
    string = 'sudo shutdown /s /t ' + str(s)
    os.system(string)




@require(platform=MACOS)
@plugin('reboot')
def reboot_MACOS(jarvis, s):
    """Reboot the system"""
    string = 'sudo shutdown -r now'
    os.system(string)


@require(platform=WINDOWS)
@plugin('reboot')
def reboot_WIN32(jarvis, s):
    """Reboot the system"""
    if s == '':
        s = jarvis.input('In how many seconds?: ')
    string = 'shutdown /r /t ' + str(s)
    os.system(string)





@require(platform=WINDOWS)
@plugin('hibernate')
def hibernate_WIN32(jarvis, s):
    """Hibernates the system"""
    string = 'shutdown /h'
    os.system(string)





@require(platform=WINDOWS)
@plugin('hybridsleep')
def hybridsleep_WIN32(jarvis, s):
    """Performs shutdown and prepares forfast startup"""
    string = 'shutdown /hybrid'
    os.system(string)


@require(platform=WINDOWS)
@plugin('log off')
def log_off_WIN32(jarvis, s):
    """Log off the system"""
    string = 'shutdown /l'
    os.system(string)
