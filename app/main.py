from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn


app = FastAPI(
    title="SooperDooperPricerSnooper",
    docs_url="/docs"
)
app.mount('/static', StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory='templates')


@app.get('/')
def landing(request: Request):
    """
    Defines processes to run upon arrival to landing page.
    This is where the app will collect info from the user
    to send to the get_price route. The get price route
    will format the data, send to the machine learning
    algorithm, receive and format the result, and fincally
    display that result next to the input form on the
    landing page.

    :return: The landing page of the application
    """

    template = "landing.html"
    context = {"request": request}

    return templates.TemplateResponse(template, context, media_type='text/html')


@app.get('/get_price')
def get_price():
    """
    Defines processes to run for the get_price route. This route is specifically for getting
    the suggested price from the machine learning algorithm.

    :return: The suggested price
    """

    #TODO Write function to get and return suggested listing price
    suggested_price = 80

    return suggested_price

# Comment out the line below when deploying to Heroku
# uvicorn.run(app)