Module neptune.backend
======================

Classes
-------

`Backend()`
:   

    ### Descendants

    * neptune.internal.backends.hosted_neptune_backend.HostedNeptuneBackend
    * neptune.internal.backends.offline_backend.OfflineBackend

    ### Instance variables

    `api_address`
    :

    `display_address`
    :

    `proxies`
    :

    ### Methods

    `create_channel(self, experiment, name, channel_type)`
    :

    `create_checkpoint(self, notebook_id, jupyter_path, _file)`
    :

    `create_experiment(self, project, name, description, params, properties, tags, abortable, monitored, git_info, hostname, entrypoint, notebook_id, checkpoint_id)`
    :

    `create_hardware_metric(self, experiment, metric)`
    :

    `create_notebook(self, project)`
    :

    `create_system_channel(self, experiment, name, channel_type)`
    :

    `download_data(self, project, path, destination)`
    :

    `extract_experiment_output(self, experiment, data)`
    :

    `extract_experiment_source(self, experiment, data)`
    :

    `get_channel_points_csv(self, experiment, channel_internal_id)`
    :

    `get_experiment(self, experiment_id)`
    :

    `get_last_checkpoint(self, project, notebook_id)`
    :

    `get_leaderboard_entries(self, project, entry_types, ids, states, owners, tags, min_running_time)`
    :

    `get_metrics_csv(self, experiment)`
    :

    `get_notebook(self, project, notebook_id)`
    :

    `get_project(self, project_qualified_name)`
    :

    `get_project_members(self, project_identifier)`
    :

    `get_projects(self, namespace)`
    :

    `get_system_channels(self, experiment)`
    :

    `mark_failed(self, experiment, traceback)`
    :

    `mark_succeeded(self, experiment)`
    :

    `ping_experiment(self, experiment)`
    :

    `reset_channel(self, channel_id)`
    :

    `send_channels_values(self, experiment, channels_with_values)`
    :

    `send_hardware_metric_reports(self, experiment, metrics, metric_reports)`
    :

    `update_experiment(self, experiment, properties)`
    :

    `update_tags(self, experiment, tags_to_add, tags_to_delete)`
    :

    `upload_experiment_output(self, experiment, data, progress_indicator)`
    :

    `upload_experiment_source(self, experiment, data, progress_indicator)`
    :