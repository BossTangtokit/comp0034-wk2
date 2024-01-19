from flask import current_app as app


@app.route('/')
def hello():
  return f"Hello!"
