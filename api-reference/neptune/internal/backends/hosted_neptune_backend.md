Module neptune.internal.backends.hosted_neptune_backend
=======================================================

Classes
-------

`HostedNeptuneBackend(**kwargs)`
:   

    ### Ancestors (in MRO)

    * neptune.backend.Backend

    ### Instance variables

    `api_address`
    :

    `display_address`
    :

    `proxies`
    :

    ### Methods

    `create_channel(*args, **kwargs)`
    :

    `create_checkpoint(*args, **kwargs)`
    :

    `create_experiment(*args, **kwargs)`
    :

    `create_hardware_metric(*args, **kwargs)`
    :

    `create_notebook(*args, **kwargs)`
    :

    `create_system_channel(*args, **kwargs)`
    :

    `download_data(*args, **kwargs)`
    :

    `extract_experiment_output(self, experiment, data)`
    :

    `extract_experiment_source(self, experiment, data)`
    :

    `get_channel_points_csv(*args, **kwargs)`
    :

    `get_download_request(*args, **kwargs)`
    :

    `get_experiment(*args, **kwargs)`
    :

    `get_last_checkpoint(*args, **kwargs)`
    :

    `get_leaderboard_entries(*args, **kwargs)`
    :

    `get_metrics_csv(*args, **kwargs)`
    :

    `get_notebook(*args, **kwargs)`
    :

    `get_project(*args, **kwargs)`
    :

    `get_project_members(*args, **kwargs)`
    :

    `get_projects(*args, **kwargs)`
    :

    `get_system_channels(*args, **kwargs)`
    :

    `mark_failed(*args, **kwargs)`
    :

    `mark_succeeded(*args, **kwargs)`
    :

    `ping_experiment(*args, **kwargs)`
    :

    `prepare_output_download_reuqest(*args, **kwargs)`
    :

    `prepare_source_download_reuqest(*args, **kwargs)`
    :

    `reset_channel(*args, **kwargs)`
    :

    `rm_data(*args, **kwargs)`
    :

    `send_channels_values(*args, **kwargs)`
    :

    `send_hardware_metric_reports(*args, **kwargs)`
    :

    `update_experiment(*args, **kwargs)`
    :

    `update_tags(*args, **kwargs)`
    :

    `upload_experiment_output(self, experiment, data, progress_indicator)`
    :

    `upload_experiment_source(self, experiment, data, progress_indicator)`
    :