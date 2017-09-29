#!/bin/bash
# Save file as spreadsheet-interface.sh in local directory
# Requires chmod +x ./spreadsheet-interface.sh
### FROM: https://superuser.com/questions/181517/how-to-execute-a-command-whenever-a-file-changes


### Set initial time of file
LTIME=`stat -c %Z in.csv`
PLAYWAVEPLAYER="mplayer out.wav -loop 0  > /dev/null 2>&1 &"
KILLWAVEPLAYER="pkill mplayer"

while true    
do
   ATIME=`stat -c %Z in.csv`

   if [[ "$ATIME" != "$LTIME" ]]
   then 
	   #Dont use - high CPU usage!
       #pkill bliplay; python csv-to-blip.py; cat -n out.blip; bliplay -n out.blip &
       #Creates out.wav, use music player (ie VLC) to loop on this wav file
	   pkill bliplay; python csv-to-blip.py;clear; cat -n out.blip; 
	   	   
	   
		if bliplay -n -y -o out.wav out.blip; then
			echo "bliplay succeeded"
			eval $KILLWAVEPLAYER
			eval $PLAYWAVEPLAYER
		else
			echo "bliplay failed"
			eval $KILLWAVEPLAYER
		fi


       LTIME=$ATIME
   fi
   sleep 1
done

eval $KILLWAVEPLAYER
