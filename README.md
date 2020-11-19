## This fork just makes it english and removes the previous streams tab.
# hololive_schedule

`hololive_schedule` is a macOS status bar plugin using BitBar. It can help you get the streaming information of hololive members conveniently, just in your status bar.

> BitBar can run your scripts regularly and put the output on your status bar. You can go to [here](https://github.com/matryer/bitbar) to install BitBar and know how it works.

![screenshot.png](https://github.com/Joseos123/hololive_schedule/blob/master/images/Screenshot%202020-11-19%20at%208.50.08%20PM.png?raw=true)

[GIF demo here](https://s1.ax1x.com/2020/07/13/UJLbdA.gif)

## Features

1. Get liveroom information from [hololive offical schedule website](https://schedule.hololive.tv/), contains live time ( date and time ), liver's name and liveroom link in just serval seconds;
2. Classify the liverooms into "Streaming now", "Upcoming" and "Stream over" (from hololive offical schedule website). The liverooms which are streaming will be at the top and have marks;
3. Auto detect the user's timezone and display the accurate time (not in default Tokyo time).

## How to use

1. [Install BitBar](https://github.com/matryer/bitbar/releases/download/v1.9.2/BitBar-v1.9.2.zip) and run it once to set the plugins folder;
2. Download the script and copy it at the plugins folder;
3. Refresh the plugin in your status bar and enjoy it.

## Notice

1. Need Python3 or above ;
2. You can rename the script as `hololive_schedule.{xxx}.py` to let BitBar run the script with a custom time interval. For example, `hololive_schedule.90s.py` means run the script every 90s;
3. Beacuse there are only YouTube liveroom links on the hololive offical schedule website, no BiliBili links are provided;
4. You may need to do `chmod +x hololive_schedule.py` to make the script working normally.
5. Because this uses the official schedule website, the status change from "upcoming" to "now" might take quite a while, as it is not instant on the site :/
