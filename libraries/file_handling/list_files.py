import os


class CollectFiles:
    def __init__(self, path):
        self.path = path
        self.files_list = []

    def make_list_of_files(self):
        # TODO: relative path to project root
        # TODO: Cross-platform enabled
        # https://www.linkedin.com/advice/3/how-do-you-manage-path-differences-python-nwxnf
        for (root, subdirs, files) in os.walk(self.path):
            for filename in files:
                self.files_list.append(os.path.join(root, filename))
        return self.files_list