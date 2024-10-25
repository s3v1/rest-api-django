import time

# for i in {1..100}; do cp tests/slow/test_sleep.py tests/slow/test_sleep_$i.py; done


def test_sleep():
    sleep_seconds: float = 0.1
    time.sleep(sleep_seconds)
    assert True
