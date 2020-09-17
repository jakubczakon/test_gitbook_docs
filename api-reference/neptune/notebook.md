Module neptune.notebook
=======================

Classes
-------

`Notebook(backend, project, _id, owner)`
:   It contains all the information about a Neptune Notebook
    
    Args:
        backend (:class:`~neptune.Backend`): A Backend object
        project (:class:`~neptune.projects.Project`): Project object
        _id (:obj:`str`): Notebook uuid
        owner (:obj:`str`): Creator of the notebook is the Notebook owner
    
    Examples:
        .. code:: python3
    
            # Create a notebook in Neptune.
            notebook = project.create_notebook('data_exploration.ipynb')

    ### Instance variables

    `id`
    :

    `owner`
    :

    ### Methods

    `add_checkpoint(self, file_path)`
    :   Uploads new checkpoint of the notebook to Neptune
        
        Args:
            file_path (:obj:`str`): File path containing notebook contents
        
        Example:
        
            .. code:: python3
        
                # Create a notebook.
                notebook = project.create_notebook('file.ipynb')
        
                # Change content in your notebook & save it
        
                # Upload new checkpoint
                notebook.add_checkpoint('file.ipynb')

    `get_name(self)`
    :   Returns the name used to upload the current checkpoint of this notebook
        
        Returns:
            :obj:`str`: the name of current checkpoint

    `get_path(self)`
    :   Returns the path used to upload the current checkpoint of this notebook
        
        Returns:
            :obj:`str`: path of the current checkpoint