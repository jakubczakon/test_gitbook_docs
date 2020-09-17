Module neptune.internal.channels.channels_values_sender
=======================================================

Classes
-------

`ChannelsValuesSender(experiment)`
:   

    ### Methods

    `join(self)`
    :

    `send(self, channel_name, channel_type, channel_value, channel_namespace=ChannelNamespace.USER)`
    :

`ChannelsValuesSendingThread(experiment, values_queue)`
:   A class that represents a thread of control.
    
    This class can be safely subclassed in a limited fashion. There are two ways
    to specify the activity: by passing a callable object to the constructor, or
    by overriding the run() method in a subclass.
    
    This constructor should always be called with keyword arguments. Arguments are:
    
    *group* should be None; reserved for future extension when a ThreadGroup
    class is implemented.
    
    *target* is the callable object to be invoked by the run()
    method. Defaults to None, meaning nothing is called.
    
    *name* is the thread name. By default, a unique name is constructed of
    the form "Thread-N" where N is a small decimal number.
    
    *args* is the argument tuple for the target invocation. Defaults to ().
    
    *kwargs* is a dictionary of keyword arguments for the target
    invocation. Defaults to {}.
    
    If a subclass overrides the constructor, it must make sure to invoke
    the base class constructor (Thread.__init__()) before doing anything
    else to the thread.

    ### Ancestors (in MRO)

    * neptune.internal.threads.neptune_thread.NeptuneThread
    * threading.Thread