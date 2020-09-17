Module neptunecontrib.viz.parallel_coordinates_plot
===================================================

Functions
---------

    
`make_parallel_coordinates_plot(html_file_path=None, metrics=False, text_logs=False, params=True, properties=False, experiment_id=None, state=None, owner=None, tag=None, min_running_time=None)`
:   Visualize experiments on the parallel coordinates plot.
    
    This function, when executed in Notebook, displays interactive parallel coordinates plot in the cell's output.
    Another option is to save visualization to the standalone html file.
    You can also inspect the lineage of experiments.
    
    **See** `example <https://neptune-contrib.readthedocs.io/examples/hiplot_visualizations.html>`_
    **for the full use case.**
    
    Axes are ordered as follows: first axis is neptune ``experiment id``,
    second is experiment ``owner``,
    then ``params`` and ``properties`` in alphabetical order.
    Finally, ``metrics`` on the right side (alphabetical order as well).
    
    This visualization it built using `HiPlot <https://facebookresearch.github.io/hiplot/index.html>`_.
    It is a library published by the Facebook AI group.
    Learn more about the `parallel coordinates plot <https://en.wikipedia.org/wiki/Parallel_coordinates>`_.
    
    Tip:
        Use ``metrics``, ``params`` and ``properties`` arguments to select what data you want to see as axes.
    
        Use ``experiment_id``, ``state``, ``owner``, ``tag``, ``min_running_time`` arguments to filter experiments
        included in a plot. Only experiments matching all the criteria will be returned.
    
    Note:
        Make sure you have your project set: ``neptune.init('USERNAME/example-project')``
    
    Args:
        html_file_path (:obj:`str`, optional, default is ``None``):
            | Saves visualization as a standalone html file. No external dependencies needed.
        metrics (:obj:`bool` or :obj:`str` or :obj:`list` of :obj:`str`, optional, default is ``False``):
            | Metrics to display on the plot (as axes).
            | If `True`, then display all metrics.
            | If `False`, then exclude all metrics.
        text_logs (:obj:`bool` or :obj:`str` or :obj:`list` of :obj:`str`, optional, default is ``False``):
            | Text logs to display on the plot (as axes).
            | If `True`, then display all text logs.
            | If `False`, then exclude all text logs.
        params (:obj:`bool` or :obj:`str` or :obj:`list` of :obj:`str`, optional, default is ``True``):
            | Parameters to display on the plot (as axes).
            | If `True`, then display all parameters.
            | If `False`, then exclude all parameters.
        properties (:obj:`bool` or :obj:`str` or :obj:`list` of :obj:`str`, optional, default is ``False``):
            | Properties to display on the plot (as axes).
            | If `True`, then display all properties.
            | If `False`, then exclude all properties.
        experiment_id (:obj:`str` or :obj:`list` of :obj:`str`, optional, default is ``None``):
            | An experiment id like ``'SAN-1'`` or list of ids like ``['SAN-1', 'SAN-2']``.
            | Matching any element of the list is sufficient to pass criterion.
        state (:obj:`str` or :obj:`list` of :obj:`str`, optional, default is ``None``):
            | An experiment state like ``'succeeded'`` or list of states like ``['succeeded', 'running']``.
            | Possible values: ``'running'``, ``'succeeded'``, ``'failed'``, ``'aborted'``.
            | Matching any element of the list is sufficient to pass criterion.
        owner (:obj:`str` or :obj:`list` of :obj:`str`, optional, default is ``None``):
            | *Username* of the experiment owner (User who created experiment is an owner) like ``'josh'``
              or list of owners like ``['frederic', 'josh']``.
            | Matching any element of the list is sufficient to pass criterion.
        tag (:obj:`str` or :obj:`list` of :obj:`str`, optional, default is ``None``):
            | An experiment tag like ``'lightGBM'`` or list of tags like ``['pytorch', 'cycleLR']``.
            | Only experiments that have all specified tags will match this criterion.
        min_running_time (:obj:`int`, optional, default is ``None``):
            Minimum running time of an experiment in seconds, like ``2000``.
    
    Returns:
    
        :obj:`ExperimentDisplayed`, object that can be used to get a ``list`` of ``Datapoint`` objects,
        like this: ``ExperimentDisplayed.get_selected()``. This is only implemented for Jupyter notebook. Check
        `HiPlot docs
        <https://facebookresearch.github.io/hiplot/py_reference.html?highlight=display#hiplot.Experiment.display>`_.
    
    Examples:
    
        .. code:: python3
    
            # Make sure you have your project set:
            neptune.init('USERNAME/example-project')
    
            # (example 1) visualization for all experiments in project
            make_parallel_coordinates_plot()
    
            # (example 2) visualization for experiment with tag 'optuna' and saving to html file.
            make_parallel_coordinates_plot(html_file_path='visualizations.html', tag='optuna')
    
            # (example 3) visualization with all params, two metrics for experiment with tag 'optuna'
            make_parallel_coordinates_plot(tag='optuna', metrics=['epoch_accuracy', 'eval_accuracy'])
    
            # (example 4) visualization with all params and two metrics. All experiments created by john.
            make_parallel_coordinates_plot(metrics=['epoch_accuracy', 'eval_accuracy'], owner='john')