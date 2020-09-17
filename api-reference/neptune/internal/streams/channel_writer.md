Module neptune.internal.streams.channel_writer
==============================================

Classes
-------

`ChannelWriter(experiment, channel_name, channel_namespace=ChannelNamespace.USER)`
:   

    ### Methods

    `write(self, data)`
    :

`TimeOffsetGenerator(start)`
:   

    ### Methods

    `next(self)`
    :   This method returns the number of milliseconds from start.
        It returns a float, with microsecond granularity.
        
        Since on Windows, datetime.now() has actually a millisecond granularity,
        we remember the last returned value and in case of a collision, we add a microsecond.