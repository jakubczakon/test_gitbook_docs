Module neptunecontrib.hpo
=========================

Sub-modules
-----------
* neptunecontrib.hpo.utils

Functions
---------

    
`bayes2skopt(bayes_opt)`
:   Converts BayesOptimization instance to scipy OptimizeResult.
    
    Helper function that converts the BayesOptimization instance into scipy OptimizeResult
    format.
    
    Args:
        bayes_opt(`bayes_opt.Bayesian_optimization.BayesianOptimization`): BayesianOptimization instance.
    
    Returns:
        `scipy.optimize.optimize.OptimizeResult`: Converted OptimizeResult.
    
    Examples:
        Run BayesOptimize maximization::
    
            ...
            bayes_optimization = BayesianOptimization(objective, space)
            bayes_optimization.maximize(init_points=10, n_iter=100, xi=0.06)
    
        Convert bayes.space.res() object to the OptimizeResult object::
    
            import neptunecontrib.hpo.utils as hp_utils
            results = hp_utils.bayes2skopt(bayes_optimization)
    
    Note:
        Since skopt is always minimizing and BayesianOptimization is maximizing, the objective function values are
        converted into negatives for consistency.

    
`df2result(df, metric_col, param_cols, param_types=None)`
:   Converts dataframe with metrics and hyperparameters to the OptimizeResults format.
    
    It is a helper function that lets you use all the tools that expect OptimizeResult object
    like for example scikit-optimize plot_evaluations function.
    
    Args:
        df(`pandas.DataFrame`): Dataframe containing metric and hyperparameters.
        metric_col(str): Name of the metric column.
        param_cols(list): Names of the hyperparameter columns.
        param_types(list or None): Optional list of hyperparameter column types.
            By default it will treat all the columns as float but you can also pass str
            for categorical channels. E.g param_types=[float, str, float, float]
    
    Returns:
        `scipy.optimize.OptimizeResult`: Results object that contains the hyperparameter and metric
        information.
    
    Examples:
        Instantiate a session::
    
            from neptune.sessions import Session
            session = Session()
    
        Fetch a project and a list of experiments::
    
            project = session.get_projects('neptune-ai')['neptune-ai/Home-Credit-Default-Risk']
            leaderboard = project.get_leaderboard(state=['succeeded'], owner=['czakon'])
    
        Comvert the leaderboard dataframe to the `ResultOptimize` instance taking only the parameters and
        metric that you care about::
    
            result = df2result(leaderboard,
                metric_col='channel_ROC_AUC',
                param_cols=['parameter_lgbm__max_depth',
                            'parameter_lgbm__num_leaves',
                            'parameter_lgbm__min_child_samples'])

    
`hpbandster2skopt(results)`
:   Converts hpbandster results to scipy OptimizeResult.
    
    Helper function that converts the hpbandster Result instance into scipy OptimizeResult
    format.
    
    Args:
        results(hpbandster.core.Result): Result instance containing parameters and loss values.
    
    Returns:
        `scipy.optimize.optimize.OptimizeResult`: Converted OptimizeResult.
    
    Examples:
        Run your hpbandster study::
    
            optim = BOHB(configspace = worker.get_configspace())
            results = optim.run(n_iterations=100)
    
        Convert hpbandster Result object into the OptimizeResult object::
    
            import neptunecontrib.hpo.utils as hp_utils
            results = hp_utils.hpbandster2skopt(results)

    
`hyperopt2skopt(trials, space)`
:   Converts hyperopt trials to scipy OptimizeResult.
    
    Helper function that converts the hyperopt Trials instance into scipy OptimizeResult
    format.
    
    Args:
        trials(`hyperopt.base.Trials`): hyperopt trials object which stores training
            information from the fmin() optimization function.
        space(`collections.OrderedDict`): Hyper parameter space over which
            hyperopt will search. It is important to have this as OrderedDict rather
            than a simple dictionary because otherwise the parameter names will be
            shuffled.
    
    Returns:
        `scipy.optimize.optimize.OptimizeResult`: Converted OptimizeResult.
    
    
    Examples:
        Prepare the space of hyperparameters to search over::
    
            from hyperopt import hp, tpe, fmin, Trials
            space = OrderedDict(num_leaves=hp.choice('num_leaves', range(10, 60, 1)),
                        max_depth=hp.choice('max_depth', range(2, 30, 1)),
                        feature_fraction=hp.uniform('feature_fraction', 0.1, 0.9)
                               )
    
        Create an objective and run your hyperopt training::
    
            trials = Trials()
            _ = fmin(objective, space, trials=trials, algo=tpe.suggest, max_evals=100)
    
        Convert trials object to the OptimizeResult object::
    
            import neptunecontrib.hpo.utils as hp_utils
            results = hp_utils.hyperopt2skopt(trials, space)

    
`optuna2skopt(study)`
:   Converts optuna study to scipy OptimizeResult.
    
    Helper function that converts the optuna Study instance into scipy OptimizeResult
    format.
    
    Args:
        study(`optuna.study.Study`): Study isntance containing scores and hyperparameters.
    
    Returns:
        `scipy.optimize.optimize.OptimizeResult`: Converted OptimizeResult.
    
    Examples:
        Run your optuna study::
    
            study = optuna.create_study()
            study.optimize(objective, n_trials=100)
    
        Convert trials_dataframe object to the OptimizeResult object::
    
            import neptunecontrib.hpo.utils as hp_utils
            results = hp_utils.optuna2skopt(study)