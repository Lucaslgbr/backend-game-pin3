from rest_framework.routers import DefaultRouter

import importlib
class APIRouter(DefaultRouter):
    CURRENT_VERSION =1

    def __init__(self):
        super(APIRouter, self).__init__()
        self.register_viewsets()

    def register_viewsets(self):
        for version in range(1,self.CURRENT_VERSION+1):
            router = importlib.import_module(f'backend.game.api.v{version}.router')
            for route in router.viewsets:
                self.register(f"v{version}/{route['path']}", route['viewset'])
    

    def register_api_views(self):
        raise NotImplementedError


