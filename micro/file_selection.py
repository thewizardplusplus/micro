import os
import sys
import inspect

_LIBRARY_VARIABLE = 'MICRO_LIBRARY'
_SCRIPT_EXTENSION = '.micro'

def try_select_path(base_path, local_base_path, filename, file_selector=None):
    full_path = _select_path(
        base_path,
        local_base_path,
        filename,
        file_selector,
    )
    if full_path is None:
        raise Exception('unable to load {}'.format(filename))

    return full_path

def _select_path(base_path, local_base_path, filename, file_selector=None):
    file_selector = file_selector if file_selector is not None else _select_file
    if local_base_path is not None:
        full_path = file_selector(os.path.join(local_base_path, filename))
        if full_path is not None:
            return full_path

    if base_path is not None:
        full_path = file_selector(os.path.join(base_path, 'vendor', filename))
        if full_path is not None:
            return full_path

    library_paths = os.getenv(_LIBRARY_VARIABLE)
    if library_paths is not None:
        for library_path in reversed(library_paths.split(':')):
            full_path = file_selector(os.path.join(library_path, filename))
            if full_path is not None:
                return full_path

    return file_selector(os.path.join(
        os.path.dirname(inspect.getfile(sys.modules[__name__])),
        'data',
        filename,
    ))

def _select_file(path):
    if os.path.splitext(path)[1] == _SCRIPT_EXTENSION and os.path.isfile(path):
        return path

    full_path = path + _SCRIPT_EXTENSION
    if os.path.isfile(full_path):
        return full_path

    full_path = os.path.join(path, '__main__' + _SCRIPT_EXTENSION)
    if os.path.isfile(full_path):
        return full_path

    return None
