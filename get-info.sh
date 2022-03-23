#/bin/bash
#set -x

curl -k https://github.com/Lab-Brat > /dev/null 2>&1 ; CURLR=$?
if [ $CURLR -eq 0 ]
then
	GIT="\033[32mAvailable\033[0m"
else
	GIT="\033[31mNOT Available\033[0m"
fi

IPADDR4=`ip a | grep -v 'inet 127.\|inet 169.254.\|inet6 ::1/128' | grep -w inet | tr -s " " | cut -f 3 -d " "`
IPADDR6=`ip a | grep -v 'inet 127.\|inet 169.254.\|inet6 ::1/128' | grep -w inet6 | tr -s " " | cut -f 3 -d " "`

if [ ! -z "$IPADDR4" ] || [ ! -z "$IPADDR6" ]
then
	MAC=`ip a | grep -B 3 "$IPADDR4\|$IPADDR6" | grep 'link/ether' | tr -s " " | cut -f 3 -d " "`
else
	MAC=`ip a | grep -v 00:00:00:00:00:00 | grep 'link/ether' | tr -s " " | cut -f 3 -d " "`
fi

if [ -z $IPADDR4 ]
then 
	IPADDR4="There is no ipv4"
fi
if [ -z $IPADDR6 ]
then
	IPADDR6="There is no ipv6"
fi

###########

#-------------------------
subgethostname() {
mount /dev/$1 /mnt 2>/dev/null 2>1
if [ -e /mnt/etc/os-release ]
then
	REZ=`grep 'PRETTY_NAME="ALT Education 9.2 (FalcoRusticolus)"' /mnt/etc/os-release`
	if [ ! -z "REZ" ]
	then
		FREESPACE=`df -h /mnt`
		if [ -e /mnt/etc/hostname ]
		then
			COMPHOSTNAME=`cat /mnt/etc/hostname`
		else
			COMPHOSTNAME=`Undefined`
		fi
	fi
fi
umount /mnt
}
#--------------------------


STDISKS=`lsblk -o NAME,HOTPLUG,MODEL,SERIAL,TYPE,SIZE,VENDOR,TRAN | grep 'MODEL\| disk ' | grep -v -w usb | cut -f 1 -d " "`
for each in `echo $STDISKS`
do
	if [ -e /dev/${each}3 ]
	then
		subgethostname ${each}3
	fi
	if [ -e /dev/${each}1 ]
	then
		subgethostname ${each}1
	fi
done
##########

CPUMODEL=`cat /proc/cpuinfo | grep -m 1 'model name' | sed -e 's/model name[[:space:]]*: //'`
CPUCORECOUNT=`cat /proc/cpuinfo | grep 'model name' | wc -l`
RAM=`free -m | grep "Mem:" | tr -s " " | cut -f 2 -d " "`" MB"

##########

#COMPVIDEO=`lspci | grep VGA | cut -f 2- -d " "`
COMPVIDEO=`hwinfo --gfxcard | grep Model | sed -e 's/  Model:[[:space:]]*//' -e 's/"//g'`

#########

COMPDISK=`lsblk -o NAME,MODEL,TYPE,SIZE,TRAN,HOTPLUG,SERIAL | grep 'MODEL\| disk' | cut -b -76 | sed -e '/^.\{76,\}$/ s/\([A-Za-z0-9]\)$/\1.../g' | cut -b -80`
#59  echo $COMPDISK
#echo -e " \n\n\n\n"
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
echo -e " \n------ Free space on AltLinux disk -----\n$FREESPACE"
echo -e "==============================================================================="
#echo -e " \n\n\n\n"




