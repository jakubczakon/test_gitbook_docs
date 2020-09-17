Module neptune.internal.threads.neptune_thread
==============================================

Classes
-------

`NeptuneThread(is_daemon)`
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

    * threading.Thread

    ### Descendants

    * neptune.internal.channels.channels_values_sender.ChannelsValuesSendingThread
    * neptune.internal.threads.aborting_thread.AbortingThread
    * neptune.internal.threads.hardware_metric_reporting_thread.HardwareMetricReportingThread
    * neptune.internal.threads.ping_thread.PingThread

    ### Methods

    `interrupt(self)`
    :

    `run(self)`
    :   Method representing the thread's activity.
        
        You may override this method in a subclass. The standard run() method
        invokes the callable object passed to the object's constructor as the
        target argument, if any, with sequential and keyword arguments taken
        from the args and kwargs arguments, respectively.

    `should_continue_running(self)`
    :