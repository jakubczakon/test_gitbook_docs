Module neptune.utils
====================

Functions
---------

    
`align_channels_on_x(dataframe)`
:   

    
`as_list(value)`
:   

    
`discover_git_repo_location()`
:   

    
`file_contains(filename, text)`
:   

    
`get_channel_name_stems(columns)`
:   

    
`get_git_info(repo_path=None)`
:   Retrieve information about git repository.
    
    If attempt fails, ``None`` will be returned.
    
    Args:
        repo_path (:obj:`str`, optional, default is ``None``):
    
            | Path to the repository from which extract information about git.
            | If ``None`` is passed, calling ``get_git_info`` is equivalent to calling
              ``git.Repo(search_parent_directories=True)``.
              Check `GitPython <https://gitpython.readthedocs.io/en/stable/reference.html#git.repo.base.Repo>`_
              docs for more information.
    
    Returns:
        :class:`~neptune.git_info.GitInfo` - An object representing information about git repository.
    
    Examples:
    
        .. code:: python3
    
            # Get git info from the current directory
            git_info = get_git_info('.')

    
`glob(pathname)`
:   

    
`in_docker()`
:   

    
`is_float(value)`
:   

    
`is_ipython()`
:   

    
`is_nan_or_inf(value)`
:   

    
`is_notebook()`
:   

    
`map_keys(f_key, dictionary)`
:   

    
`map_values(f_value, dictionary)`
:   

    
`merge_dataframes(dataframes, on, how='outer')`
:   

    
`update_session_proxies(session, proxies)`
:   

    
`validate_notebook_path(path)`
:   

    
`with_api_exceptions_handler(func)`
: