from _pytest.config import ExitCode


def test_skip_until__today__expect_skipped(testdir):
    testdir.makepyfile("""
        import pytest
        from datetime import datetime, timedelta

        @pytest.mark.skip_until(deadline=datetime.now() + timedelta(seconds=1))
        def test_skip_until__today__expect_skipped(request):
            assert 1 == 2
    """)

    result = testdir.runpytest("-v")

    result.stdout.fnmatch_lines([
        "*::test_skip_until__today__expect_skipped SKIPPED*",
    ])
    result.stdout.fnmatch_lines([
        "test_skip_until__today__expect_skipped.py: The test is suppressed until*",
    ])
    assert result.ret == ExitCode.OK


def test_skip_until__deadline_in_args__expect_skipped(testdir):
    testdir.makepyfile("""
        import pytest
        from datetime import datetime, timedelta

        @pytest.mark.skip_until(datetime.now() + timedelta(seconds=1))
        def test_skip_until__today__expect_skipped(request):
            assert 1 == 2
    """)

    result = testdir.runpytest("-v")

    result.stdout.fnmatch_lines([
        "*::test_skip_until__today__expect_skipped SKIPPED*",
    ])
    assert result.ret == ExitCode.OK


def test_skip_until__today__expect_suppressed_message(testdir):
    testdir.makepyfile("""
        import pytest
        from datetime import datetime, timedelta

        @pytest.mark.skip_until(
            deadline=datetime(2023, 12, 11),
            msg="The test is flaky"
        )
        def test_skip_until__today__expect_suppressed_message(request):
            assert 1 == 2
    """)

    result = testdir.runpytest("-rsx")

    result.stdout.fnmatch_lines([
        "*The test is suppressed until 2023-12-11 00:00:00. "
        "The reason is: The test is flaky*"
    ])
    assert result.ret == ExitCode.OK


def test_skip_until__later_date__expect_not_being_skipped(testdir):
    testdir.makepyfile("""
        import pytest
        from datetime import datetime, timedelta

        @pytest.mark.skip_until(deadline=datetime.now() - timedelta(seconds=1))
        def test_skip_until__later_date__expect_not_being_skipped(request):
            assert 1 == 2
    """)

    result = testdir.runpytest("-v")

    result.stdout.fnmatch_lines([
        "*::test_skip_until__later_date__expect_not_being_skipped FAILED*",
    ])
    result.stdout.fnmatch_lines([
        "test_skip_until__later_date__expect_not_being_skipped.py::"
        "test_skip_until__later_date__expect_not_being_skipped: the deadline "
        "for the test has passed*",
    ])
    assert result.ret == ExitCode.TESTS_FAILED


def test_skip_until__no_deadline_arg__expect_exception(testdir):
    testdir.makepyfile("""
        import pytest
        from datetime import datetime, timedelta

        @pytest.mark.skip_until()
        def test_skip_until__no_deadline_arg__expect_exception(request):
            assert 1 == 2
    """)

    result = testdir.runpytest("-v")

    result.stderr.fnmatch_lines([
        "ERROR: The deadline is not defined for skip_until!",
    ])

    assert result.ret == ExitCode.USAGE_ERROR


def test_skip_until__invalid_deadline_type__expect_exception(testdir):
    testdir.makepyfile("""
        import pytest
        from datetime import datetime, timedelta

        @pytest.mark.skip_until(deadline="test")
        def test_skip_until__no_deadline_arg__expect_exception(request):
            assert 1 == 2
    """)

    result = testdir.runpytest("-v")

    result.stderr.fnmatch_lines([
        "ERROR: Unexpected deadline type <class 'str'> is passed "
        "to skip_until, please specify a datetime!",
    ])

    assert result.ret == ExitCode.USAGE_ERROR
