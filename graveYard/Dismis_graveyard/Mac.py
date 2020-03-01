from platform import mac_ver
@require(platform=MACOS)
@plugin('os')
def Os__MAC(jarvis, s):
    #Displays information about your operating system
    print(
        Style.BRIGHT
        + '[!] Operating System Information'
        + Style.RESET_ALL,
        Fore.BLUE)
    print('[*] Kernel: ' + sys(), Fore.GREEN)
    print('[*] Kernel Release Version: ' + release(), Fore.GREEN)
    print('[*] macOS System version: ' + mac_ver()[0], Fore.GREEN)
    for _ in architecture():
        if _ is not '':
            print('[*] ' + _, Fore.GREEN)

@require(platform=MACOS, native="pmset")
@plugin('screen off')
def screen_off__MAC(jarvis, s):
    #Turn of screen instantly
    os.system('pmset displaysleepnow')

@require(platform=MACOS, native="screenfetch")
@plugin('systeminfo')
def systeminfo__MAC(jarvis, s):
    #Display system information with distribution logo
    os.system("screenfetch")   


@require(platform=MACOS)
@plugin("update system")
def update_system__macos(jarvis, s): 
    os.system('brew upgrade && brew update')


@require(platform=MACOS)
@plugin('shutdown')
def shutdown_MACOS(jarvis, s):
    """
    Shutdown the system
    Uses:
    shutdown : asks for time
    shutdown -c : cancels shutdown
    """
    if s == '':
        s = jarvis.input('In how many minutes?: ')
    if s == '-c':
        os.system('sudo killall shutdown')
        jarvis.say('Shutdown operation cancelled')
        return
    string = 'sudo shutdown -h +' + str(s)
    os.system(string)


# Mac
def increase_volume__MAC():
    #Increases your speaker's sound.
    system(
        'osascript -e "set volume output volume '
        '(output volume of (get volume settings) + 10) --100%"'
    )

def decrease_volume__MAC():
    #Decreases your speaker's sound.
    system(
        'osascript -e "set volume output volume '
        '(output volume of (get volume settings) - 10) --100%"'
    ) 


import re
import subprocess


def get_speaker_output_volume():
    """
    Get the current speaker output volume from 0 to 100.

    Note that the speakers can have a non-zero volume but be muted, in which
    case we return 0 for simplicity.

    Note: Only runs on macOS.
    """
    cmd = "osascript -e 'get volume settings'"
    process = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True)
    output = process.stdout.strip().decode('ascii')

    pattern = re.compile(r"output volume:(\d+), input volume:(\d+), "
                         r"alert volume:(\d+), output muted:(true|false)")
    volume, _, _, muted = pattern.match(output).groups()

    volume = int(volume)
    muted = (muted == 'true')

    return 0 if muted else volume

    #
    vol = get_speaker_output_volume()
    print(f'Volume: {vol}%')
    #output = 'volume: 80%'
get_speaker_output_volume()