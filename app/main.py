import pandas as pd
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from tensorflow.keras.models import load_model

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


class DateRange(BaseModel):
    start_date: str
    end_date: str


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
@app.post("/get_price/")
def get_price(date_range: DateRange):
    """
    Defines processes to run for the get_price route. This route
    is specifically for getting the suggested price from the
    machine learning algorithm.

    :return: The suggested price
    """

    df = pd.read_csv('https://raw.githubusercontent.com/'
                     'SooperDooper1/SooperDooperPricerSnooper/'
                     'main/Denver%20Data/nts_subset.csv')

    df['date'] = pd.to_datetime(df['date'], infer_datetime_format=True)

    start_date = date_range.start_date.replace('2021', '2008')
    end_date = date_range.end_date.replace('2021', '2019')

    start_date = pd.to_datetime(start_date, infer_datetime_format=True)
    end_date = pd.to_datetime(end_date, infer_datetime_format=True)

    range_subset = df[(df['date'] >= start_date) &
                      (df['date'] <= end_date)]

    range_subset = range_subset.drop(columns='date')

    target = 'price'
    features = range_subset.drop(columns=[target]).columns.tolist()

    X_test = range_subset[features]
    y_test = range_subset[target]

    model = load_model("/my_h5_model.h5")

    suggested_price = model.predict(X_test)

    suggested_price = suggested_price.mean()

    suggested_price = round(suggested_price, 2)

    return str(suggested_price)
