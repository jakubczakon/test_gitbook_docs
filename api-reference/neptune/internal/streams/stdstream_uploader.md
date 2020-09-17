Module neptune.internal.streams.stdstream_uploader
==================================================

Classes
-------

`StdErrWithUpload(experiment)`
:   

    ### Ancestors (in MRO)

    * neptune.internal.streams.stdstream_uploader.StdStreamWithUpload

    ### Methods

    `close(self)`
    :

`StdOutWithUpload(experiment)`
:   

    ### Ancestors (in MRO)

    * neptune.internal.streams.stdstream_uploader.StdStreamWithUpload

    ### Methods

    `close(self)`
    :

`StdStreamWithUpload(experiment, channel_name, stream)`
:   

    ### Descendants

    * neptune.internal.streams.stdstream_uploader.StdErrWithUpload
    * neptune.internal.streams.stdstream_uploader.StdOutWithUpload

    ### Methods

    `fileno(self)`
    :

    `flush(self)`
    :

    `isatty(self)`
    :

    `write(self, data)`
    :