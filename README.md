# Update Steam Display Name
Automatically update your Steam display name.

# Disclaimer
Due to the nature of how I am interacting with steam, I have no way of determining if the user is logged in. Ensure you are already logged into steam or the macros will not be kind!

Depending on your setup, you may need to tweak a few of the constants
1. Update what browser you are using. By default, this is set to "Firefox". `BROWSER = "Firefox"`.
2. Update delays based on your setup. Slower machines/internet speeds can cause websites to load slower, and you will need to increase the amount of time to wait. `DELAY_BETWEEN_KEYS = 0.2` `TIMEOUT_TO_LOAD_PAGE = 3`

## Future Updates
The current state is Not Dynamic. The reason why is due to browser security.
I didn't want to have the user input their login credentials into my tool, and because of that I have to rely on the user already being logged into Steam. However using something like `selenium` temporarily logs the user out of all their accounts to prevent stealing user data, and I am unable to interact with the users account.

To get around this, I use keyboard input to simulate a user opening a browser of their choice. This requires static `sleep` functions and CSS Selectors.
In the future, I may switch to having the user input their credentials into my tool and I can save it off in a json or something, however Steam requiring 2FA might make that more of a hassle than it's worth

# About Me
https://www.linkedin.com/in/ryanclkeough/
