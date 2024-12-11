def get_server_url(request) -> str:
    """ Não tem última barra

    Args:
        request (_type_): _description_

    Returns:
        str: _description_
    """
    server_url = request.build_absolute_uri('/')
    
    # Remove a última barra se ela existir
    if server_url.endswith('/'):
        server_url = server_url[:-1]
    
    return server_url

def get_server_url_and_current_url(request):

    server_url = request.build_absolute_uri('/')
    path = request.path.lstrip('/')
    current_url = server_url + path 
    

    return server_url, current_url

def api_endpoint(request, path):
    return f"{get_server_url(request)}{path}"