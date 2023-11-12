# -*- coding: utf-8 -*-
from datetime import datetime

import pytest


# TODO:
# [ ] datetime -> date switch

def pytest_addoption(parser):
    group = parser.getgroup('skipuntil')
    group.addoption(
        '--ignore-skip-until',
        action='store',
        dest='dest_foo',
        default='2023',
        help='Set the value for the fixture "bar".'
    )

    parser.addini('HELLO', 'Dummy pytest.ini setting')


@pytest.fixture
def bar(request):
    return request.config.option.dest_foo


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "skip_until(dt, strict, msg): mark test to run only on named environment"
    )


def pytest_collection_modifyitems(items):
    for testcase in items:       
        for marker in testcase.own_markers:            
            if marker.name == "skip_until":
                deadline = marker.kwargs.get("deadline")                
                
                if deadline is None:                    
                    raise Exception("deadline is not defined!")

                hard = marker.kwargs.get("strict") or False
                msg = marker.kwargs.get("msg") or ""
                print(f"dt {datetime.now()} {deadline=}")
                if datetime.now() > deadline:
                    print(f"dt {datetime.now()=} {deadline=}")
                    continue
                
                testcase.add_marker(pytest.mark.skip(reason=f"suppresed until {deadline}. reason: {msg}"))
                print(f"suppresed until {deadline}. reason: {msg}")
