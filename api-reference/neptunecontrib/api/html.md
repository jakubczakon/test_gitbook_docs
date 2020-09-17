Module neptunecontrib.api.html
==============================

Functions
---------

    
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