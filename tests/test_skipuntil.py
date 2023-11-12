# -*- coding: utf-8 -*-

# TODO: [ ] add test to cover no deadline arg


def test_skipuntil__later_date__expect_skipped(testdir):
    testdir.makepyfile("""
        import pytest
        from datetime import datetime, timedelta

        @pytest.mark.skip_until(deadline=datetime.now()+timedelta(seconds=1))
        def test_skipuntil__later_date__expect_skipped(request):
            assert 1 == 2
    """)


    result = testdir.runpytest('-v')
    result.stdout.fnmatch_lines([
        '*::test_skipuntil__later_date__expect_skipped SKIPPED*',
    ])
    assert result.ret == 0


def test_skipuntil__later_date__expect_not_being_skipped(testdir):
    testdir.makepyfile("""
        import pytest
        from datetime import datetime, timedelta

        @pytest.mark.skip_until(deadline=datetime.now()-timedelta(seconds=1))
        def test_skipuntil__later_date__expect_not_being_skipped(request):
            assert 1 == 2
    """)

    result = testdir.runpytest('-v')

    result.stdout.fnmatch_lines([
        '*::test_skipuntil__later_date__expect_not_being_skipped FAILED*',
    ])

    assert result.ret == 1
