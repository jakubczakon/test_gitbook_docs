Module neptune.internal.storage.storage_utils
=============================================

Functions
---------

    
`normalize_file_name(name)`
:   

    
`scan_unique_upload_entries(upload_entries)`
:   Returns upload entries for all files that could be found for given upload entries.
    In case of directory as upload entry, files we be taken from all subdirectories recursively.
    Any duplicated entries are removed.

    
`split_upload_files(upload_entries, max_package_size=1048576, max_files=500)`
:   

    
`upload_to_storage(upload_entries, upload_api_fun, upload_tar_api_fun, warn_limit=None, **kwargs)`
:   

Classes
-------

`LoggingProgressIndicator(total, frequency=10)`
:   

    ### Ancestors (in MRO)

    * neptune.internal.storage.storage_utils.ProgressIndicator

    ### Methods

    `complete(self)`
    :

    `progress(self, steps)`
    :

`ProgressIndicator()`
:   

    ### Descendants

    * neptune.internal.storage.storage_utils.LoggingProgressIndicator
    * neptune.internal.storage.storage_utils.SilentProgressIndicator

    ### Methods

    `complete(self)`
    :

    `progress(self, steps)`
    :

`SilentProgressIndicator()`
:   

    ### Ancestors (in MRO)

    * neptune.internal.storage.storage_utils.ProgressIndicator

    ### Methods

    `complete(self)`
    :

    `progress(self, steps)`
    :

`UploadEntry(source_path, target_path)`
:   

    ### Methods

    `is_stream(self)`
    :

    `to_str(self)`
    :   Returns the string representation of the model

`UploadPackage()`
:   

    ### Methods

    `is_empty(self)`
    :

    `reset(self)`
    :

    `to_str(self)`
    :   Returns the string representation of the model

    `update(self, entry, size)`
    :