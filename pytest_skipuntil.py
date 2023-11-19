from datetime import datetime

import pytest


# TODO: [ ] datetime -> date switch
# TODO: [ ] add strict feature

MARKER_NAME = "skip_until"


def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        f"{MARKER_NAME}(...): skip test until datetime",
    )


def pytest_collection_modifyitems(items):
    for testcase in items:
        for marker in testcase.own_markers:
            if marker.name == "skip_until":
                deadline = marker.kwargs.get("deadline")

                if deadline is None:
                    raise pytest.UsageError(
                        "The deadline is not defined for skip_until!",
                    )

                msg = marker.kwargs.get("msg") or ""

                if datetime.now() > deadline:
                    continue

                testcase.add_marker(
                    pytest.mark.skip(
                        reason=(
                            f"The test is suppressed until {deadline}. "
                            f"The reason is: {msg}"
                        ),
                    ),
                )
