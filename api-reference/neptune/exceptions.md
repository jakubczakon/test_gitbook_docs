Module neptune.exceptions
=========================

Classes
-------

`CannotResolveHostname(host)`
:   Common base class for all non-exit exceptions.

    ### Ancestors (in MRO)

    * neptune.exceptions.NeptuneException
    * builtins.Exception
    * builtins.BaseException

`DeprecatedApiToken(app_url)`
:   Common base class for all non-exit exceptions.

    ### Ancestors (in MRO)

    * neptune.exceptions.NeptuneException
    * builtins.Exception
    * builtins.BaseException

`FileNotFound(path)`
:   Common base class for all non-exit exceptions.

    ### Ancestors (in MRO)

    * neptune.exceptions.NeptuneException
    * builtins.Exception
    * builtins.BaseException

`IncorrectProjectQualifiedName(project_qualified_name)`
:   Common base class for all non-exit exceptions.

    ### Ancestors (in MRO)

    * neptune.exceptions.NeptuneException
    * builtins.Exception
    * builtins.BaseException

`InvalidChannelValue(expected_type, actual_type)`
:   Common base class for all non-exit exceptions.

    ### Ancestors (in MRO)

    * neptune.exceptions.NeptuneException
    * builtins.Exception
    * builtins.BaseException

`InvalidChannelX(x)`
:   Common base class for all non-exit exceptions.

    ### Ancestors (in MRO)

    * neptune.exceptions.NeptuneException
    * builtins.Exception
    * builtins.BaseException

`InvalidNeptuneBackend(provided_backend_name)`
:   Common base class for all non-exit exceptions.

    ### Ancestors (in MRO)

    * neptune.exceptions.NeptuneException
    * builtins.Exception
    * builtins.BaseException

`InvalidNotebookPath(path)`
:   Common base class for all non-exit exceptions.

    ### Ancestors (in MRO)

    * neptune.exceptions.NeptuneException
    * builtins.Exception
    * builtins.BaseException

`LibraryNotInstalled(library)`
:   Common base class for all non-exit exceptions.

    ### Ancestors (in MRO)

    * neptune.exceptions.NeptuneException
    * builtins.Exception
    * builtins.BaseException

`MissingApiToken()`
:   Common base class for all non-exit exceptions.

    ### Ancestors (in MRO)

    * neptune.exceptions.NeptuneException
    * builtins.Exception
    * builtins.BaseException

`MissingProjectQualifiedName()`
:   Common base class for all non-exit exceptions.

    ### Ancestors (in MRO)

    * neptune.exceptions.NeptuneException
    * builtins.Exception
    * builtins.BaseException

`NeptuneException(*args, **kwargs)`
:   Common base class for all non-exit exceptions.

    ### Ancestors (in MRO)

    * builtins.Exception
    * builtins.BaseException

    ### Descendants

    * neptune.api_exceptions.NeptuneApiException
    * neptune.api_exceptions.SSLError
    * neptune.exceptions.CannotResolveHostname
    * neptune.exceptions.DeprecatedApiToken
    * neptune.exceptions.FileNotFound
    * neptune.exceptions.IncorrectProjectQualifiedName
    * neptune.exceptions.InvalidChannelValue
    * neptune.exceptions.InvalidChannelX
    * neptune.exceptions.InvalidNeptuneBackend
    * neptune.exceptions.InvalidNotebookPath
    * neptune.exceptions.LibraryNotInstalled
    * neptune.exceptions.MissingApiToken
    * neptune.exceptions.MissingProjectQualifiedName
    * neptune.exceptions.NoChannelValue
    * neptune.exceptions.NoExperimentContext
    * neptune.exceptions.NotADirectory
    * neptune.exceptions.NotAFile
    * neptune.exceptions.Uninitialized
    * neptune.exceptions.UnsupportedClientVersion

`NoChannelValue()`
:   Common base class for all non-exit exceptions.

    ### Ancestors (in MRO)

    * neptune.exceptions.NeptuneException
    * builtins.Exception
    * builtins.BaseException

`NoExperimentContext()`
:   Common base class for all non-exit exceptions.

    ### Ancestors (in MRO)

    * neptune.exceptions.NeptuneException
    * builtins.Exception
    * builtins.BaseException

`NotADirectory(path)`
:   Common base class for all non-exit exceptions.

    ### Ancestors (in MRO)

    * neptune.exceptions.NeptuneException
    * builtins.Exception
    * builtins.BaseException

`NotAFile(path)`
:   Common base class for all non-exit exceptions.

    ### Ancestors (in MRO)

    * neptune.exceptions.NeptuneException
    * builtins.Exception
    * builtins.BaseException

`Uninitialized()`
:   Common base class for all non-exit exceptions.

    ### Ancestors (in MRO)

    * neptune.exceptions.NeptuneException
    * builtins.Exception
    * builtins.BaseException

`UnsupportedClientVersion(version, minVersion, maxVersion)`
:   Common base class for all non-exit exceptions.

    ### Ancestors (in MRO)

    * neptune.exceptions.NeptuneException
    * builtins.Exception
    * builtins.BaseException