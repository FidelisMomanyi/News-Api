from flask import render_template
from . import main


@main.errorhandler(404)
def four_Ow_four(error):
    '''
    An error page to render the function of 404
    '''
    return render_template('fourOwfour.html'), 404