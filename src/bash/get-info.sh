#/bin/bash
#set -x

curl -k https://github.com/Lab-Brat > /dev/null 2>&1 ; CURLR=$?
if [ $CURLR -eq 0 ]
then
	GIT="\033[32mAvailable\033[0m"
else
	GIT="\033[31mNOT Available\033[0m"
fi

IPADDR4=`ip a \
        | grep -v 'inet 127.\|inet 169.254.\|inet6 ::1/128' \
		| grep -w inet \
		| tr -s " " \
		| cut -f 3 -d " "`
IPADDR6=`ip a \
        | grep -v 'inet 127.\|inet 169.254.\|inet6 ::1/128' \
		| grep -w inet6 \
		| tr -s " " \
		| cut -f 3 -d " "`

if [ ! -z "$IPADDR4" ] || [ ! -z "$IPADDR6" ]
then
	MAC=`ip a \
	     | grep -B 3 "$IPADDR4\|$IPADDR6" \
		 | grep 'link/ether' \
		 | tr -s " " \
		 | cut -f 3 -d " "`
else
	MAC=`ip a \
	     | grep -v 00:00:00:00:00:00 \
		 | grep 'link/ether' \
		 | tr -s " " \
		 | cut -f 3 -d " "`
fi

if [ -z $IPADDR4 ]
then 
	IPADDR4="There is no ipv4"
fi
if [ -z $IPADDR6 ]
then
	IPADDR6="There is no ipv6"
fi

COMPHOSTNAME=`hostname -f`

FREESPACE=`df -h /`
CPUMODEL=`cat /proc/cpuinfo \
          | grep -m 1 'model name' \
		  | sed -e 's/model name[[:space:]]*: //'`
CPUCORECOUNT=`cat /proc/cpuinfo | grep 'model name' | wc -l`
RAM=`free -m \
     | grep "Mem:" \
	 | tr -s " " \
	 | cut -f 2 -d " "`" MB"

COMPVIDEO=`hwinfo --gfxcard \
           | grep Model \
		   | sed -e 's/  Model:[[:space:]]*//' -e 's/"//g'`
COMPDISK=`lsblk -o NAME,MODEL,TYPE,SIZE,TRAN,HOTPLUG,SERIAL \
          | grep 'MODEL\| disk' \
		  | cut -b -76 \
		  | sed -e '/^.\{76,\}$/ s/\([A-Za-z0-9]\)$/\1.../g' \
		  | cut -b -80`

echo -e "==============================================================================="
echo -e " github.com/Lab-Brat:\t$GIT"
echo -e " IPv4 address:\t\t$IPADDR4"
echo -e " IPv6 address:\t\t$IPADDR6"
echo -e " MAC address:\t\t$MAC"
echo -e " Hostname:\t\t$COMPHOSTNAME"
echo -e " CPU Model name:\t$CPUMODEL"
echo -e " CPU Core count:\t$CPUCORECOUNT"
echo -e " RAM size:\t\t$RAM"
echo -e " Videcard:\t\t$COMPVIDEO"
echo -e " \n----------------- Disks ----------------\n$COMPDISK"
echo -e " \n------ Free space on disk -----\n$FREESPACE"
echo -e "==============================================================================="
