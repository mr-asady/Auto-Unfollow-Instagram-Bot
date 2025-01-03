### Instagram Auto Unfollow Bot
This automated script for Instagram helps you easily unfollow users from your following list. After the first login, the bot saves the session cookie, so you won’t need to log in again. The bot unfollows one user every 10 seconds, and you can adjust the time between unfollows.

### Requirements:
Download and install geckodriver and provide the full path to the executable.
Download and install the Firefox browser.
Python 3.x installed on your machine.
Install dependencies using pip.

## Setup Instructions:
Clone the repository: First, clone this repository to your local machine.


# Download and install required tools:

Download geckodriver from the [official release page](https://github.com/mozilla/geckodriver/releases) and extract the contents.
Install Firefox from the [official website](https://www.mozilla.org/en-US/firefox/new/).
# Set the paths for geckodriver and Firefox:

After downloading, place geckodriver.exe in a location of your choice and make sure to update the path to this file in the code.
Similarly, install Firefox and update the path to firefox.exe in the code.
# Example of the paths:

```
service = Service('C:/path/to/geckodriver.exe')  # Full path to geckodriver.exe
```
```
options.binary_location = r'C:/path/to/firefox.exe'  # Full path to firefox.exe
```
# Enter your Instagram username and password:
After setting the paths, you'll need to enter your Instagram login credentials in the script:

On line 36, replace ```USERNAME_HERE``` with your Instagram username. For example
```
username_input.send_keys('USERNAME_HERE')
```
On line 41, replace ```PASSWORD_HERE``` with your Instagram password. For example:
```
password_input.send_keys('PASSWORD_HERE')
```

# Install dependencies: Create a requirements.txt file with the following content:

```
selenium
```
Then, install the required Python dependencies by running:

```
pip install -r requirements.txt
```
Running the script: After completing the above steps, you can run the script by executing:

```
python script.py
```

### Important Notes:
# Enter your Instagram username and password the first time you run the bot. After that, the bot will save the session cookies, so you won’t need to log in again.
# It is recommended to use the bot for no more than one hour at a time, followed by a few hours of rest to avoid your account getting blocked.
# The bot unfollows one user every 10 seconds by default, but you can modify the interval as needed. However, it's recommended not to go below 10 seconds to maintain 
# natural behavior on Instagram.
