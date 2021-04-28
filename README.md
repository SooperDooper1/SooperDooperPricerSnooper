# Welcome to the Sooper Dooper Pricer Snooper
This is a basic Air BnB Price prediction that Helps hosts set prices based on Seattle market data.

We're currently using the archaic method of returning a mean to help hosts know what they should charge.
We may have been able to create a more accurate model with a few more hands ¯\_(ツ)_/¯ 

Using the app is as simple as:
1. Select the beginning date/end date for your predictions (smaller timeframes tend to be more accurate)
2. Enter the Zip Code for the area the listing is in
3. Bob's your Uncle. Press predict and there's the best booking price for you!


### Here's a few odd things you may run into when trying to run the app locally.

To get this to work properly on Heroku, the 'directory' argument
of 'StaticFiles' must be prepended with 'app/' to read as 'app/static'
(for local remove the 'app/')

