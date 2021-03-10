from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('q1t.html')

@app.route("/response")
def render_response():
    r1 = request.args['r2'] 
    #The request object stores information about the request sent to the server.
    #args is an ImmutableMultiDict (like a dictionary but can have mutliple values for the same key and can't be changed)
    #The information in args is visible in the url for the page being requested. ex. .../response?color=blue
    if r1 == 'pink':
        reply = "That's my favorite color, too!"
    else:
        reply = "My favorite color is pink."
    return render_template('response.html', response = reply)
    
    
@app.route("/")
def render_main():
    return render_template('q2t.html')

@app.route("/response")
def render_response():
    r2 = request.args['r2'] 
    #The request object stores information about the request sent to the server.
    #args is an ImmutableMultiDict (like a dictionary but can have mutliple values for the same key and can't be changed)
    #The information in args is visible in the url for the page being requested. ex. .../response?color=blue
    if r2 == 'pink':
        reply = "That's my favorite color, too!"
    else:
        reply = "My favorite color is pink."
    return render_template('response.html', response = reply)

@app.route("/")
def render_main():
    return render_template('q3t.html')

@app.route("/response")
def render_response():
    r3 = request.args['r3'] 
    #The request object stores information about the request sent to the server.
    #args is an ImmutableMultiDict (like a dictionary but can have mutliple values for the same key and can't be changed)
    #The information in args is visible in the url for the page being requested. ex. .../response?color=blue
    if r3 == 'pink':
        reply = "That's my favorite color, too!"
    else:
        reply = "My favorite color is pink."
    return render_template('response.html', response = reply)


@app.route("/response")
def render_response():
    r4 = request.args['r4'] 
    #The request object stores information about the request sent to the server.
    #args is an ImmutableMultiDict (like a dictionary but can have mutliple values for the same key and can't be changed)
    #The information in args is visible in the url for the page being requested. ex. .../response?color=blue
    if r4 == 'pink':
        reply = "That's my favorite color, too!"
    else:
        reply = "My favorite color is pink."
    return render_template('response.html', response = reply)


if __name__=="__main__":
    app.run(debug=False, port=54321)
