# Learning - microblog
The microblog example is my adaptation of the great blog series by Miguel
Grinberg, "[The Flask Mega-Tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)"
that I am using to learn the Flask framework.

## Configuration
Configuration for this example assumes that Python and VirtualEnv are installed
on the development machine. My development machine is Windows 10.  

To configure, do the following:
1. In the **cmd prompt**, navigate to the local Git clone was installed. For me, this was on my *c:\myPy\learning\microblog*. Type in the following:
```python
> C:\myPy\learning\microblog VirtualEnv Flask
```
This will lay down VirtualEnv files

Start the VirtualEnv
```cmd
c:\myPy\learning\microblog> cd flask\scripts
c:\myPy\learning\microblog\flask\scripts> activate
(flask) C:\myPy\learning\microblog\flask\scripts>
```

Install Flask in the VirtualEnv
```
(flask) C:\myPy\learning\microblog\flask\scripts> pip install flask
```

Next, run the application:
```
(flask) c:\myPal\learning\microblog\flask\scripts> cd ../..
(flask) c:\myPy\learning\microblog> python run.py
```
