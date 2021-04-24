from fastapi import FastAPI
import uvicorn


app = FastAPI(
    title="SooperDooperPricerSnooper",
    docs_url="/docs"
)


@app.get('/')
def landing():
    """
    Defines processes to run upon arrival to landing/home/root/index page.
    This is where the app will collect info from the user

    :return: The landing page of the application
    """

    return 'Landing'


@app.get('/location')
def landing():
    """
    Defines processes to run upon arrival to location page.
    This is where the app will collect info from the user

    :return: The location page of the application
    """

    return 'Location'


@app.get('/time')
def landing():
    """
    Defines processes to run upon arrival to time page.
    This is where the app will collect info from the user

    :return: The time page of the application
    """

    return 'Time'


@app.get('/refresh')
def landing():
    """
    Defines processes to run upon arrival to refresh page.
    This is where the app will collect info from the user

    :return: The refresh page of the application
    """

    return 'Refresh'


@app.get('/display')
def landing():
    """
    Defines processes to run upon arrival to display page.
    This is where the app will collect info from the user

    :return: The landing page of the application
    """

    return 'Display'


@app.get('/test')
def test():
    """
    Defines the docs route for frontend generation.
    :return: Interface for front end generation
    """

    return {'body': 'Test Route Working'}


# uvicorn.run(app)
