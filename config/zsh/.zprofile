if [ -z "${DISPLAY}" ] && [ "${XDG_VTNR}" -eq 1 ]; then 
	exec cd
	exec xinit
fi
