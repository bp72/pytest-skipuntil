# -*- coding: utf-8 -*-



def test_skipuntil__later_date__expect_skipped(testdir):
    testdir.makepyfile("""
        import pytest
        from datetime import datetime

        @pytest.mark.skip_until(datetime.now())
        def test_hello_world(request):
            assert 1 == 2
    """)

    result = testdir.runpytest('-v')

    result.stdout.fnmatch_lines([
        '*::test_hello_world SKIPPED*',
    ])
    assert result.ret == 0
