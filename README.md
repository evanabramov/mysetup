![screenshot_20220512_113953](https://user-images.githubusercontent.com/63347222/168029404-a680925c-2413-475b-9c22-f62788060da5.png)

WM: i3

bar: polybar

terminal: alacritty

file managers: ranger, nautilus

launcher: rofi

screenshots: scrot + xclip

composer: picom

IDE: Pitch Black theme + Recursive Mono 13.0

Currently using Arch with GNOME 42.1(can be easily installed with archinstall)

![image](https://user-images.githubusercontent.com/63347222/169929084-7e26b5ed-0602-4974-b481-a6cdcc57e519.png)

And slightly modified DTOS

![image](https://user-images.githubusercontent.com/63347222/170149967-62d0da46-8279-4873-95af-5ddb2051b10c.png)

Currently stick to Arch + Gnome with Gruvbox theme.

![image](https://user-images.githubusercontent.com/63347222/172941861-a822f2e5-d8f7-41e3-aedf-02b28693a535.png)

Some void linux notes:

a. when setting up pipewire, use elogind

b. pipewire itself :

Install pipewire:

xbps-install pipewire alsa-pipewire 
(libpulseaudio-pipewire is NOT needed. In fact, it appears to have been removed from the repos.)

idk if all this needed if no pulseaudio is installed tho

Uncomment the following line in /etc/pipewire/pipewire.conf:

#"/usr/bin/pipewire" = { args = "-c pipewire-pulse.conf" }

Run these commands:

mkdir -p /etc/alsa/conf.d
ln -s /usr/share/alsa/alsa.conf.d/50-pipewire.conf /etc/alsa/conf.d
ln -s /usr/share/alsa/alsa.conf.d/99-pipewire-default.conf /etc/alsa/conf.d
Edit /etc/pulse/client.conf and replace the following line:

; autospawn = yes

With:

autospawn = no

Finally, set Pipewire to start when you start a user session/log in. 

c. lightdm and lightdm-gtk3-greeter alongside i3

d. ad nonfree repos for intellij
