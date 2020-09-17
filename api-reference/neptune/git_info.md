Module neptune.git_info
=======================

Classes
-------

`GitInfo(commit_id, message='', author_name='', author_email='', commit_date='', repository_dirty=True, active_branch='', remote_urls=None)`
:   Class that keeps information about a git repository in experiment.
    
    When :meth:`~neptune.projects.Project.create_experiment` is invoked, instance of this class is created to
    store information about git repository.
    This information is later presented in the experiment details tab in the Neptune web application.
    
    Args:
        commit_id (:obj:`str`): commit id sha.
        message (:obj:`str`, optional, default is ``""``): commit message.
        author_name (:obj:`str`, optional, default is ``""``): commit author username.
        author_email (:obj:`str`, optional, default is ``""``): commit author email.
        commit_date (:obj:`datetime.datetime`, optional, default is ``""``): commit datetime.
        repository_dirty (:obj:`bool`, optional, default is ``True``):
            ``True``, if the repository has uncommitted changes, ``False`` otherwise.