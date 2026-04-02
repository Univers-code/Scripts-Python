#!/bin/bash

#Automatizacion de escaneos via bash.

# Colores (si estás en TTY)
RED="$(tput setaf 1)"
BOLD="$(tput bold)"
RESET="$(tput sgr0)"

echo
echo "${RED}${BOLD}"
cat <<'BANNER'
   _____                                   _   _ __  __          _____  
  / ____|                                 | \ | |  \/  |   /\   |  __ \ 
 | (___   ___ __ _ _ __  _ __   ___ _ __  |  \| | \  / |  /  \  | |__) |
  \___ \ / __/ _` | '_ \| '_ \ / _ \ '__| | . ` | |\/| | / /\ \ |  ___/ 
  ____) | (_| (_| | | | | | | |  __/ |    | |\  | |  | |/ ____ \| |     
 |_____/ \___\__,_|_| |_|_| |_|\___|_|    |_| \_|_|  |_/_/    \_\_|     
                                                                        
                                                                        
BANNER
echo "${RESET}"
echo



#1- Pedir la IP a escanear

read -p "IP: " IP

#2- Crear un medidor de tiempo que indique una barra en como va el proceso.

# Barra "marquee" indeterminada mientras corre un PID
marquee_progress() {
  local pid=$1
  local msg=${2:-"Procesando..."}
  local width=36
  local pos=0
  local direction=1
  local fill_char='#'
  local empty_char='-'

  printf "%s " "$msg"
  while kill -0 "$pid" 2>/dev/null; do
    local bar=""
    for ((i=0;i<width;i++)); do
      if [ $i -eq $pos ]; then
        bar+="$fill_char"
      else
        bar+="$empty_char"
      fi
    done
    printf "\r%s [%s]" "$msg" "$bar"
    pos=$((pos + direction))
    if [ $pos -ge $((width-1)) ]; then direction=-1; pos=$((width-1)); fi
    if [ $pos -le 0 ]; then direction=1; pos=0; fi
    sleep 0.08
  done

  # mostrar barra completa cuando termine
  local full=""
  for ((i=0;i<width;i++)); do full+="$fill_char"; done
  printf "\r%s [%s]\n" "$msg" "$full"
}

#3- ejecutar el comando con la variable definida como la ip

sudo nmap -p- --open -sS -sV -sC -Pn "$IP" -oN "scan.txt" >/dev/null 2>&1 &
nmap_pid=$!
marquee_progress "$nmap_pid" "Escaneando ${IP}..."
wait "$nmap_pid"


