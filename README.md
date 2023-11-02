# Shark Presence

This is a simple console application using Discord RPC. The main purpose is to display what you listen to/watch in YouTube Music and YouTube, respectively. Also, while you are not listening to anything, it displays the stats of your PC, or a predefined text.

If you don't want to edit the code in any way and come for a working application, just download Shark.exe, you don't need to install anything for it [(except for the browser extension)](#to-display-information-from-youtube-you-will-need-the-webnowplaying-redux-extension)


# How It Looks?

#### YouTube
![YouTube](./readme_assets/2023-11-02%20214018.png)
#### YouTube Music
![YouTube Music](./readme_assets/2023-11-02%20213844.png)
#### PC Specs
![PC Specs](./readme_assets/2023-11-02%20214007.png)

### RPC updates every 10 seconds!


# Requirements

All tested on Python 3.9.11

```python
pywnp
pypresence
time
psutil
wmi
```

### **To display information from YouTube you will need the WebNowPlaying-Redux extension!**

You can find it here:
- [Google Chrome](https://chrome.google.com/webstore/detail/webnowplaying-redux/jfakgfcdgpghbbefmdfjkbdlibjgnbli)
- [Mozilla Firefox](https://addons.mozilla.org/en-US/firefox/addon/webnowplaying-redux)

**Note:** Due to a bug in firefox, you will have to manually grant it permissions.
Right click "WebNowPlaying Redux" -> Manage Extension -> Permissions -> Check "Access your data for all websites"

Now you need to open the extension and check the box next to "Custom Adapter" and write, to the right of it, "1234". When you see the green word "Connected" everything should work.

**Note:** If you launched the application but information from YouTube is not displayed, go to the extension settings again, then remove and check the box again.