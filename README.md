# Spotify Follower Scraper

A Python script to retrieve any Spotify user's followers.


## Usage

Run the scraper using the following command:
``` bash
python scraper.py SPOTIFY_USER_ID
```

Replace `SPOTIFY_USER_ID` with the target user's Spotify ID.

## Spotify User ID

The Spotify user ID is a unique string identifier for a Spotify user. It can be found at the end of the Spotify URI for the user. For example, in the URI spotify:user:wizzler, the user ID would be wizzler.

To obtain a user's Spotify ID:
1. Open the Spotify desktop client
2. Navigate to the user's profile
3. Right-click (Windows) or Ctrl-Click (Mac) on the user's name
4. Select "Copy link to profile"
   
This URL contains the Spotify user ID and should be of the format:
```
https://open.spotify.com/user/USER_ID?
```

## Note
This script is for educational purposes only. Please respect Spotify's terms of service and users' privacy when using this tool.

## Additional Information
For more details on Spotify URIs and IDs, refer to the [official Spotify Web API documentation](https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids).
