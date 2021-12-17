# Gentoo

Installation on a Lenovo/IBM T500/T60 Laptop

## Let's start

``` sh
gentoo acpi=on docache dosshd passwd=pw
10 # for german
net-setup eth0
```

## Partitioning

``` sh
fdisk /dev/sda
p (Partitionstabelle anzeigen)
d # (Partition # löschen)
n (Bootpartition erstellen P= Primär, 1=Partitionsnummer, Start = default, Ende = +32M)
n (Swappartition erstellen P= Primär, 2=Partitionsnummer, Start = default, Ende = +2048M)
n (Rootpartition erstellen P= Primär, 3=Partitionsnummer, Start = default, Ende = default)
```

## Create Filesystem

``` sh
mke2fs /dev/sda1
mke2fs -j /dev/sda3

mkswap /dev/sda2
swapon /dev/sda2

mount /dev/sda3 /mnt/gentoo
mkdir /mnt/gentoo/boot
mount /dev/sda1 /mnt/gentoo/boot
```

## add mirror

``` sh
cd /mnt/gentoo
links http://www.gentoo.org/main/en/mirrors.xml
```

choose mirror```releases/x86/autobuilds/, x86, i686```

``` sh
tar xvjpf stage3-*.tar.bz2
```

## Portage

Link: <http://www.gentoo.org/main/en/mirrors.xml>
Choose mirror:```snapshots/, portage-latest.tar.bz2```

``` sh
tar xvjf /mnt/gentoo/portage-latest.tar.bz2 -C /mnt/gentoo/usr
```

``` sh
nano -w /mnt/gentoo/etc/make.conf
	+CFLAGS="-O2 -march=i686 -pipe -fomit-frame-pointer"
	+MAKEOPTS="-j3"
	+AUTOCLEAN="YES"
	+USE="-gtk -gnome qt3 qt4 kde dvd alsa cdr"
	+VIDEO_CARDS="radeon"
	+INPUT_DEVICES="evdev"
	+INPUT_DEVICES="synaptics"
```

``` sh
mirrorselect -i -o >> /mnt/gentoo/etc/make.conf
mirrorselect -i -r -o >> /mnt/gentoo/etc/make.conf
```

``` sh
cp -L /etc/resolv.conf /mnt/gentoo/etc/
```

``` sh
mount -t proc none /mnt/gentoo/proc
mount -o bind /dev /mnt/gentoo/dev
```

``` sh
chroot /mnt/gentoo /bin/bash
env-update
source /etc/profile
export PS1="(chroot) $PS1"
```

``` sh
emerge --sync
emerge --oneshot portage
```

``` sh
eselect profile list
eselect profile set 2
```

``` sh
nano -w /etc/locale.gen
```

Choose:

```
en_US ISO-8859-1
en_US.UTF-8 UTF-8
de_DE ISO-8859-1
de_DE@euro ISO-8859-15
```

``` sh
cp /usr/share/zoneinfo/Europe /etc/localtime
```

``` sh
emerge gentoo-sources
```

``` sh
cd /usr/src/linux
make menuconfig
```

More details: <http://de.gentoo-wiki.com/wiki/IBM_Lenovo_Thinkpad_R60>

## Special Lenovo T60 Devices

``` sh
emerge radeon-ucode
echo "media-libs/mesa -classic gallium" >> /etc/portage/package.use
emerge -uN mesa
emerge xev
```

``` sh
emerge iwl3945-ucode
emerge alsa-utils
rc-update add alsasound boot
emerge bluez --> Fals es nicht klappt: emerge bluez-firmware
rc-update add bluetooth default
emerge acpid
rc-update add acpid default
emerge pam_fprint
echo app-laptop/hdapsd >> /etc/portage/package.accept_keywords
emerge hdapsd
rc-update add hdapsd default
alsaconf
```

## COMPILE BABY

``` sh
make && make modules_install
cp arch/i386/boot/bzImage /boot/kernel-2.6.37-gentoo-r4
find /lib/modules/kernel-2.6.37-gentoo-r4/ -type f -iname '*.o' -or -iname '*.ko' | less
nano -w /etc/modules.autoload.d/kernel-2.6 -> Dateinamen ohne Pfad und Endung hier eintragen
```

## Partitionen automatisch mounten

``` sh
/dev/sda1   /boot        ext2    defaults,noatime     1 2
/dev/sda2   none         swap    sw                   0 0
/dev/sda3   /            ext3    noatime              0 1

/dev/cdrom  /mnt/cdrom   auto    noauto,user          0 0

proc        /proc        proc    defaults             0 0
shm         /dev/shm     tmpfs   nodev,nosuid,noexec  0 0
```

## Hostname eintragen:

``` sh
nano -w /etc/conf.d/hostname
```

## Hier das .\\O löschen

``` sh
nano -w /etc/issue
nano -w /etc/conf.d/net
	+config_eth0=( "dhcp" )
rc-update add net.eth0 default
passwd
nano -w /etc/conf.d/keymaps
	~SET_WINDOWKEYS="yes"
nano -w /etc/conf.d/clock
	~ CLOCK="local"
	~ TIMEZONE="Europe/Berlin"
emerge syslog-ng
rc-update add syslog-ng default
emerge logrotate
emerge vixie-cron
rc-update add vixie-cron default
emerge mlocate
emerge dhcpcd
emerge links
rc-update add sshd default
```

# Bootloader installieren

``` sh
emerge grub
nano -w /boot/grub/grub.conf
	~ default 0
	~ timeout 3
	~ #splashimage=(hd0,0)/boot/grub/splash.xpm.gz
	~ title The almighty WizardOfOS
	~ root (hd0,0)
	~ kernel /boot/kernel-2.6.37-gentoo-r4 root=/dev/sda3
grep -v rootfs /proc/mounts > /etc/mtab
grub-install --no-floppy /dev/sda
exit
cd
umount /mnt/gentoo/boot /mnt/gentoo/dev /mnt/gentoo/proc /mnt/gentoo
reboot
```

## X-Window

``` sh
emerge xorg-server
emerge xorg-x11

nano -w /etc/make.conf
	~ USE="-gtk -gnome qt3 qt4 kde dvd alsa cdr hal dbus static-libs nls -dynamic X acpi crypt -apm -debug -dell"

emerge udev
emerge dbus
/etc/init.d/dbus restart

emerge --unmerge upower
emerge hal
emerge xf86-input-evdev

env-update
source /etc/profile


/etc/init.d/hald start
rc-update add hald default

emerge twm
emerge xterm

nano -w /etc/hal/fdi/policy/10-x11-input.fdi
In <match key="info.capabilities" contains="input.keys"> diesen String hinzufügen:
	+ <merge key="input.xkb.options" type="string">terminate:ctrl_alt_bksp</merge>

/etc/init.d/hald restart

cp /usr/share/hal/fdi/policy/10osvendor/10-input-policy.fdi /etc/hal/fdi/policy
cp /usr/share/hal/fdi/policy/10osvendor/10-x11-input.fdi /etc/hal/fdi/policy

cp /usr/share/X11/xorg.conf.d/10-evdev.conf /etc/X11/xorg.conf.d


nano -w /etc/X11/xorg.conf.d
	+ Section "Device"
   	+	Identifier  "Grafikkarte"
   	+	Driver      "radeon"
   	+ 	Option      "AccelMethod" "EXA"
	+ EndSection


Xorg -configure
```

Test

``` sh
X -retro -config /root/xorg.conf.new

cp /root/xorg.conf.new /etc/X11/xorg.conf
```

## KDE

### Edit the make.conf (comment the original USE)

``` sh
XUSE="truetype X new-login xorg xscreensaver xv xcomposite xinerama opengl aiglx"
IMAGEUSE="jpeg gif tiff png svg pdf"
MEDIAUSE="alsa mad vidix asf win32codecs dvd mp4 aac x264 xvid nsplugin mp3 real"
GENERAL="samba java bzip2 symlink sqlite spell xml"
SYSTEM="hal fam dbus aoss threads"
NOTUSE="-arts -qt4"
KDEUSE="kde kdeenablefinal qt3 rdesktop"
XTRA="declarative sql webkit"

KDESTUFF="nls pam acl fam ipv6 samba ssl consolekit usb threads crypt gtk alsa xine gstreamer exif cups addbookmarks autoreplace contactnotes handbook highlight history nowlistening pipes privacy ssl statistics texteffect translator urlpicpreview xmpp handbook python rss xinerama sqlite webkit holidays opengl X a52 aac alsa css dts flac gnome gtk ipv6 mad mng modplug musepack nls opengl samba sdl theora truetype v4l vidix vorbis win32codecs xcb xinerama xv 3dnow 3dnowext X alsa bzip2 encode hardcoded-tables mmx mmxext mp3 sdl ssse3 threads vorbis x264 xvid zlib"

USE="${KDESTUFF} ${XTRA} ${NOTUSE} ${SYSTEM} ${GENERAL} ${IMAGEUSE} ${XUSE} ${KDEUSE} ${MEDIAUSE}"
```

``` sh
emerge kde-meta
emerge kdm
locate kdmrc
	~AllowRootLogin=true
kdm
```

## Notes

``` sh
nano -w /etc/X11/xorg.conf.d/10-evdev.conf
	+ Section "InputClass"
	+ 	Identifier "evdev keyboard catchall"
	+ 	Option "xkb_layout" "de"
	+ EndSection
```

``` sh
nano -w /etc/X11/xorg.conf/99-synaptics

	+ Section "InputClass"
        + 	Identifier "Alle Touchpads"
        + 	Option SHMConfig "on"
	+       MatchIsTouchpad "on"
	+ EndSection
```

``` sh
nano -w /etc/X11/xorg.conf.d/10-evdev.conf
	+ Section "InputClass"
	+         Identifier "evdev keyboard catchall"
	+         Option "xkb_layout" "de"
	+ EndSection
```
