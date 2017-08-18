from unittest import TestCase

from apps.appsmanager import AppsManager
from apps.blender.blenderenvironment import BlenderEnvironment
from apps.core.benchmark.benchmark import Benchmark
from apps.lux.luxenvironment import LuxRenderEnvironment


class TestAppsManager(TestCase):

    @staticmethod
    def _init_app_manager():
        """
        Start App manager and load apps list
        :return AppManager:
        """
        app_manager = AppsManager()
        app_manager.load_apps()
        return app_manager

    def test_get_env_list(self):
        """
        Checks if default environments are in the apps list
        """
        app_manager = self._init_app_manager()
        apps = app_manager.get_env_list()
        assert any(isinstance(app, BlenderEnvironment) for app in apps)
        assert any(isinstance(app, LuxRenderEnvironment) for app in apps)

    def test_benchmark_is_in_apps(self):
        """
        Check if there is benchmark in the apps list
        :return:
        """
        app_manager = self._init_app_manager()
        assert isinstance(app_manager.apps['Blender'].benchmark(), Benchmark)
        assert isinstance(app_manager.apps['LuxRender'].benchmark(), Benchmark)
