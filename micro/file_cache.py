import abc

from . import loading

class BaseFileLoader(abc.ABC):
    @abc.abstractmethod
    def make_file_id(self, base_path, local_base_path, filename):
        pass

    @abc.abstractmethod
    def load_file(
        self,
        base_path,
        local_base_path,
        filename,
        file_id,
        functions={},
    ):
        pass

class FileCache:
    def __init__(self, file_loader=None):
        self._file_loader = file_loader \
            if file_loader is not None \
            else loading.FileLoader()
        self._file_cache = {}

    def get_file(self, base_path, local_base_path, filename, functions={}):
        file_id = self._file_loader.make_file_id(
            base_path,
            local_base_path,
            filename,
        )
        if file_id not in self._file_cache:
            result = self._file_loader.load_file(
                base_path,
                local_base_path,
                filename,
                file_id,
                functions,
            )
            self._file_cache[file_id] = result
        else:
            result = self._file_cache[file_id]

        return result
