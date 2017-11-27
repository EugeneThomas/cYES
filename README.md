# Cloudy with a Chance of Skeeball
## Team cYES: carol Pan, Yuyang Zhang, Eugene Thomas, and Samantha Ngo

### Our app makes suggestions for activities to do today based on the weather patterns. It provides daily weather updates and based on the weather forecast, we suggest activities such as current movies in theaters, treanding books, and local events.

#### Things you will need pre-installed on your computer:
- Git Terminal ___ get it here: https://git-scm.com/downloads ___
- Flask ___ get it here: http://flask.pocoo.org/ ___

#### Once you have that, clone our repo by entering `git clone https://github.com/EugeneThomas/cYES.git`

### Procure the necessary API Keys:
#### Open `keys.txt` in a text editor.
#### Weather API
1. [Register Here.](http://api.wunderground.com/member/registration?mode=api_signup)
2. Confirm your email
3. [Go Here](http://api.wunderground.com/weather/api/d/pricing.html) and create a project.
4. Copy the given API key.
5. You now have the weather API key!
6. Go to `keys.txt` and place your api key where it says `insert_weather_api_key_here` by replacing it.

#### NYT Book Reviews API
1. [Register Here](https://developer.nytimes.com/signup) and sign up for Books API.
2. Check your email for the API key.
4. Copy the given API key.
5. You now have the book API key!
6. Go to `keys.txt` and place your api key where it says `insert_book_api_key_here` by replacing it.

#### EventBrite API
1. [Register Here](http://www.eventbrite.com/myaccount/apps/) and sign up for EventBrite API.
2. Create a free simple account on EventBrite.
3. Select the `Create an app` button and fill out the required information. You can use any URL for `Application URL` field.
4. Copy the given `Your personal OAuth token` key.
5. You now have the events API key!
6. Go to `keys.txt` and place your api key where it says `insert_eventbrite_api_key_here` by replacing it.

#### Save your `keys.txt` file with all the new information. All three rows should have been replaced by your newly acquired keys and you should not have to procure new keys again unless you delete the repo.

### Now to run:
#### 1. Enter your virtual environment in your terminal.
#### 2. `cd` into the root directory of the repo
#### 3. Run the following command: `python app.py`
#### 4. The web app should now be available in your browser at `localhost:5000/`
