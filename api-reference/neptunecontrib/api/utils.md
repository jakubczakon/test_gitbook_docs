Module neptunecontrib.api.utils
===============================

Functions
---------

    
`concat_experiments_on_channel(experiments, channel_name)`
:   Combines channel values from experiments into one dataframe.
    
    This function helps to compare channel values from a list of experiments
    by combining them in a dataframe. E.g: Say we want to extract the `log_loss`
    channel values for a list of experiments. The resulting dataframe will have
    ['id','x_log_loss','y_log_loss'] columns.
    
    Args:
        experiments(list): list of `neptune.experiments.Experiment` objects.
        channel_name(str): name of the channel for which we want to extract values.
    
    Returns:
        `pandas.DataFrame`: Dataframe of ['id','x_CHANNEL_NAME','y_CHANNEL_NAME']
        values concatenated from a list of experiments.
    
    Examples:
        Instantiate a session::
    
            from neptune.sessions import Session
            session = Session()
    
        Fetch a project and a list of experiments::
    
            project = session.get_projects('neptune-ai')['neptune-ai/Salt-Detection']
            experiments = project.get_experiments(state=['aborted'], owner=['neyo'], min_running_time=100000)
    
        Construct a channel value dataframe::
    
            from neptunecontrib.api.utils import concat_experiments_on_channel
            compare_df = concat_experiments_on_channel(experiments,'unet_0 epoch_val iout loss')
    
    Note:
        If an experiment in the list of experiments does not contain the channel with a specified channel_name
        it will be omitted.

    
`extract_project_progress_info(leadearboard, metric_colname, time_colname='finished')`
:   Extracts the project progress information from the experiment view.
    
    This function takes the experiment view (leaderboard) and extracts the information
    that is important for analysing the project progress. It creates additional columns
    `metric` (actual experiment metric), `metric_best` (best metric score to date)),
    `running_time_day` (total amount of experiment running time for a given day in hours),
    'experiment_count_day' (total number of experiments ran in a given day).
    
    This function is usually used with the `plot_project_progress` from `neptunecontrib.viz.projects`.
    
    Args:
        leadearboard(`pandas.DataFrame`): Dataframe containing the experiment view of the project.
            It can be extracted via `project.get_leaderboard()`.
        metric_colname(str): name of the column containing the metric of interest.
        time_colname(str): name of the column containing the timestamp. It can be either `finished`
            or `created`. Default is 'finished'.
    
    Returns:
        `pandas.DataFrame`: Dataframe of ['id', 'metric', 'metric_best', 'running_time',
        'running_time_day', 'experiment_count_day', 'owner', 'tags', 'timestamp', 'timestamp_day']
        columns.
    
    Examples:
        Instantiate a session::
    
            from neptune.sessions import Session
            session = Session()
    
        Fetch a project and the experiment view of that project::
    
            project = session.get_projects('neptune-ai')['neptune-ai/Salt-Detection']
            leaderboard = project.get_leaderboard()
    
        Create a progress info dataframe::
    
            from neptunecontrib.api.utils import extract_project_progress_info
            progress_df = extract_project_progress_info(leadearboard,
                                                        metric_colname='channel_IOUT',
                                                        time_colname='finished')

    
`get_channel_columns(columns)`
:   Filters leaderboard columns to get the channel column names.
    
    Args:
        columns(iterable): Iterable of leaderboard column names.
    
    Returns:
        list: A list of channel column names.

    
`get_parameter_columns(columns)`
:   Filters leaderboard columns to get the parameter column names.
    
    Args:
        columns(iterable): Iterable of leaderboard column names.
    
    Returns:
        list: A list of channel parameter names.

    
`get_pickle(filename, experiment)`
:   Downloads pickled artifact object from Neptune and returns a Python object.
    
    Downloads the pickled object from artifacts of given experiment,
     loads it to memory and returns a Python object.
    
    Args:
        filename(str): filename under which object will be saved to Neptune.
        experiment(`neptune.experiments.Experiment`): Neptune experiment.
    
    Examples:
        Initialize Neptune::
    
            import neptune
    
            project = neptune.init('USER_NAME/PROJECT_NAME')
    
        Choose Neptune experiment::
    
            experiment = project.get_experiments(id=['PRO-101'])[0]
    
        Get your pickled object from experiment artifacts::
    
            from neptunecontrib.api import get_pickle
    
            results = get_pickle('results.pkl', experiment)

    
`get_property_columns(columns)`
:   Filters leaderboard columns to get the property column names.
    
    Args:
        columns(iterable): Iterable of leaderboard column names.
    
    Returns:
        list: A list of channel property names.

    
`get_system_columns(columns)`
:   Filters leaderboard columns to get the system column names.
    
    Args:
        columns(iterable): Iterable of leaderboard column names.
    
    Returns:
        list: A list of channel system names.

    
`log_pickle(filename, obj, experiment=None)`
:   Logs picklable object to Neptune.
    
    Pickles and logs your object to Neptune under specified filename.
    
    Args:
        obj: Picklable object.
        filename(str): filename under which object will be saved to Neptune.
        experiment(`neptune.experiments.Experiment`): Neptune experiment.
    
    Examples:
        Initialize Neptune::
    
            import neptune
            neptune.init('USER_NAME/PROJECT_NAME')
    
        Create RandomForest object and log to Neptune::
    
            from sklearn.ensemble import RandomForestClassifier
            from neptunecontrib.api import log_pickle
    
            neptune.create_experiment()
    
            rf = RandomForestClassifier()
            log_pickle('rf.pkl', rf)

    
`strip_prefices(columns, prefices)`
:   Filters leaderboard columns to get the system column names.
    
    Args:
        columns(iterable): Iterable of leaderboard column names.
        prefices(list): List of prefices to strip. You can choose one of
            ['channel_', 'parameter_', 'property_']
    
    Returns:
        list: A list of clean column names.