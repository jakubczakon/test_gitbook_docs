Module neptunecontrib.monitoring.optuna
=======================================

Functions
---------

    
`NeptuneMonitor(experiment=None)`
:   

    
`log_study(study, experiment=None, log_charts=True, params=None)`
:   

    
`log_study_info(study, experiment=None, log_charts=True, params=None)`
:   Logs runs results and parameters to neptune.
    
    Logs all hyperparameter optimization results to Neptune. Those include best score ('best_score' metric),
    best parameters ('best_parameters' property), the study object itself as artifact, and interactive optuna charts
    ('contour', 'parallel_coordinate', 'slice', 'optimization_history') as artifacts in 'charts' sub folder.
    
    Args:
        study('optuna.study.Study'): Optuna study object after training is completed.
        experiment(`neptune.experiments.Experiment`): Neptune experiment. Default is None.
        log_charts('bool'): Whether optuna visualization charts should be logged. By default all charts are logged.
        params(`list`): List of parameters to be visualized. Default is all parameters.
    
    Examples:
        Initialize neptune_monitor::
    
            import neptune
            import neptunecontrib.monitoring.optuna as opt_utils
    
            neptune.init(project_qualified_name='USER_NAME/PROJECT_NAME')
            neptune.create_experiment(name='optuna sweep')
    
            neptune_callback = opt_utils.NeptuneCallback()
    
        Run Optuna training passing monitor as callback::
    
            ...
            study = optuna.create_study(direction='maximize')
            study.optimize(objective, n_trials=100, callbacks=[neptune_callback])
            opt_utils.log_study_info(study)
    
        You can explore an example experiment in Neptune:
        https://ui.neptune.ai/o/shared/org/showroom/e/SHOW-1016/artifacts

Classes
-------

`NeptuneCallback(experiment=None, log_charts=False, log_study=False, params=None)`
:   Logs hyperparameter optimization process to Neptune.
    
    For each iteration it logs run metric and run parameters as well as the best score to date.
    
    Args:
        experiment(`neptune.experiments.Experiment`): Neptune experiment. Default is None.
        log_charts('bool'): Whether optuna visualization charts should be logged. By default no charts are logged.
        log_study('bool'): Whether optuna study object should be pickled and logged. By default it is not.
        params(`list`): List of parameters to be visualized. Default is all parameters.
    
    Examples:
        Initialize neptune_monitor::
    
            import neptune
            import neptunecontrib.monitoring.optuna as opt_utils
    
            neptune.init(api_token='ANONYMOUS',
                         project_qualified_name='shared/showroom')
            neptune.create_experiment(name='optuna sweep')
    
            neptune_callback = opt_utils.NeptuneCallback()
    
        Run Optuna training passing neptune_callback as callback::
    
            ...
            study = optuna.create_study(direction='maximize')
            study.optimize(objective, n_trials=100, callbacks=[neptune_callback])
    
        You can explore an example experiment in Neptune:
        https://ui.neptune.ai/o/shared/org/showroom/e/SHOW-1016/artifacts
    
        You can also log optuna visualization charts and study object after every iteration::
    
            neptune_callback = opt_utils.NeptuneCallback(log_charts=True, log_study=True)