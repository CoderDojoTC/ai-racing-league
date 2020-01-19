#!/bin/bash
# A menu driven shell script for the AI Racing League 
# ----------------------------------
RED='\033[0;41;30m'
STD='\033[0;0;39m'
 
# User defined functions
pause(){
  read -p "Press [Enter] key to continue..." fackEnterKey
}

one(){
	echo "Calibrate Steering"
	echo "Make sure that you can communicate with the I2C bus and turn your ASC swtich to ON"
        pause
}
 
# do something in two()
two(){
	echo "Calibrate Throtte"
        pause
}

three(){
	echo "Verify I2C Communication"
        pause
}

four(){
	echo "Drive with Joystick"
        pause
}

five(){
	echo "Drive with Web Page"
        pause
}

six(){
	echo "Compress Tub to Zip File"
        pause
}

seven(){
	echo "Send Zip File to GPU Server"
        pause
}

eight(){
	echo "Get Model from GPU Server"
        pause
}

nine(){
	echo "Drive with Model"
        pause
}

# function to display menus
show_menus() {
	clear
	echo "~~~~~~~~~~~~~~~~~~~~~"	
	echo " AI Racing League - Main Menu"
	echo "~~~~~~~~~~~~~~~~~~~~~"
	echo "1. Calibrate Steering"
	echo "2. Calibrate Throttle"
	echo "3. Verify I2C Commmunication"
	echo "4. Drive with Joystick"
	echo "5. Drive with Web Page"
	echo "6. Compress Tub to Zip File"
	echo "7. Send Zip File To GPU Server"
	echo "8. Get model from GPU Server"
	echo "9. Drive with Model"
	echo "0. Exit"
}
# read input from the keyboard and take a action
# invoke the one() when the user select 1 from the menu option.
# invoke the two() when the user select 2 from the menu option.
# Exit when user the user select 3 form the menu option.
read_options(){
	local choice
	read -p "Enter choice [ 0 - 9] " choice
	case $choice in
		1) one ;;
		2) two ;;
		3) three ;;
		4) four ;;
		5) five ;;
		6) six ;;
		7) seven ;;
		8) eight ;;
		9) nine ;;
		0) exit 0;;
		*) echo -e "${RED}Error...${STD}" && sleep 2
	esac
}
 
# ----------------------------------------------
# Step #3: Trap CTRL+C, CTRL+Z and quit singles
# ----------------------------------------------
trap '' SIGINT SIGQUIT SIGTSTP
 
# -----------------------------------
# Step #4: Main logic - infinite loop
# ------------------------------------
while true
do
 
	show_menus
	read_options
done
