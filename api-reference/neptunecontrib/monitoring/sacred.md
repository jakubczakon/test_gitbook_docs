Module neptunecontrib.monitoring.sacred
=======================================

Classes
-------

`NeptuneObserver(project_name, api_token=None, source_extensions=None)`
:   Logs sacred experiment data to Neptune.
    
    Sacred observer that logs experiment metadata to neptune.
    The experiment data can be accessed and shared via web UI or experiment API.
    Check Neptune docs for more information https://docs.neptune.ai.
    
    Args:
        project_name(str): project name in Neptune app
        api_token(str): Neptune API token. If it is kept in the NEPTUNE_API_TOKEN environment
           variable leave None here.
        source_extensions(list(str)): list of extensions that Neptune should treat as source files
           extensions and send. If None is passed, Python file from which experiment was created will be uploaded.
           Pass empty list ([]) to upload no files. Unix style pathname pattern expansion is supported.
           For example, you can pass '*.py' to upload all python source files from the current directory.
           For recursion lookup use '**/*.py' (for Python 3.5 and later). For more information see glob library.
    
    Examples:
        Create sacred experiment::
    
            from numpy.random import permutation
            from sklearn import svm, datasets
            from sacred import Experiment
    
            ex = Experiment('iris_rbf_svm')
    
        Add Neptune observer::
    
            from neptunecontrib.monitoring.sacred import NeptuneObserver
            ex.observers.append(NeptuneObserver(api_token='YOUR_LONG_API_TOKEN',
                                                project_name='USER_NAME/PROJECT_NAME'))
    
        Run experiment::
    
            @ex.config
            def cfg():
                C = 1.0
                gamma = 0.7
    
            @ex.automain
            def run(C, gamma, _run):
                iris = datasets.load_iris()
                per = permutation(iris.target.size)
                iris.data = iris.data[per]
                iris.target = iris.target[per]
                clf = svm.SVC(C, 'rbf', gamma=gamma)
                clf.fit(iris.data[:90],
                        iris.target[:90])
                return clf.score(iris.data[90:],
                                 iris.target[90:])
    
        Go to the app and see the experiment. For example, https://ui.neptune.ai/jakub-czakon/examples/e/EX-341

    ### Ancestors (in MRO)

    * sacred.observers.base.RunObserver

    ### Methods

    `artifact_event(self, name, filename, metadata=None, content_type=None)`
    :

    `completed_event(self, stop_time, result)`
    :

    `failed_event(self, fail_time, fail_trace)`
    :

    `interrupted_event(self, interrupt_time, status)`
    :

    `log_metrics(self, metrics_by_name, info)`
    :

    `resource_event(self, filename)`
    :

    `started_event(self, ex_info, command, host_info, start_time, config, meta_info, _id)`
    :