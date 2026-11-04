from taskflow import __version__, sort_tasks


def test_package_exports_sort_tasks():
    assert callable(sort_tasks)


def test_package_version():
    assert __version__ == "0.1.0"
