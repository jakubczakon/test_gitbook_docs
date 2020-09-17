Module neptune.api_exceptions
=============================

Classes
-------

`ChannelAlreadyExists(experiment_short_id, channel_name)`
:   Common base class for all non-exit exceptions.

    ### Ancestors (in MRO)

    * neptune.api_exceptions.NeptuneApiException
    * neptune.exceptions.NeptuneException
    * builtins.Exception
    * builtins.BaseException

`ChannelDoesNotExist(experiment_short_id, channel_name)`
:   Common base class for all non-exit exceptions.

    ### Ancestors (in MRO)

    * neptune.api_exceptions.NeptuneApiException
    * neptune.exceptions.NeptuneException
    * builtins.Exception
    * builtins.BaseException

`ChannelNotFound(channel_id)`
:   Common base class for all non-exit exceptions.

    ### Ancestors (in MRO)

    * neptune.api_exceptions.NeptuneApiException
    * neptune.exceptions.NeptuneException
    * builtins.Exception
    * builtins.BaseException

`ChannelsValuesSendBatchError(experiment_short_id, batch_errors)`
:   Common base class for all non-exit exceptions.

    ### Ancestors (in MRO)

    * neptune.api_exceptions.NeptuneApiException
    * neptune.exceptions.NeptuneException
    * builtins.Exception
    * builtins.BaseException

`ConnectionLost()`
:   Common base class for all non-exit exceptions.

    ### Ancestors (in MRO)

    * neptune.api_exceptions.NeptuneApiException
    * neptune.exceptions.NeptuneException
    * builtins.Exception
    * builtins.BaseException

`ExperimentAlreadyFinished(experiment_short_id)`
:   Common base class for all non-exit exceptions.

    ### Ancestors (in MRO)

    * neptune.api_exceptions.NeptuneApiException
    * neptune.exceptions.NeptuneException
    * builtins.Exception
    * builtins.BaseException

`ExperimentLimitReached()`
:   Common base class for all non-exit exceptions.

    ### Ancestors (in MRO)

    * neptune.api_exceptions.NeptuneApiException
    * neptune.exceptions.NeptuneException
    * builtins.Exception
    * builtins.BaseException

`ExperimentNotFound(experiment_short_id, project_qualified_name)`
:   Common base class for all non-exit exceptions.

    ### Ancestors (in MRO)

    * neptune.api_exceptions.NeptuneApiException
    * neptune.exceptions.NeptuneException
    * builtins.Exception
    * builtins.BaseException

`ExperimentValidationError(*args, **kwargs)`
:   Common base class for all non-exit exceptions.

    ### Ancestors (in MRO)

    * neptune.api_exceptions.NeptuneApiException
    * neptune.exceptions.NeptuneException
    * builtins.Exception
    * builtins.BaseException

`Forbidden()`
:   Common base class for all non-exit exceptions.

    ### Ancestors (in MRO)

    * neptune.api_exceptions.NeptuneApiException
    * neptune.exceptions.NeptuneException
    * builtins.Exception
    * builtins.BaseException

`InvalidApiKey()`
:   Common base class for all non-exit exceptions.

    ### Ancestors (in MRO)

    * neptune.api_exceptions.NeptuneApiException
    * neptune.exceptions.NeptuneException
    * builtins.Exception
    * builtins.BaseException

`NamespaceNotFound(namespace_name)`
:   Common base class for all non-exit exceptions.

    ### Ancestors (in MRO)

    * neptune.api_exceptions.NeptuneApiException
    * neptune.exceptions.NeptuneException
    * builtins.Exception
    * builtins.BaseException

`NeptuneApiException(*args, **kwargs)`
:   Common base class for all non-exit exceptions.

    ### Ancestors (in MRO)

    * neptune.exceptions.NeptuneException
    * builtins.Exception
    * builtins.BaseException

    ### Descendants

    * neptune.api_exceptions.ChannelAlreadyExists
    * neptune.api_exceptions.ChannelDoesNotExist
    * neptune.api_exceptions.ChannelNotFound
    * neptune.api_exceptions.ChannelsValuesSendBatchError
    * neptune.api_exceptions.ConnectionLost
    * neptune.api_exceptions.ExperimentAlreadyFinished
    * neptune.api_exceptions.ExperimentLimitReached
    * neptune.api_exceptions.ExperimentNotFound
    * neptune.api_exceptions.ExperimentValidationError
    * neptune.api_exceptions.Forbidden
    * neptune.api_exceptions.InvalidApiKey
    * neptune.api_exceptions.NamespaceNotFound
    * neptune.api_exceptions.NotebookNotFound
    * neptune.api_exceptions.PathInProjectNotFound
    * neptune.api_exceptions.ProjectNotFound
    * neptune.api_exceptions.ServerError
    * neptune.api_exceptions.StorageLimitReached
    * neptune.api_exceptions.Unauthorized

`NotebookNotFound(notebook_id, project=None)`
:   Common base class for all non-exit exceptions.

    ### Ancestors (in MRO)

    * neptune.api_exceptions.NeptuneApiException
    * neptune.exceptions.NeptuneException
    * builtins.Exception
    * builtins.BaseException

`PathInProjectNotFound(path, project_identifier)`
:   Common base class for all non-exit exceptions.

    ### Ancestors (in MRO)

    * neptune.api_exceptions.NeptuneApiException
    * neptune.exceptions.NeptuneException
    * builtins.Exception
    * builtins.BaseException

`ProjectNotFound(project_identifier)`
:   Common base class for all non-exit exceptions.

    ### Ancestors (in MRO)

    * neptune.api_exceptions.NeptuneApiException
    * neptune.exceptions.NeptuneException
    * builtins.Exception
    * builtins.BaseException

`SSLError()`
:   Common base class for all non-exit exceptions.

    ### Ancestors (in MRO)

    * neptune.exceptions.NeptuneException
    * builtins.Exception
    * builtins.BaseException

`ServerError()`
:   Common base class for all non-exit exceptions.

    ### Ancestors (in MRO)

    * neptune.api_exceptions.NeptuneApiException
    * neptune.exceptions.NeptuneException
    * builtins.Exception
    * builtins.BaseException

`StorageLimitReached()`
:   Common base class for all non-exit exceptions.

    ### Ancestors (in MRO)

    * neptune.api_exceptions.NeptuneApiException
    * neptune.exceptions.NeptuneException
    * builtins.Exception
    * builtins.BaseException

`Unauthorized()`
:   Common base class for all non-exit exceptions.

    ### Ancestors (in MRO)

    * neptune.api_exceptions.NeptuneApiException
    * neptune.exceptions.NeptuneException
    * builtins.Exception
    * builtins.BaseException