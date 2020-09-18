# neptune

## Sub-modules

* neptune.api\_exceptions
* neptune.backend
* neptune.checkpoint
* neptune.constants
* neptune.envs
* neptune.exceptions
* neptune.experiments
* neptune.git\_info
* neptune.internal
* neptune.model
* neptune.notebook
* neptune.oauth
* neptune.patterns
* neptune.projects
* neptune.sessions
* neptune.utils

## Variables

`ANONYMOUS` : Anonymous user API token. You can pass this value as api\_token during init\(\) call, either by an environment variable or passing it directly

## Functions

`append_tag(tag, *tags)` : Append tag\(s\) to the experiment on the top of experiments view.

```text
Alias for: :meth:`~neptune.experiments.Experiment.append_tag`
```

`append_tags(tag, *tags)` : Append tag\(s\) to the experiment on the top of experiments view.

```text
Alias for: :meth:`~neptune.experiments.Experiment.append_tags`
```

`create_experiment(name=None, description=None, params=None, properties=None, tags=None, upload_source_files=None, abort_callback=None, logger=None, upload_stdout=True, upload_stderr=True, send_hardware_metrics=True, run_monitoring_thread=True, handle_uncaught_exceptions=True, git_info=None, hostname=None, notebook_id=None)` : Create and start Neptune experiment.

```text
Alias for: :meth:`~neptune.projects.Project.create_experiment`
```

`delete_artifacts(path)` : Delete an artifact \(file/directory\) from experiment storage.

```text
Alias for :meth:`~neptune.experiments.Experiment.delete_artifacts`
```

`get_experiment()` :

`init(project_qualified_name=None, api_token=None, proxies=None, backend=None)` : Initialize `Neptune client library <https://github.com/neptune-ai/neptune-client>`\_ to work with specific project.

```text
Authorize user, sets value of global variable ``project`` to :class:`~neptune.projects.Project` object
that can be used to create or list experiments, notebooks, etc.

Args:
    project_qualified_name (:obj:`str`, optional, default is ``None``):
        Qualified name of a project in a form of ``namespace/project_name``.
        If ``None``, the value of ``NEPTUNE_PROJECT`` environment variable will be taken.

    api_token (:obj:`str`, optional, default is ``None``):
        User's API token. If ``None``, the value of ``NEPTUNE_API_TOKEN`` environment variable will be taken.

        .. note::

            It is strongly recommended to use ``NEPTUNE_API_TOKEN`` environment variable rather than
            placing your API token in plain text in your source code.

    proxies (:obj:`dict`, optional, default is ``None``):
        Argument passed to HTTP calls made via the `Requests <https://2.python-requests.org/en/master/>`_ library.
        For more information see their proxies
        `section <https://2.python-requests.org/en/master/user/advanced/#proxies>`_.

        .. note::

            Only `http` and `https` keys are supported by all features.

        .. deprecated :: 0.4.4

        Instead, use:

        .. code :: python3

            from neptune import HostedNeptuneBackend
            neptune.init(backend=HostedNeptuneBackend(proxies=...))

    backend (:class:`~neptune.Backend`, optional, default is ``None``):
        By default, Neptune client library sends logs, metrics, images, etc to Neptune servers:
        either publicly available SaaS, or an on-premises installation.

        You can also pass the default backend instance explicitly to specify its parameters:

        .. code :: python3

            from neptune import HostedNeptuneBackend
            neptune.init(backend=HostedNeptuneBackend(...))

        Passing an instance of :class:`~neptune.OfflineBackend` makes your code run without communicating
        with Neptune servers.

        .. code :: python3

            from neptune import OfflineBackend
            neptune.init(backend=OfflineBackend())

        .. note::
            Instead of passing a ``neptune.OfflineBackend`` instance as ``backend``, you can set an
            environment variable ``NEPTUNE_BACKEND=offline`` to override the default behaviour.

Returns:
    :class:`~neptune.projects.Project` object that is used to create or list experiments, notebooks, etc.

Raises:
    `MissingApiToken`: When ``api_token`` is None and ``NEPTUNE_API_TOKEN`` environment variable was not set.
    `MissingProjectQualifiedName`: When ``project_qualified_name`` is None
        and ``NEPTUNE_PROJECT`` environment variable was not set.
    `InvalidApiKey`: When given ``api_token`` is malformed.
    `Unauthorized`: When given ``api_token`` is invalid.

Examples:

    .. code:: python3

        # minimal invoke
        neptune.init()

        # specifying project name
        neptune.init('jack/sandbox')

        # running offline
        neptune.init(backend=neptune.OfflineBackend())
```

`log_artifact(artifact, destination=None)` : Save an artifact \(file\) in experiment storage.

```text
Alias for :meth:`~neptune.experiments.Experiment.log_artifact`
```

`log_image(log_name, x, y=None, image_name=None, description=None, timestamp=None)` : Log image data in Neptune.

```text
Alias for :meth:`~neptune.experiments.Experiment.log_image`
```

`log_metric(log_name, x, y=None, timestamp=None)` : Log metrics \(numeric values\) in Neptune.

```text
Alias for :meth:`~neptune.experiments.Experiment.log_metric`
```

`log_text(log_name, x, y=None, timestamp=None)` : Log text data in Neptune.

```text
Alias for :meth:`~neptune.experiments.Experiment.log_text`
```

`remove_property(key)` : Removes a property with given key.

```text
Alias for: :meth:`~neptune.experiments.Experiment.remove_property`
```

`remove_tag(tag)` : Removes single tag from experiment.

```text
Alias for: :meth:`~neptune.experiments.Experiment.remove_tag`
```

`send_artifact(artifact, destination=None)` : Save an artifact \(file\) in experiment storage.

```text
Alias for :meth:`~neptune.experiments.Experiment.log_artifact`
```

`send_image(channel_name, x, y=None, name=None, description=None, timestamp=None)` : Log image data in Neptune.

```text
Alias for :meth:`~neptune.experiments.Experiment.log_image`
```

`send_metric(channel_name, x, y=None, timestamp=None)` : Log metrics \(numeric values\) in Neptune.

```text
Alias for :meth:`~neptune.experiments.Experiment.log_metric`
```

`send_text(channel_name, x, y=None, timestamp=None)` : Log text data in Neptune.

```text
Alias for :meth:`~neptune.experiments.Experiment.log_text`
```

`set_project(project_qualified_name)` : Setups `Neptune client library <https://github.com/neptune-ai/neptune-client>`\_ to work with specific project.

```text
| Sets value of global variable ``project`` to :class:`~neptune.projects.Project` object
  that can be used to create or list experiments, notebooks, etc.
| If Neptune client library was not previously initialized via :meth:`~neptune.init` call
  it will be initialized with API token taken from ``NEPTUNE_API_TOKEN`` environment variable.

Args:
    project_qualified_name (:obj:`str`):
        Qualified name of a project in a form of ``namespace/project_name``.

Returns:
    :class:`~neptune.projects.Project` object that is used to create or list experiments, notebooks, etc.

Raises:
    `MissingApiToken`: When library was not initialized previously by ``init`` call and
        ``NEPTUNE_API_TOKEN`` environment variable is not set.

Examples:

    .. code:: python3

        # minimal invoke
        neptune.set_project('jack/sandbox')
```

`set_property(key, value)` : Set `key-value` pair as an experiment property.

```text
If property with given ``key`` does not exist, it adds a new one.

Alias for: :meth:`~neptune.experiments.Experiment.set_property`
```

`stop(traceback=None)` : Marks experiment as finished \(succeeded or failed\).

```text
Alias for :meth:`~neptune.experiments.Experiment.stop`
```

