import logging
from chalice import Chalice

app = Chalice(app_name='lets-encrypt-certbot-aws-lambda')

app = Chalice(app_name='lets-encrypt-certbot-aws-lambda', debug=True, configure_logs=True)
app.debug = True
logging.getLogger().setLevel(logging.DEBUG)


@app.lambda_function()
def renew_tls(event):
    logging.debug("Received an event {}".format(event))
    return {'hello': 'world'}
