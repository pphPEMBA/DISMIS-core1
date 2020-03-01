#!/bin/bash
echo "############################################################# "
echo "Updating apt, preparing to install pip3, dependencies,"
echo "python3 libraries and other things to make Dismis_Home_Automation"
echo "runs perfectly for now and the future"
echo "############################################################# "
export DISMIS_HOME_AUTOMATION_SETUP_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}" )" && pwd )"
echo "DISMIS_HOME_AUTOMATION_SETPUT_DIR = $DISMIS_HOME_AUTOMATION_SETUP_DIR"
echo " "
echo "*** Installing Dependencies ***"
apt-get update #system upate
apt-get insall espeak #espeak
apt-get install python3-pip #pip3
apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0 #pyaudio
apt-get install libttspico-utils #pico2wave
#apt-get install sox libsox-fmt-all #sox
apt-get install mpg123 #mpg123
apt-get install pavucontrol #guiPulseAudio
pip3 install --upgrade google-api-python-client google-auth-httplib2 #google-auth-oauthlib #google-api-python-clients
pip3 install -r $DISMIS_HOME_AUTOMATION_SETUP_DIR/requirements.txt #Python3 Libraries
echo " "
pico2wave -w speech.wav "Hello PEMBA, please reconfigure m p g one two three volume at 30 percent in PulseAudio Control. Now opening PulseAudio Control application" && aplay speech.wav && rm speech.wav
mpg123 $DISMIS_HOME_AUTOMATION_SETUP_DIR/.volReconfigure_MPG123.mp3
pavucontrol
mkdir $DISMIS_HOME_AUTOMATION_SETUP_DIR/backup
now=.$(date +"%T")
mkdir $DISMIS_HOME_AUTOMATION_SETUP_DIR/backup/$now
echo "Making Backup of .profile .bashrc"
cp -r ~/.profile $DISMIS_HOME_AUTOMATION_SETUP_DIR/$now/.profile
cp -r ~/.bashrc $DISMIS_HOME_AUTOMATION_SETUP_DIR/$now/.bashrc
#cp -r ~/.profile ~/.profile.backup
#cp -r ~/.bashrc ~/.bashrc.backup
echo "Now coping .bashrc .profile .D-Slave1_banner.py to ~/ directory"
cp -r $DISMIS_HOME_AUTOMATION_SETUP_DIR/.bashrc $DISMIS_HOME_AUTOMATION_SETUP_DIR/.profile $DISMIS_HOME_AUTOMATION_SETUP_DIR/.D-Slave1_banner.py ~/
echo "Creating Dismis_Home_Automation and coping files from source to Dismis_Home_Automation"
mkdir -p ~/.Dismis_Home_Automation
pkill mpg123
cd ..
DISMIS_HOME_AUTOMATION_DIR=$(pwd)
echo "DISMIS_HOME_AUTOMATION_DIR = "$DISMIS_HOME_AUTOMATION_DIR
cp -a $DISMIS_HOME_AUTOMATION_DIR/. ~/.Dismis_Home_Automation/
echo " "
echo " Installing of Dismis-HA Accomplished! "
echo "____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________"
echo " "
echo " "
echo " "
echo " "
echo "Do you want to reboot or run Dismis_Home_Automation --without-reboot"
echo " "
echo "type ' Y ' if you want to reboot the system"
echo "type ' N ' if you want to run Dismis_Home_Automation without reboot"
while true; do
    read -p "Do you wish to install this program?" yn
    case $yn in
        [Yy]* ) echo "rebooting the system"; reboot;;
        [Nn]* ) echo "\t\t\t\t\t Now Running Dismis-Home_Automation"
                cd ~/.Dismis_Home_Automation/
                python3 DISMIS-HA.py; break;;
        * ) echo "Please answer y or n.";;
    esac
done