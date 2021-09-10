from chalice import Chalice

app = Chalice(app_name='lets-encrypt-certbot-aws-lambda')


@app.lambda_function()
def renew_tls(event, context):
    return {'hello': 'world'}
