**Additional Guidlines**

You can use the tool's icon located at **'src/assets/icons/ELPM-preview.png'** to setup the desktop icon if it doesn't set up nor displays after running it.
The main path in main_window.py & elpm_main.py have been set. Simlpy add the icon to your .Desktop file following this:

First create and open the .desktop file:
```
nano ~/.local/share/applications/elpmd.desktop

```

Paste the following into the text editor

```

[Desktop Entry]
Type=Application
Name=ELPMD
Comment=Enhanced Linux Process Monitor
Exec=/home/gr3ytrac3/Pictures/enhanced-linux-process-monitor/src/run_elpm.sh
Icon=ELPM-preview
Terminal=false
Categories=Utility;System;
StartupNotify=true

```
Make the file executable. This renders the icon executable that runs the [run_elpm.sh](src/run_elpm.sh) script


```
chmod +x ~/Desktop/elpmd.desktop

```
Then run

```
gtk-launch elpmd

```

You should be able to see the icon on your Desktop
