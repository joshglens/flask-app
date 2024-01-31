from flask import Flask
app = Flask(__name__)

@app.route('/')
def cool_button():
    cool_button = '''
        <button class="pushable" style="background: hsl(340deg 100% 32%); border: none; border-radius: 12px; padding: 0; cursor: pointer;">
            <span class="front" style="display: block; padding: 12px 42px; border-radius: 12px; font-size: 1.25rem; background: hsl(345deg 100% 47%); color: white; transform: translateY(-4px);">
                Push me
            </span>
        </button>\n'''
    return '<p>Hello Cool Button</p>' + cool_button
