# -*- coding: utf-8 -*-
from datetime import datetime

import pytest


# TODO: [ ] datetime -> date switch

MARKER_NAME = "skip_until"

def pytest_configure(config):
    config.addinivalue_line(
        "markers", f"{MARKER_NAME}(...): skip test until datetime"
    )


def pytest_collection_modifyitems(items):
    for testcase in items:       
        for marker in testcase.own_markers:            
            if marker.name == "skip_until":
                deadline = marker.kwargs.get("deadline")                
                
                if deadline is None:                    
                    raise Exception("deadline is not defined!")

                msg = marker.kwargs.get("msg") or ""

                if datetime.now() > deadline:
                    continue
                
                testcase.add_marker(pytest.mark.skip(reason=f"suppresed until {deadline}. reason: {msg}"))
