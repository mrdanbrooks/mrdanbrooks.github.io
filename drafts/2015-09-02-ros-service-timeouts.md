---
layout: post
title: ROS Service call custom timeouts
tags: linux python
category: programming
year: 2015
month: 09
day: 02
published: true
summary: ROS Service calls are blocking functions. Here is a workaround.
---

ROS has several [communication patterns](http://wiki.ros.org/ROS/Patterns/Communication) can be used to allow interprocess communication.
These include Topics (publish/subscribe), Services (request/reply), and Actions  (asynchronous task control).

Service calls have been designed to mimic the way in which regular functions are written and used.
This is nice since it is the behavior most people would want and expect.
On the server side, the function is often written almost exactly the same way you would write any other function, and then wrapped as a ROS Service to be exposed to other processes (ROS Nodes).
On the client side, nodes receive a callable function that is called in almost the same way as any other function.
This makes ROS Services a very attractive system for creating APIs to control more complex (and sometimes hidden) functionality. 

Unfortunately, Services in ROS have a few problems. 
The most immediately obvious problem is that there are far fewer tools available for working with Services then there are for working with their publish/subscribe counterparts (Topics).
For example, it is currently not possible to monitor or log transactions between service clients and service servers.

Today, however, I ran into a much less obvious problem with Services. 
Some developers had used ROS Services to create an API for a product I was working with.
Everything would run smoothly most of the time.
However, occasionally the service call would take MUCH longer to return - so much longer that it was causing problems.
Thus, I wanted to be able to set an upper bound the length of time the service would run for.
If the computation could not be completed within a certain time period, the results would no longer be useful to me and I wanted to start a new computation as soon as possible with my new parameters. 

But is no built-in way to do this.
Service calls block the client from continuing to execute until they return a value.
Furthermore, there is no mechanism built into service calls to allow a client to specify to a server how long the client is willing to wait for an answer. 
The result is that the client is forced to wait for server to return a value to it.

One possible solution to this problem is for the service server to add a timeout parameter to the service call.
However, this is only realistic in cases where the author of the client can alter or convince someone else to alter the code for the service server.
In the case of the commercial product I was using, this was not an option.

The solution I came up with was to execute the service from a separate thread, allowing the call to take as long as it likes.
If it takes too long, my code will simply continue on using a default value while the thread finishes running its course in the background.

```
import time
import threading
class ServiceTimeouter(object):
    """ Ros services cannot be timed out. Occasionally the IK solver would take
        up to 5 seconds to respond. This is a workaround class. """
    def __init__(self, srv, param=(), kwargs={}):
        self.srv = srv
        self.param = param
        self.kwargs = kwargs
        self.timeout = 0.5
        self.retval = None
        self.returned = False
        self.lock = threading.Lock()
        self.thread = threading.Thread(target=self._call_thread)
    def _call_thread(self):
        try:
            self.retval = self.srv(*self.param, **self.kwargs)
            self.returned = True
        except rospy.ServiceException, e:
            rospy.loginfo("Service call failed: %s" % (e,))
        except AttributeError:
            rospy.loginfo("Socket.close() exception. Socket has become 'None'")
    def call(self):
        self.thread.start()
        timeout = time.time() + self.timeout
        while time.time() < timeout and self.thread.isAlive():
            time.sleep(0.001)
        if not self.returned:
            print "timed out"
            return None
        return self.retval
```
