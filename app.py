from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def hello():
    arg = request.args.get("arg", default="", type = str)

    template = """
    <html>
    <head>
        <title>animal</title>
        <style>
            body {{
                text-align:center;
            }}
        </style>
    <body>
    <h1>{}</h1>
    {{% if arg == 'cat' %}}
        <img src='/static/images/cat.jpg' >
    {{% elif arg == 'dog' %}}
        <img src='/static/images/dog.jpg' >
    {{% elif arg == 'rat' %}}
        <img src='/static/images/rat.jpg' }} >
    {{% else %}}
        <img src='/static/images/no.jpg' }} >
    {{% endif %}}
    </br>
    </br>
    <a href="/?arg=cat">cat</a>
    <a href="/?arg=dog">dog</a>
    <a href="/?arg=rat">rat</a>
    </body>
    </html>
    """.format(arg)

    return render_template_string(template,arg=arg)
#    return 'Hello Flask World'

if __name__ == '__main__':
    app.run()
