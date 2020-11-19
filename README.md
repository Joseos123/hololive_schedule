## This fork just makes it english and removes the previous streams tab.
# hololive_schedule

`hololive_schedule` is a macOS status bar plugin using BitBar. It can help you get the streaming information of hololive members conveniently, just in your status bar.

> BitBar can run your scripts regularly and put the output on your status bar. You can go to [here](https://getbitbar.com/) to install BitBar and know how it works.

![screenshot.png](https://github.com/Joseos123/hololive_schedule/blob/master/images/Screenshot%202020-11-19%20at%208.50.08%20PM.png?raw=true)

[GIF demo here](https://s1.ax1x.com/2020/07/13/UJLbdA.gif)

## Features

1. Get liveroom information from [hololive offical schedule website](https://schedule.hololive.tv/lives/all), contains live time ( date and time ), liver's name and liveroom link in just serval seconds;
2. Classify the liverooms into "Streaming now", "Upcoming" and "Stream over" (from hololive offical schedule website). The liverooms which are streaming will be at the top and have marks;
3. Auto detect the user's timezone and display the accurate time (not in default Tokyo time).

## How to use

1. [Install BitBar](https://getbitbar.com/) and run it once to set the plugins folder;
2. Download the script and copy it at the plugins folder;
3. Refresh the plugin in your status bar and enjoy it.

## For Windows Users

Because there is not a tool such like BitBar on Windows platform, Windows users cannot use this script like a menu in their taskbar. But you can also execute this script in your terminal if you have python3 and `bs4` and `requests` module installed. You can get the same output.

## Notice

1. Need Python3 or above ;
2. ~~Need `bs4` and `requests` packages, you can install them with `pip3 install bs4 requests` ;~~
3. ~~If your `python3` is not at `/usr/local/bin/python3` , you might need to change the python3 interpreter's path at the first line of the script;~~
4. You can rename the script as `hololive_schedule.{xxx}.py` to let BitBar run the script with a custom time interval. For example, `hololive_schedule.90s.py` means run the script every 90s;
5. ~~Because there are many URLs to get, the script might need a little long time to run. On my device and network environment (MacBook Air 2018 & **CANNOT** connect to YouTube directly), it will take about 90s to refresh once;~~
6. ~~You will need a proxy if you cann't get access to YouTube directly;~~
7. Beacuse there are only YouTube liveroom links on the hololive offical schedule website, no BiliBili links are provided;
8. You may need to do `chmod +x hololive_schedule.py` to make the script working normally.

## Update notes

### 2020-7-13

1. Add emoji marks for every hololive member;
2. Add a option can lead you to hololive offical schedule website.

### 2020-8-5

1. Now the script can get all information without YouTube webpage. Now it just take serval seconds to refresh once and it can work without proxy (for regions cannot connect directly to YouTube);
2. Add text tells the time taken of last refreshing.

### 2020-8-23

Add new emojis for hololive 5th generation.

### 2020-9-16

Add new emojis for holoEN.

### 2020-11-13

Auto-install packages which are not exist.

## TODO

1. ~~Optimize refreshing speed (for YouTube links);~~
2. ~~Support for HoloCN members (There are no info of HoloCN on the offical website);~~
3. Get bilibili liveroom links;
4. Develop a Rainmeter plugin based on this script for Windows users.

