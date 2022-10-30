export VIMINIT="set nocp | source ${XDG_CONFIG_HOME:-$HOME/.config}/vim/vimrc"
export QT_QPA_PLATFORMTHEME="qt5ct"
if [ -z "${DISPLAY}" ] && [ "${XDG_VTNR}" -eq 1 ]; then 
<<<<<<< HEAD
	sudo nmcli device connect wlan0 &
	exec startx
=======
	exec cd
	exec xinit
>>>>>>> 81e93048a384aa5f8d72948bafaaa4af35a4d707
fi
