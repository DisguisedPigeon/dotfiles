export VIMINIT="set nocp | source ${XDG_CONFIG_HOME:-$HOME/.config}/vim/vimrc"
export QT_QPA_PLATFORMTHEME="qt5ct"
if [ -z "${DISPLAY}" ] && [ "${XDG_VTNR}" -eq 1 ]; then 
	sudo nmcli device connect wlan0 &
	exec startx
fi
