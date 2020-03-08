#!/bin/bash
echo "############################################################# "
echo "Updating apt, preparing to install pip3, dependencies,"
echo "python3 libraries and other things to make Dismis"
echo "runs perfectly for now and the future"
echo "############################################################# "
pico2wave -w speech2.wav "Hello boss, its my honor to serve you. The Completion of Dismis setup takes maximum 10 times till that you can sit and chill. Thank you!" && aplay speech2.wav && rm speech2.wav
export DISMIS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}" )" && pwd )"
echo "DISMIS_SETPUT_DIR = $DISMIS_DIR"
echo " "
echo "*** Installing Dependencies ***"
apt-get update #system upate
apt install tesseract-ocr # install tesseract is used for extracting text from image
apt-get insall espeak #espeak
apt-get install gnome-tweaks
apt-get install python3-pip #pip3
apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0 #pyaudio
apt-get install libttspico-utils #pico2wave
#apt-get install sox libsox-fmt-all #sox
apt-get install mpg123 #mpg123
apt-get install pavucontrol #guiPulseAudio
pip3 install --upgrade google-api-python-client google-auth-httplib2 #google-auth-oauthlib #google-api-python-clients
pip3 install -r $DISMIS_DIR/requirements.txt #Python3 Libraries
echo " "
pico2wave -w speech1.wav "I've already install tweaks. Open tweaks and on the right side bar you'll find Power, click on it then turn off Suspend When Laptop Lid Is Close." && aplay speech1.wav && rm speech1.wav
# sleep for 5 seconds
sleep 15
echo " "
pico2wave -w speech.wav "Hello PEMBA, please reconfigure m p g one two three volume at 30 percent in PulseAudio Control. Now opening PulseAudio Control application" && aplay speech.wav && rm speech.wav
mpg123 $DISMIS_DIR/.volReconfigure_MPG123.mp3
pavucontrol
mkdir $DISMIS_DIR/backup
now=.$(date +"%T")
mkdir $DISMIS_DIR/backup/$now
echo "Making Backup of .profile .bashrc"
cp -r ~/.profile $DISMIS_DIR/$now/.profile
cp -r ~/.bashrc $DISMIS_DIR/$now/.bashrc
#cp -r ~/.profile ~/.profile.backup
#cp -r ~/.bashrc ~/.bashrc.backup
echo "Now coping .bashrc .profile .D-Slave1_banner.py to ~/ directory"
cp -r $DISMIS_DIR/.bashrc $DISMIS_DIR/.profile $DISMIS_DIR/.D-Slave1_banner.py ~/
echo "Creating Dismis and coping files from source to Dismis"
mkdir -p ~/.Dismis
pkill mpg123
cd ..
DISMIS_DIR=$(pwd)
echo "DISMIS_DIR = "$DISMIS_DIR
cp -a $DISMIS_DIR/. ~/.Dismis/
echo " "
echo " Installing of Dismis Accomplished! "
echo "____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________"
echo " "
echo " "
echo " "
echo " "
echo "Do you want to reboot or run Dismis --without-reboot"
echo " "
echo "type ' Y ' if you want to reboot the system"
echo "type ' N ' if you want to run Dismis without reboot"
while true; do
    read -p "Do you wish to install this program?" yn
    case $yn in
        [Yy]* ) echo "rebooting the system"; reboot;;
        [Nn]* ) echo "\t\t\t\t\t Now Running Dismis-Home_Automation"
                cd ~/.Dismis/
                python3 DISMIS.py; break;;
        * ) echo "Please answer y or n.";;
    esac
done






