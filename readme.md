A command-line tool to extract and play direct links to streaming TV channels found on (some) websites.

Prerequisites: Python 3, VLC media player, youtube-dl

Python dependencies:
* requests - for fetching remote files
* tldextract - to extract domains from URLs easily
* youtube-dl - to have YT handled for me :)

Usage: `python TVRetriever <url>`<br>
Example: `python TVRetriever https://trwamtv.live.rd.insyscd.net/cl01/out/u/trwam.mpd`

Known issues:
* Cannot play a video through PotPlayer using command line
