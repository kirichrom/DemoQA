import os

from framework.utils.path_provider import PathProvider

framework_config_path = os.path.join(PathProvider.get_root_dir(), 'framework/resources/config.json')
test_config_path = os.path.join(PathProvider.get_root_dir(), 'project/resources/test_config.json')
