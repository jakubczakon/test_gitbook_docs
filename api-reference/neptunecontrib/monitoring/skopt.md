Module neptunecontrib.monitoring.skopt
======================================

Functions
---------

    
`NeptuneMonitor(*args, **kwargs)`
:   

    
`log_results(results, experiment=None, log_plots=True, log_pickle=True)`
:   Logs runs results and parameters to neptune.
    
    Logs all hyperparameter optimization results to Neptune. Those include best score ('best_score' metric),
    best parameters ('best_parameters' property), convergence plot ('diagnostics' log),
    evaluations plot ('diagnostics' log), and objective plot ('diagnostics' log).
    
     Args:
         results('scipy.optimize.OptimizeResult'): Results object that is typically an
             output of the function like `skopt.forest_minimize(...)`
         experiment(`neptune.experiments.Experiment`): Neptune experiment. Default is None.
        log_plots: ('bool'): If True skopt plots will be logged to Neptune.
        log_pickle: ('bool'): if True pickled skopt results object will be logged to Neptune.
    
     Examples:
         Run skopt training::
    
             ...
             results = skopt.forest_minimize(objective, space,
                                 base_estimator='ET', n_calls=100, n_random_starts=10)
    
         Initialize Neptune::
    
            import neptune
    
            neptune.init(api_token='ANONYMOUS',
                         project_qualified_name='shared/showroom')
            neptune.create_experiment(name='optuna sweep')
    
         Send best parameters to Neptune::
    
             import neptunecontrib.monitoring.skopt as sk_utils
    
             sk_utils.log_results(results)
    
        You can explore an example experiment in Neptune:
        https://ui.neptune.ai/o/shared/org/showroom/e/SHOW-1065/logs

Classes
-------

`NeptuneCallback(experiment=None, log_checkpoint=True)`
:   Logs hyperparameter optimization process to Neptune.
    
    Specifically using NeptuneCallback will log: run metrics and run parameters, best run metrics so far, and
    the current results checkpoint.
    
    Examples:
        Initialize NeptuneCallback::
    
            import neptune
            import neptunecontrib.monitoring.skopt as sk_utils
    
            neptune.init(api_token='ANONYMOUS',
                         project_qualified_name='shared/showroom')
    
            neptune.create_experiment(name='optuna sweep')
    
            neptune_callback = sk_utils.NeptuneCallback()
    
        Run skopt training passing neptune_callback as a callback::
    
            ...
            results = skopt.forest_minimize(objective, space, callback=[neptune_callback],
                                base_estimator='ET', n_calls=100, n_random_starts=10)
    
        You can explore an example experiment in Neptune:
        https://ui.neptune.ai/o/shared/org/showroom/e/SHOW-1065/logs