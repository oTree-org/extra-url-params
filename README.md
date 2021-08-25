# About

This is a small server that allows you to capture extra parameters passed in URLs.

For example, you can have a URL like this:

```
https://your-custom-site.herokuapp.com/?participant_label=JohnSmith&aaa=120383&&bbb=h9w132
```

The participant_label will be passed as is; all other parameters
such as 'sid' and 'xid' will be passed to oTree as participant vars.

It uses oTree's REST API.

## Setup

Clone this repo, then install dependencies with `pip3 install -r requirements.txt`.

Customize the constants in `main.py`.

## Testing locally
To run locally, do `uvicorn main:app --port 8500`.

Visit a URL like:

```
http://localhost:8500/?participant_label=JohnSmith&aaa=120383&&bbb=h9w132
```

Observe how the participant vars get recorded into oTree.

## Deploy to Heroku

Then, deploy to Heroku with:

```
heroku create
git push heroku master
heroku open
```

Now, rather than going directly to your oTree site, participants should come to this site,
which will redirect them to your oTree site.