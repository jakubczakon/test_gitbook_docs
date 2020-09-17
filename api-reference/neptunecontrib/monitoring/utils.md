Module neptunecontrib.monitoring.utils
======================================

Functions
---------

    
`axes2fig(axes, fig=None)`
:   Converts ndarray of matplotlib object to matplotlib figure.
    
    Scikit-optimize plotting functions return ndarray of axes. This can be tricky
    to work with so you can use this function to convert it to the standard figure format.
    
    Args:
        axes(`numpy.ndarray`): Array of matplotlib axes objects.
        fig('matplotlib.figure.Figure'): Matplotlib figure on which you may want to plot
            your axes. Default None.
    
    Returns:
        'matplotlib.figure.Figure': Matplotlib figure with axes objects as subplots.
    
    Examples:
        Assuming you have a `scipy.optimize.OptimizeResult` object you want to plot::
    
            from skopt.plots import plot_evaluations
            eval_plot = plot_evaluations(result, bins=20)
            >>> type(eval_plot)
                numpy.ndarray
    
            from neptunecontrib.viz.utils import axes2fig
            fig = axes2fig(eval_plot)
            >>> fig
                matplotlib.figure.Figure

    
`pickle_and_send_artifact(obj, filename, experiment=None)`
:   

    
`send_figure(fig, channel_name='figures', experiment=None)`
: