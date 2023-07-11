import os


class PathProvider:
    BASE_NAME = 'DemoQA'  # Project root folder name
    TEST_PATH_NAME = 'tests'  # Test folder name

    @staticmethod
    def get_root_dir() -> str:
        """
        Method that returns the path to the root folder of the project, regardless of where the tests are called from.
        :return: str, root path
        """
        work_path = os.getcwd()
        root_dir = None
        base_name = os.path.basename(work_path)
        if base_name == PathProvider.BASE_NAME:
            root_dir = work_path
        elif base_name == PathProvider.TEST_PATH_NAME:
            while os.path.basename(work_path) != PathProvider.BASE_NAME:
                work_path = os.path.dirname(work_path)
            root_dir = work_path
        return root_dir

