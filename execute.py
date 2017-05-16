import subprocess
import os
# command to monitor the screensaver
# MONITOR = "xscreensaver-command"
# MONITOR_ARGS = [MONITOR, "-watch"]

# commands to turn the screen on and off
# update control to  have the value vcgencmd
CONTROL = "vcgencmd"
DISABLE_DISPLAY = [CONTROL, "display_power", "0"]
ENABLE_DISPLAY = [CONTROL, "display_power", "1"]
DEFAULT = ['ON', 'green']


def hdmi(DEFAULT):
    if DEFAULT == ['ON', 'green']:
        subprocess.call(DISABLE_DISPLAY)
        DEFAULT[0], DEFAULT[1] = 'OFF', 'red'
    else:
        subprocess.call(ENABLE_DISPLAY)
        DEFAULT[0], DEFAULT[1] = 'ON', 'green'
    return DEFAULT

hdmi(DEFAULT)

