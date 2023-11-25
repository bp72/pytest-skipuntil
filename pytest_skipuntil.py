from datetime import datetime
from enum import Enum
from logging import getLogger

import pytest


logger = getLogger(__name__)

# TODO: [ ] datetime -> date switch
# TODO: [ ] add strict feature

MARKER_NAME = "skip_until"


class MessageLevel(str, Enum):
    error = "error"
    warning = "warning"


class SkipUntilPlugin:

    name = MARKER_NAME

    def __init__(self, config):
        self.config = config
        self.messages = []

    def pytest_collection_modifyitems(self, items):
        for testcase in items:
            for marker in testcase.own_markers:
                if marker.name == "skip_until":
                    deadline = marker.kwargs.get("deadline")
                    if not deadline and marker.args:
                        deadline = marker.args[0]

                    if deadline is None:
                        raise pytest.UsageError("The deadline is not defined for skip_until!")

                    if not isinstance(deadline, datetime):
                        raise pytest.UsageError(
                            f"Unexpected deadline type {type(deadline)} is passed "
                            f"to skip_until, please specify a datetime!",
                        )

                    file_location = testcase.location[0]
                    if datetime.now() > deadline:
                        self.messages.append(
                            (
                                f"{file_location}::{testcase.name}: the deadline for "
                                "the test has passed",
                                MessageLevel.error,
                            )
                        )
                        continue

                    msg = marker.kwargs.get("msg") or "not specified"
                    message = f"The test is suppressed until {deadline}. The reason is: {msg}"
                    self.messages.append((f"{file_location}: {message}", MessageLevel.warning))
                    testcase.add_marker(pytest.mark.skip(reason=message))

    def pytest_terminal_summary(
        self,
        terminalreporter,
        exitstatus,
        config,
    ) -> None:
        for message, level in self.messages:
            if level == MessageLevel.error:
                terminalreporter.write_line(message, red=True)
            if level == MessageLevel.warning:
                terminalreporter.write_line(message, yellow=True)


def pytest_configure(config):
    config.pluginmanager.register(SkipUntilPlugin(config), SkipUntilPlugin.name)
    config.addinivalue_line(
        "markers",
        f"{MARKER_NAME}(...): skip test until datetime",
    )
