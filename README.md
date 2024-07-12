# Reddit-Post-Title-Scraper
Small Python script that queries the Reddit API, and creates an Excel sheet of the most recent 1,000 post titles for a given subreddit. This is the first "real" Python program I created. As such, there is likely a lot of room for improvement. Nevertheless, it works well enough, and generally does what I wanted it to.

## About this title scraper
I created this program, because I wanted a simple way to harvest the last five years' worth of post titles from any given subreddit, and output them as an Excel spreadsheet. I later learned that this is not possible, since the API limits queries to the last 1,000 records only.

## Getting Reddit app credentials
In order to use this, you need to create a Reddit app in your Reddit account.

1. Log into Reddit
2. Access the App Creation Page at https://www.reddit.com/prefs/apps
3. Create a new app with the necessary details
   - name: choose a name for your app
   - app type: select script for personal use or simple scripting tasks
   - description (optional)
   - about url (optional)
   - redirect url: for a script type app such as this, you can put 'http://localhost:8080' or some other placeholder
   - Click "Create App" at the bottom of the form
4. Get your credentials
   - client_id
   - client_secret
5. Add the client_id and client_secret to the script
6. For user_agent, you can use something like 'My Reddit app by /u/yourusername'

Obviously, keep these credentials secret.
