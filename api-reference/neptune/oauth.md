Module neptune.oauth
====================

Classes
-------

`NeptuneAuth(session)`
:   Base class that all auth implementations derive from

    ### Ancestors (in MRO)

    * requests.auth.AuthBase

    ### Methods

    `refresh_token_if_needed(*args, **kwargs)`
    :

`NeptuneAuthenticator(auth_tokens, ssl_verify, proxies)`
:   Authenticates requests.
    
    :param host: Host to authenticate for.

    ### Ancestors (in MRO)

    * bravado.requests_client.Authenticator

    ### Methods

    `apply(self, request)`
    :   Apply authentication to a request.
        
        :param request: Request to add authentication information to.

    `matches(self, url)`
    :   Returns true if this authenticator applies to the given url.
        
        :param url: URL to check.
        :return: True if matches host and port, False otherwise.