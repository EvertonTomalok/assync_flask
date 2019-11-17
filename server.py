
# Start with a basic flask app webpage.
from flask_socketio import SocketIO, emit
from flask import Flask, render_template, url_for, copy_current_request_context
from random import random
from time import sleep
from threading import Thread
from requests import get


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True

#turn the flask app into a socketio app
socketio = SocketIO(app)

#random number Generator Thread
thread = Thread()
counter = 0

class RandomThread(Thread):
    def __init__(self):
        self.delay = 5
        super(RandomThread, self).__init__()

    def randomNumberGenerator(self):
        """
        Generate a random number every 1 second and emit to a socketio instance (broadcast)
        Ideally to be run in a separate thread?
        """
        #infinite loop of magical random numbers
        while counter > 0:
            try:
                response = get("http://3.15.173.81:5050/comandas/active").json()
                socketio.emit('newnumber', {'number': response}, namespace='/test')
            except Exception as err:
                print(err, type(err))

            sleep(self.delay)


    def run(self):
        self.randomNumberGenerator()


@app.route('/')
def index():
    #only by sending this page first will the client be connected to the socketio instance
    return render_template('index.html')

@socketio.on('connect', namespace='/test')
def test_connect():
    # need visibility of the global thread object
    global thread, counter
    counter += 1
    print(f'Client connected actual: {counter}')    

    #Start the random number generator thread only if the thread has not been started before.
    if not thread.is_alive():
        thread = RandomThread()
        thread.start()
        print("Starting Thread: ", counter)

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    global counter

    print(f'Client disconnected. Actual: {counter}, then remove one: {counter - 1}')

    if counter > 0:
        counter -= 1


if __name__ == '__main__':
    socketio.run(app)
