from flask import Flask
import random
app = Flask(__name__)

@app.route('/')
def cool_button():
    red_button = '''
        <button class="pushable" style="background: hsl(340deg 100% 32%); border: none; border-radius: 12px; padding: 0; cursor: pointer;">
            <span class="front" style="display: block; padding: 12px 42px; border-radius: 12px; font-size: 1.25rem; background: hsl(345deg 100% 47%); color: white; transform: translateY(-4px);">
                Push me, I'm Red!
            </span>
        </button>\n'''
    blue_button = '''
        <button class="pushable" style="background: hsl(240deg 100% 32%); border: none; border-radius: 12px; padding: 0; cursor: pointer;">
            <span class="front" style="display: block; padding: 12px 42px; border-radius: 12px; font-size: 1.25rem; background: hsl(245deg 100% 47%); color: white; transform: translateY(-4px);">
                Push me, I'm Blue!
            </span>
        </button>\n'''
    green_button = '''
        <button class="pushable" style="background: hsl(120 100% 32%); border: none; border-radius: 12px; padding: 0; cursor: pointer;">
            <span class="front" style="display: block; padding: 12px 42px; border-radius: 12px; font-size: 1.25rem; background: hsl(125deg 100% 47%); color: white; transform: translateY(-4px);">
                Push me, I'm Green!
            </span>
        </button>\n'''

    return_string = "<p>Here are a random amount of red buttons:</p>"
    for x in range(random.randrange(1, 10)):
        return_string += red_button

    return_string += "<p>Here are a random amount of green buttons:</p>"
    for x in range(random.randrange(1, 10)):
        return_string += green_button

    return_string += "<p>Here are a random amount of blue buttons:</p>"
    for x in range(random.randrange(1, 10)):
        return_string += blue_button

    return '<p>Hello Random Number of Cool Buttons</p>' + return_string
