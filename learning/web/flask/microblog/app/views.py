from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Don'} # fake user
    posts = [
        {'author': 'Don', 'tags': ['foo', 'bar'], 'title':'test tile', 'body': '<p>this is the body of post 1</p>'},
        {'author': 'Sue', 'tags': ['x'], 'title':'test tile 2'}
    ]
    
    
    # posts = [
    #     {
    #         'author': {'nickname': 'John'},
    #         'body': 'Beautiful day in Portland!'
    #     },
    #     {
    #         'author': {'nickname': 'Susan'},
    #         'body': 'The Avengers movie was so cool!'
    #     },
    #     {
    #         'author': {'nickname': 'Don'},
    #         'body': '..and fun was had by all!'
    #     }
    # ]

    return render_template('index.html',
                            title=app.config,
                            user=user,
                            posts=posts)

@app.route('/item', methods=['GET', 'POST'])
def item():
    post = {'author': 'Don', 'tags': ['foo', 'bar'], 'title':'test title', 'body': 'This is the body of post 1.<br/> This is some more long running text that should build out a better view of how it might look on the page. Super cool, if you think about it. Just type, type, typing away as if I didnt have a care in the world. There is nothing here to see. Just words and more words. So damn fun, huh?'}
    return render_template('item.html', title='foo', post=post)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', 
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])