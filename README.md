# Welcome to the Sooper Dooper Pricer Snooper
This is a basic Air BnB Price prediction that Helps hosts set prices based on Denver market data.

Using the app is as simple as:
1. Select the beginning date/end date for your predictions (smaller timeframes tend to be more accurate)
2. Enter the Zip Code for the area the listing is in
3. Bob's your Uncle. Press predict and there's your Sooper Dooper booking price for you!


### Here's a few odd things you may run into when trying to run the app locally.

To get this to work properly on Heroku, the `directory` argument
of `StaticFiles` and `Jinja2Templates` must be prepended with `app/` to 
read as `app/static` and `app/templates`. Will also need to add `uvicorn.run(app)` to 
the end of `main.py`
(for local remove the `app/` and `uvicorn.run(app)`)
