.PHONY: default desktop apps lang aur snap wifi clean
default: desktop apps lang aur snap

desktop:
	sudo pacman -S xorg-server xorg-xinit xorg-xrandr xorg-xprop qtile noto-fonts noto-fonts-cjk noto-fonts-emoji ttf-roboto nvidia 	

apps:
	sudo pacman -S git unzip lxappearance pulseaudio bluez pavucontrol alacritty firefox thunar spectacle 

lang:
	sudo pacman -S npm jdk-openjdk python-pip
	curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
	pip install psutil

aur:
	# install snapd
	cd ~
	git clone https://aur.archlinux.org/snapd.git
	git clone https://aur.archlinux.org/consolas-font.git
	git clone https://aur.archlinux.org/picom-jonaburg-git.git
	git clone https://aur.archlinux.org/minecraft-launcher.git
	
	cd ~/snapd && makepkg -si
	systemctl enable --now snapd.socket
	sudo ln -s /var/lib/snapd/snap /snap #classic support

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

clean:
	rm -rf consolas-font/ snapd/ picom-jonaburg-git/ minecraft-launcher/
