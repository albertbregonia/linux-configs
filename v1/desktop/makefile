.PHONY: default desktop apps lang aur snap wifi opencv audio clean
default: desktop apps lang aur

desktop: # xset s off -> disable screen timeout
	sudo pacman -S xorg-server xorg-xinit xorg-xrandr xorg-xprop qtile noto-fonts noto-fonts-cjk noto-fonts-emoji ttf-roboto nvidia

apps:
	sudo pacman -S git unzip cmake lxappearance pulseaudio pulseaudio-bluetooth alsa-utils bluez bluez-utils pavucontrol alacritty firefox thunar thunar-volman gvfs spectacle virtualbox vlc tigervnc # repo 2 for virtualbox
	sudo modprobe vboxdrv # might need this for virtualbox
lang:
	sudo pacman -S npm jdk-openjdk python-pip openssl openssh # c/c++/python is already installed, install java, pip, nodejs, TLS and SSH
	curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
	pip install psutil

mcu: # tinygo and AVR compiler/libs
	sudo pacman -S avr-gcc avr-libc avrdude tinygo 

aur:
	# install snapd
	cd ~
	git clone https://aur.archlinux.org/snapd.git
	git clone https://aur.archlinux.org/consolas-font.git
	git clone https://aur.archlinux.org/picom-jonaburg-git.git
	git clone https://aur.archlinux.org/minecraft-launcher.git
	
	cd ~/snapd && makepkg -si
	systemctl enable --now snapd.socket
	sudo ln -s /var/lib/snapd/snap /snap # classic support

	#install desired apps
	cd ~/consolas-font && makepkg -si

	cd ~/picom-jonaburg-git && makepkg -si

	cd ~/minecraft-launcher && makepkg -si

snap:
	sudo snap install code --classic
	sudo snap install discord
	sudo snap install slack --classic
	sudo snap install spotify

wifi:
	nmcli d wifi connect BREGONIA password albertbregonia4173

opencv:
	sudo pacman -Syyu
	sudo pacman -S opencv fmt hdf5 glew pugixml protobuf openmpi vtk
	
audio: # i need to do this for my hp spectre's audio to work
	sof-firmware # sof-firmware is for detecting audio driver
	sudo echo 'blacklist snd_hda_intel' > /etc/modprobe.d/blacklist.conf
	sudo echo 'blacklist snd_soc_skl' >> /etc/modprobe.d/blacklist.conf

clean:
	rm -rf consolas-font/ snapd/ picom-jonaburg-git/ minecraft-launcher/
