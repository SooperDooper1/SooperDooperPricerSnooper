from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import pandas as pd
import uvicorn


# Create App with title and docs endpoint
app = FastAPI(
    title="SooperDooperPricerSnooper",
    docs_url="/docs"
)

# Mount the static folder for access to css and javascript files
# To get this to work properly on Heroku, the 'directory' argument
# of 'StaticFiles' must be prepended with 'app/' to read as 'app/static'

app.mount('/static', StaticFiles(directory='app/static'), name='static')

# Create jinja object for accessing templates
templates = Jinja2Templates(directory='app/templates')


# Create endpoint for landing page where all information
# is collected and displayed
@app.get('/')
def landing(request: Request):
    """
    Defines processes to run upon arrival to landing page.
    This is where the app will collect info from the user
    to send to the get_price route. The get price route
    will format the data, send to the machine learning
    algorithm, receive and format the result, and finally
    display that result next to the input form on the
    landing page.

    :return: The landing page of the application
    """

    template = "landing.html"
    context = {"request": request}

    return templates.TemplateResponse(template, context,
                                      media_type='text/html')


# Create endpoint for getting the suggested price
@app.get('/get_price')
def get_price(date1, date2):
    """
    Defines processes to run for the get_price route. This route
    is specifically for getting the suggested price from the
    machine learning algorithm.

    :return: The suggested price
    """

    df = pd.read_csv('https://raw.githubusercontent.com/'
                     'SooperDooper1/SooperDooperPricerSnooper'
                     '/main/Data/calendar_cleaned.csv')

    range_subset = df[(df['date'] >= date1) & (df['date'] <= date2)]
    suggested_price = range_subset['price'].mean()
    suggested_price = round(suggested_price, 2)

    return suggested_price


# Comment out the line below when deploying to Heroku
# uvicorn.run(app)
