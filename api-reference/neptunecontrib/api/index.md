Module neptunecontrib.api
=========================

Sub-modules
-----------
* neptunecontrib.api.audio
* neptunecontrib.api.chart
* neptunecontrib.api.explainers
* neptunecontrib.api.html
* neptunecontrib.api.table
* neptunecontrib.api.utils
* neptunecontrib.api.video

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

    
`get_filepaths(dirpath='.', extensions=None)`
:   Creates a list of all the files with selected extensions.
    
    Args:
        dirpath(str): Folder from which all files with given extensions should be added to list.
        extensions(list(str) or None): All extensions with which files should be added to the list.
    
    Returns:
        list: A list of filepaths with given extensions that are in the directory or subdirecotries.
    
    Examples:
        Initialize Neptune::
    
             import neptune
             from neptunecontrib.versioning.data import log_data_version
             neptune.init('USER_NAME/PROJECT_NAME')
    
        Create experiment and track all .py files from given directory and subdirs::
    
             with neptune.create_experiment(upload_source_files=get_filepaths(extensions=['.py'])):
                 neptune.send_metric('score', 0.97)

    
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

    
`get_pickled_artifact(experiment, filename)`
:   

    
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

    
`log_audio(path_to_file, audio_name=None, experiment=None)`
:   Logs audio file to 'artifacts/audio' with player.
    
    Logs audio file to the 'artifacts/audio' in the experiment, where you can play it directly from the browser.
    You can also download raw audio file to the local machine.
    Just use "three vertical dots" located to the right from the player.
    
    Args:
        path_to_file (:obj:`str`): Path to audio file.
        audio_name (:obj:`str`, optional, default is ``None``): Name to be displayed in artifacts/audio.
            | If `None`, file name is used.
        experiment (:obj:`neptune.experiments.Experiment`, optional, default is ``None``):
            | For advanced users only. Pass Neptune
              `Experiment <https://docs.neptune.ai/neptune-client/docs/experiment.html#neptune.experiments.Experiment>`_
              object if you want to control to which experiment data is logged.
            | If ``None``, log to currently active, and most recent experiment.
    
    Example:
    
        .. code:: python3
    
            log_audio('audio-file.wav')
            log_audio('/full/path/to/some/other/audio/file.mp3')
            log_audio('/full/path/to/some/other/audio/file.mp3', 'my_audio')
    
    Note:
        Check out how the logged audio file looks in Neptune:
        `here <https://ui.neptune.ai/o/shared/org/showroom/e/SHOW-1485/artifacts?path=audio%2F>`_.

    
`log_chart(name, chart, experiment=None)`
:   Logs charts from matplotlib, plotly, bokeh, and altair to neptune.
    
    Plotly, Bokeh, and Altair charts are converted to interactive HTML objects and then uploaded to Neptune
    as an artifact with path charts/{name}.html.
    
    Matplotlib figures are converted optionally. If plotly is installed, matplotlib figures are converted
    to plotly figures and then converted to interactive HTML and uploaded to Neptune as an artifact with
    path charts/{name}.html. If plotly is not installed, matplotlib figures are converted to PNG images
    and uploaded to Neptune as an artifact with path charts/{name}.png
    
    Args:
        name (:obj:`str`):
            | Name of the chart (without extension) that will be used as a part of artifact's destination.
        chart (:obj:`matplotlib` or :obj:`plotly` Figure):
            | Figure from `matplotlib` or `plotly`. If you want to use global figure from `matplotlib`, you
              can also pass reference to `matplotlib.pyplot` module.
        experiment (:obj:`neptune.experiments.Experiment`, optional, default is ``None``):
            | For advanced users only. Pass Neptune
              `Experiment <https://docs.neptune.ai/neptune-client/docs/experiment.html#neptune.experiments.Experiment>`_
              object if you want to control to which experiment data is logged.
            | If ``None``, log to currently active, and most recent experiment.
    
    Examples:
        Start an experiment::
    
            import neptune
    
            neptune.init(api_token='ANONYMOUS',
                         project_qualified_name='shared/showroom')
            neptune.create_experiment(name='experiment_with_charts')
    
        Create matplotlib figure and log it to Neptune::
    
            import matplotlib.pyplot as plt
    
            fig = plt.figure()
            x = [21,22,23,4,5,6,77,8,9,10,31,32,33,34,35,36,37,18,49,50,100]
            plt.hist(x, bins=5)
            plt.show()
    
            from neptunecontrib.api import log_chart
    
            log_chart('matplotlib_figure', fig)
    
        Create Plotly chart and log it to Neptune::
    
            import plotly.express as px
    
            df = px.data.tips()
            fig = px.histogram(df, x="total_bill", y="tip", color="sex", marginal="rug",
                               hover_data=df.columns)
            fig.show()
    
            from neptunecontrib.api import log_chart
    
            log_chart('plotly_figure', fig)
    
        Create Altair chart and log it to Neptune::
    
            import altair as alt
            from vega_datasets import data
    
            source = data.cars()
    
            chart = alt.Chart(source).mark_circle(size=60).encode(
                            x='Horsepower',
                            y='Miles_per_Gallon',
                            color='Origin',
                            tooltip=['Name', 'Origin', 'Horsepower', 'Miles_per_Gallon']
            ).interactive()
    
            from neptunecontrib.api import log_chart
    
            log_chart('altair_chart', chart)
    
        Create Bokeh figure and log it to Neptune::
    
            from bokeh.plotting import figure
    
            p = figure(plot_width=400, plot_height=400)
    
            # add a circle renderer with a size, color, and alpha
            p.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="navy", alpha=0.5)
    
            from neptunecontrib.api import log_chart
    
            log_chart('bokeh_figure', p)
    
    Note:
        Check out how the logged charts look in Neptune:
        `example experiment
        <https://ui.neptune.ai/o/shared/org/showroom/e/SHOW-973/artifacts?path=charts%2F&file=bokeh_figure.html>`_

    
`log_explainer(filename, explainer, experiment=None)`
:   Logs dalex explainer to Neptune.
    
    Dalex explainer is pickled and logged to Neptune.
    
    Args:
        filename (:obj:`str`): filename that will be used as an artifact's destination.
        explainer (:obj:`dalex.Explainer`): an instance of dalex explainer
        experiment (:obj:`neptune.experiments.Experiment`, optional, default is ``None``):
            | For advanced users only. Pass Neptune
              `Experiment <https://docs.neptune.ai/neptune-client/docs/experiment.html#neptune.experiments.Experiment>`_
              object if you want to control to which experiment data is logged.
            | If ``None``, log to currently active, and most recent experiment.
    
    Examples:
        Start an experiment::
    
            import neptune
    
            neptune.init(api_token='ANONYMOUS',
                         project_qualified_name='shared/dalex-integration')
            neptune.create_experiment(name='logging explanations')
    
        Train your model and create dalex explainer::
    
            ...
            clf.fit(X, y)
    
            expl = dx.Explainer(clf, X, y, label="Titanic MLP Pipeline")
    
            log_explainer('explainer.pkl', expl)
    
    Note:
        Check out how the logged explainer looks in Neptune:
        `example experiment <https://ui.neptune.ai/o/shared/org/dalex-integration/e/DAL-48/artifacts>`_

    
`log_global_explanations(explainer, categorical_features=None, numerical_features=None, experiment=None)`
:   Logs global explanations from dalex to Neptune.
    
    Dalex explanations are converted to interactive HTML objects and then uploaded to Neptune
    as an artifact with path charts/{name}.html.
    
    The following explanations are logged: variable importance. If categorical features are specified partial dependence
    and accumulated dependence are also logged. Explanation charts are created and logged with default settings.
    To log charts with custom settings, create a custom chart and use `neptunecontrib.api.log_chart`.
    For more information about Dalex go to `Dalex Website <https://modeloriented.github.io/DALEX/>`_.
    
    Args:
        explainer (:obj:`dalex.Explainer`): an instance of dalex explainer
        categorical_features (:list): list of categorical features for which you want to create
            accumulated dependence plots.
        numerical_features (:list): list of numerical features for which you want to create
            partial dependence plots.
        experiment (:obj:`neptune.experiments.Experiment`, optional, default is ``None``):
            | For advanced users only. Pass Neptune
              `Experiment <https://docs.neptune.ai/neptune-client/docs/experiment.html#neptune.experiments.Experiment>`_
              object if you want to control to which experiment data is logged.
            | If ``None``, log to currently active, and most recent experiment.
    
    Examples:
        Start an experiment::
    
            import neptune
    
            neptune.init(api_token='ANONYMOUS',
                         project_qualified_name='shared/dalex-integration')
            neptune.create_experiment(name='logging explanations')
    
        Train your model and create dalex explainer::
    
            ...
            clf.fit(X, y)
    
            expl = dx.Explainer(clf, X, y, label="Titanic MLP Pipeline")
            log_global_explanations(expl, categorical_features=["gender", "class"], numerical_features=["age", "fare"])
    
    Note:
        Check out how the logged explanations look in Neptune:
        `example experiment <https://ui.neptune.ai/o/shared/org/dalex-integration/e/DAL-48/artifacts?path=charts%2F>`_

    
`log_html(name, html, experiment=None)`
:   Logs html to neptune.
    
    HTML is logged to Neptune as an artifact with path html/{name}.html
    
    Args:
        name (:obj:`str`):
            | Name of the chart (without extension) that will be used as a part of artifact's destination.
        html_body (:obj:`str`):
            | HTML string that is logged and rendered as HTML.
        experiment (:obj:`neptune.experiments.Experiment`, optional, default is ``None``):
            | For advanced users only. Pass Neptune
              `Experiment <https://docs.neptune.ai/neptune-client/docs/experiment.html#neptune.experiments.Experiment>`_
              object if you want to control to which experiment data is logged.
            | If ``None``, log to currently active, and most recent experiment.
    
    Examples:
        Start an experiment::
    
            import neptune
    
            neptune.init(api_token='ANONYMOUS',
                         project_qualified_name='shared/showroom')
            neptune.create_experiment(name='experiment_with_html')
    
        Create an HTML string::
    
            html = "<button type='button',style='background-color:#005879; width:300px; height:200px; font-size:30px'>                  <a style='color: #ccc', href='https://docs.neptune.ai'> Take me back to the docs!!<a> </button>"
    
        Log it to Neptune::
    
             from neptunecontrib.api import log_html
    
             log_html('go_to_docs_button', html)
    
        Check out how the logged table looks in Neptune:
        https://ui.neptune.ai/o/shared/org/showroom/e/SHOW-988/artifacts?path=html%2F&file=button_example.html

    
`log_local_explanations(explainer, observation, experiment=None)`
:   Logs local explanations from dalex to Neptune.
    
    Dalex explanations are converted to interactive HTML objects and then uploaded to Neptune
    as an artifact with path charts/{name}.html.
    
    The following explanations are logged: break down, break down with interactions, shap, ceteris paribus,
    and ceteris paribus for categorical variables. Explanation charts are created and logged with default settings.
    To log charts with custom settings, create a custom chart and use `neptunecontrib.api.log_chart`.
    For more information about Dalex go to `Dalex Website <https://modeloriented.github.io/DALEX/>`_.
    
    Args:
        explainer (:obj:`dalex.Explainer`): an instance of dalex explainer
        observation (:obj): an observation that can be fed to the classifier for which the explainer was created
        experiment (:obj:`neptune.experiments.Experiment`, optional, default is ``None``):
            | For advanced users only. Pass Neptune
              `Experiment <https://docs.neptune.ai/neptune-client/docs/experiment.html#neptune.experiments.Experiment>`_
              object if you want to control to which experiment data is logged.
            | If ``None``, log to currently active, and most recent experiment.
    
    Examples:
        Start an experiment::
    
            import neptune
    
            neptune.init(api_token='ANONYMOUS',
                         project_qualified_name='shared/dalex-integration')
            neptune.create_experiment(name='logging explanations')
    
        Train your model and create dalex explainer::
    
            ...
            clf.fit(X, y)
    
            expl = dx.Explainer(clf, X, y, label="Titanic MLP Pipeline")
    
            new_observation = pd.DataFrame({'gender': ['male'],
                                            'age': [25],
                                            'class': ['1st'],
                                            'embarked': ['Southampton'],
                                            'fare': [72],
                                            'sibsp': [0],
                                            'parch': 0},
                                           index=['John'])
    
            log_local_explanations(expl, new_observation)
    
    Note:
        Check out how the logged explanations look in Neptune:
        `example experiment <https://ui.neptune.ai/o/shared/org/dalex-integration/e/DAL-48/artifacts?path=charts%2F>`_

    
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

    
`log_table(name, table, experiment=None)`
:   Logs pandas dataframe to neptune.
    
    Pandas dataframe is converted to an HTML table and logged to Neptune as an artifact with path tables/{name}.html
    
    Args:
        name (:obj:`str`):
            | Name of the chart (without extension) that will be used as a part of artifact's destination.
        table (:obj:`pandas.Dataframe`):
            | DataFrame table
        experiment (:obj:`neptune.experiments.Experiment`, optional, default is ``None``):
            | For advanced users only. Pass Neptune
              `Experiment <https://docs.neptune.ai/neptune-client/docs/experiment.html#neptune.experiments.Experiment>`_
              object if you want to control to which experiment data is logged.
            | If ``None``, log to currently active, and most recent experiment.
    
    Examples:
        Start an experiment::
    
            import neptune
    
            neptune.init(api_token='ANONYMOUS',
                         project_qualified_name='shared/showroom')
            neptune.create_experiment(name='experiment_with_tables')
    
        Create or load dataframe::
    
            import pandas as pd
    
            iris_df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv', nrows=100)
    
        Log it to Neptune::
    
             from neptunecontrib.api import log_table
    
             log_table('pandas_df', iris_df)
    
        Check out how the logged table looks in Neptune:
        https://ui.neptune.ai/o/shared/org/showroom/e/SHOW-977/artifacts?path=tables%2F&file=pandas_df.html

    
`log_video(path_to_file, video_name=None, experiment=None)`
:   Logs a video file to 'artifacts/video' with player.
    
    Logs a video file to the 'artifacts/video' in the experiment, where you can play it directly from the browser.
    
    You can also download raw video file to the local machine.
    Just use "three vertical dots" located to the right from the player.
    
    Args:
        path_to_file (:obj:`str`): Path to video file.
        video_name (:obj:`str`, optional, default is ``None``): Name to be displayed in artifacts/video.
            | If `None`, file name is used.
        experiment (:obj:`neptune.experiments.Experiment`, optional, default is ``None``):
            | For advanced users only. Pass Neptune
              `Experiment <https://docs.neptune.ai/neptune-client/docs/experiment.html#neptune.experiments.Experiment>`_
              object if you want to control to which experiment data is logged.
            | If ``None``, log to currently active, and most recent experiment.
    
    Example:
    
        .. code:: python3
    
            log_video('video-file.mp4')
            log_video('/full/path/to/some/other/video/file.mp4')
            log_video('/full/path/to/some/other/video/file.mp4', 'my_video')
    
    Note:
        Check out how the logged video file looks in Neptune:
        `here <https://ui.neptune.ai/o/shared/org/showroom/e/
        SHOW-1542/artifacts?path=video%2F&file=jellyfish-25-mbps-hd-hevc.html>`_.
    
    Warning:
        Video files contribute to the storage usage. Be mindful with large video files.

    
`pickle_and_log_artifact(obj, filename, experiment=None)`
:   

    
`strip_prefices(columns, prefices)`
:   Filters leaderboard columns to get the system column names.
    
    Args:
        columns(iterable): Iterable of leaderboard column names.
        prefices(list): List of prefices to strip. You can choose one of
            ['channel_', 'parameter_', 'property_']
    
    Returns:
        list: A list of clean column names.