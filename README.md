# nowplaying
Now Playing Twitch overlay for the "Now Playing in Texts" V2 VLC extension

## What is this

`davur/nowplaying` is a Twitch overlay for displaying information on what is 
being played currently in VLC.

It was written entirely [live on Twitch](https://www.twitch.tv/videos/1551955388).

## How to use it

### Pre-requisites

1. Install [Now Playing in Texts V2](https://addons.videolan.org/p/1172613/).
2. Make sure it is configured and enabled in VLC.
3. Install PIP requirements. Run `pip install -r requirements.txt`.

### Run nowplaying backend

1. From repository root directory, run:

	```
	python nowplaying.py --metadata-path=<path> runserver
	```

	Provide the path corresponding to your "Now Playing in Texts" output path.
	The default output path in Mac OS is "~/Library/Application Support/org.videolan.vlc/np_metadata.txt",
	see docs for the default for your OS https://addons.videolan.org/p/1172613/

2. Add a Browser over "Browser" source to OBS (or equivalent) with the URL set 
   to "http://127.0.0.1:5000"
