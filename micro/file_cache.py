import abc

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
