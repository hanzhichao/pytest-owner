import pytest


def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "owner: Mark tests with owner and run tests by use --owner"
    )


def pytest_addoption(parser):
    parser.addoption('--owner', action='append', help='Run tests which mark the same owners')


@pytest.fixture
def owner(config):
    """获取当前指定的owner"""
    return config.getoption('--owner')


def pytest_collection_modifyitems(session, config, items):
    selected_owners = config.getoption('--owner')
    # print(selected_owners)
    if selected_owners == None:
        return
    
    deselected_items = set()
    for item in items:
        marker_owner = None
        for marker in item.iter_markers('owner'):
            [marker_owner] = marker.args
        if marker_owner not in selected_owners:
            deselected_items.add(item)

    selected_items = [item for item in items if item not in deselected_items]
    items[:] = selected_items
    config.hook.pytest_deselected(items=list(deselected_items))


