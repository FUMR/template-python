def test_basic(val=6):
    # NOTE: range is generating numbers 0..n-1
    #  So we simply add 1
    assert sum(range(val ** 2 + 1)) == 666
