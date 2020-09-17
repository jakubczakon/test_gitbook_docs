Module neptunecontrib.viz.projects
==================================

Functions
---------

    
`project_progress(progress_df, width=800, heights=(50, 400), line_size=5, text_size=15, opacity=0.3)`
:   Creates an interactive project progress exploration chart.
    
    It lets you choose the resources you want to see ('experiment_count_day' or 'running_time_day'), you
    can see the metric/id/tags for every experiment on mouseover, you can select the x range which you want to
    investigate by selecting it on the top chart and you get shown the actual values on mousehover.
    
    The chart is build on top of the Altair which in turn is build on top of Vega-Lite and Vega.
    That means you can use the objects produces by this script (converting it first to json by .to_json() method)
    in your html webpage without any problem.
    
    Args:
        progress_df('pandas.DataFrame'): Dataframe containing ['id', 'metric', 'metric_best', 'running_time',
            'running_time_day', 'experiment_count_day', 'owner', 'tags', 'timestamp', 'timestamp_day'].
            It can be obtained from a list of experiments by using the
            `neptunecontrib.api.extract_project_progress_info` function.
            If the len of the dataframe exceeds 5000 it will cause the MaxRowsError.
            Read the Note to learn why and how to disable it.
        width(int): width of the chart. Default is 800.
        heights(tuple): heights of the subcharts. The first value controls the top chart, the second
            controls the bottom chart. Default is (50,400).
        line_size(int): size of the lines. Default is 5.
        text_size(int): size of the text containing metric/id/tags in the middle.
        opacity(float): opacity of the resource bars in the background. Default is 0.3.
    
    Returns:
        `altair.Chart`: Altair chart object which will be automatically rendered in the notebook. You can
        also run the `.to_json()` method on it to convert it to the Vega-Lite json format.
    
    Examples:
        Instantiate a session::
    
            from neptunelib.api.session import Session
            session = Session()
    
        Fetch a project and the experiment view of that project::
    
            project = session.get_projects('neptune-ai')['neptune-ai/Salt-Detection']
            leaderboard = project.get_leaderboard()
    
        Create a progress info dataframe::
    
            from neptunecontrib.api.utils import extract_project_progress_info
            progress_df = extract_project_progress_info(leadearboard,
                                                        metric_colname='channel_IOUT',
                                                        time_colname='finished')
    
        Plot interactive chart in notebook::
    
            from neptunecontrib.viz.projects import project_progress
            project_progress(progress_df)
    
    Note:
        Because Vega-Lite visualizations keep all the chart data in the HTML the visualizations can consume huge
        amounts of memory if not handled properly. That is why, by default the hard limit of 5000 rows is set to
        the len of dataframe. That being said, you can disable it by adding the following line in the notebook or code::
    
            import altair as alt
            alt.data_transformers.enable('default', max_rows=None)