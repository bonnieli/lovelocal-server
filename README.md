This is the project for LoveLocals.ca - a project that is set to support our local businesses by buying gift cards for the future, purchasing from them safely during this time and just sharing the love!

Many businesses are in a difficult cash situation as social isolation and quarantine has forced most people to stay in their homes and non- essential businesses have closed their doors. Gift cards keep income flowing to local restaurateurs that are having to pay rent and other expenses while businesses are closed.

This project was originally set out to help Toronto but can be expanded widely to other cities as well. Other projects have been created in the past few weeks such as: Help Main Street, GiveLocal, SaveOurFaves, TheNeighbourGood and Rally for Restaurants.

To run the backend locally:

- `pip install -r requirements.txt`
- `python manage.py makemigrations` # this will create any migrations detected from your models in `models.py`
- `python manage.py migrate` to create the tables. run this every time you do introduce any migrations as well
- `python manage.py runserver`

To run this client locally:

- Go into `./client`
- `npm install`
- `npm start` : this should be running on `localhost:3000` and has proxy to port `8000`

To deploy:

- `cd client`
- `PUBLIC_URL=[STATIC_URL] yarn build`
- `cd ..`
- `python manage.py collectstatic`
- `gsutil rsync -R static gs://[GOOGLE_PROJECT_LINK]/static` #this uploads all your static folder to the cloud
- `gcloud beta app deploy --project [GOOGLE_PROJECT_ID]`

To populate the DB:

- `python scripts/load_businesses.py` to run scripts to populate the db
