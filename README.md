# hotspot_autologin
1. Checks if an external website (google?) is up to determine if internet is up
2. If external website is inaccessible, check if hotspot is accessible
3. If hotspot is accessible but external website is not, run through the captive portal to log back in.

This was created to keep my machine logged in to the hotspot in my hotel. Sometimes, while I'm away/out the facility resets their equipment and then my machine is offline until I manually hit the portal again. 

They are using a mikrotik captive portal with a single shared 'user/access ID'. 

I run this as a cron job at an interval. 

# Usage 
From from CLI:

```
python hotspot_login.py https://www.google.com http://landing.portal username
```

# Requirements

Selenium