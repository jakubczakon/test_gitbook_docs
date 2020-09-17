Module neptunecontrib.versioning
================================

Sub-modules
-----------
* neptunecontrib.versioning.data

Functions
---------

    
`log_data_version(path, prefix='', experiment=None)`
:   Logs data version of file or folder to Neptune
    
    For a path it calculates the hash and logs it along with the path itself as a property to Neptune experiment.
    Path to dataset can be a file or directory.
    
    Args:
        path(str): path to the file or directory,
        prefix(str): Prefix that will be added before 'data_version' and 'data_path'
        experiment(neptune.experiemnts.Experiment or None): if the data should be logged to a particular
           neptune experiment it can be passed here. By default it is logged to the current experiment.
    
    Examples:
        Initialize Neptune::
    
            import neptune
            from neptunecontrib.versioning.data import log_data_version
            neptune.init('USER_NAME/PROJECT_NAME')
    
        Log data version from filepath::
    
            FILEPATH = '/path/to/data/my_data.csv'
            with neptune.create_experiment():
                log_data_version(FILEPATH)

    
`log_image_dir_snapshots(image_dir, channel_name='image_dir_snapshots', experiment=None, sample=16, seed=1234)`
:   Logs visual snapshot of the directory with image data to Neptune.
    
    For a given directory with images it logs a sample of images as figure to Neptune.
    If the `image_dir` specified contains multiple folders it will sample per folder and create
    multiple figures naming each figure with the folder name.
    See snapshots per class here https://ui.neptune.ai/jakub-czakon/examples/e/EX-95/channels.
    
    Args:
        image_dir(str): path to directory with images.
        sample(int): number of images that should be sampled for plotting.
        channel_name(str): name of the neptune channel. Default is 'image_dir_snapshots'.
        experiment(neptune.experiemnts.Experiment or None): if the data should be logged to a particular
           neptune experiment it can be passed here. By default it is logged to the current experiment.
        seed(int): random state for the sampling of images.
    
    Examples:
        Initialize Neptune::
    
            import neptune
            from neptunecontrib.versioning.data import log_image_dir_snapshots
            neptune.init('USER_NAME/PROJECT_NAME')
    
        Log visual snapshot of image directory::
    
            PATH = 'train_dir/'
            with neptune.create_experiment():
                log_image_dir_snapshots(PATH)

    
`log_s3_data_version(bucket_name, path, prefix='', experiment=None)`
:   Logs data version of s3 bucket to Neptune
    
    For a bucket and path it calculates the hash and logs it along with the path itself as a property to
    Neptune experiment.
    Path is either the s3 bucket key to a file or the begining of a key (in case you use a "folder" structure).
    
    Args:
        bucket_name(str): name of the s3 bucket
        path(str): path to the file or directory on s3 bucket
        prefix(str): Prefix that will be added before 'data_version' and 'data_path'
        experiment(neptune.experiemnts.Experiment or None): if the data should be logged to a particular
           neptune experiment it can be passed here. By default it is logged to the current experiment.
    
    Examples:
        Initialize Neptune::
    
            import neptune
            from neptunecontrib.versioning.data import log_s3_data_version
            neptune.init('USER_NAME/PROJECT_NAME')
    
        Log data version from bucket::
    
            BUCKET = 'my-bucket'
            PATH = 'train_dir/'
            with neptune.create_experiment():
                log_s3_data_version(BUCKET, PATH)