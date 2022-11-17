"""{{ cookiecutter.project_name }} Routes Configuration

The `route_patterns` list routes URLs to views.

Examples:
    Function views:
        1. Add an import:  from my_app.views import home
        2. Add a URL to route_patterns:  Gateway('/', handler=home, name='home')
    Class-based views:
        1. Add an import:  from other_app.views import Home
        2. Add a URL to route_patterns:  Gateway('/', handler=Home, name='home')
    Including another configuration:
        1. Import the Include object: from esmerald import Include
        2. Add a URL to route_patterns:  Gateway('/api/v1/', Include(namespace='myapp.urls'))
"""
from esmerald import Include

route_patterns = [Include("/api/v1", namespace="accounts.v1.urls")]
