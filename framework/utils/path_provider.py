import os


class PathProvider:

    @staticmethod
    def get_root_dir() -> str:
        work_path = os.getcwd()
        root_dir = None
        if os.path.basename(work_path) == 'DemoQA':
            root_dir = work_path
        elif os.path.basename(work_path) == 'tests':
            root_dir = os.path.dirname(os.path.dirname(work_path))
        return root_dir
