COUNTER_KEY = 'test_cache/counter'

def test_cache(cache):  # <1>
    value = cache.get(COUNTER_KEY, 0)
    print("Counter before:", value)
    cache.set(COUNTER_KEY, value + 1)  # <2>
    value = cache.get(COUNTER_KEY, 0)  # <2>
    print("Counter after:", value)
    assert True   # <3>

def hello():
    print("Hello, pytesting world")

def test_capsys(capsys):
    hello()  # <4>
    out, err = capsys.readouterr()  # <5>
    print("STDOUT:", out)

def bhello():
    print(b"Hello, binary pytesting world\n")

def test_capsysbinary(capsys):
    bhello()  # <6>
    out, err = capsys.readouterr()  # <7>
    print("BINARY STDOUT:", out)

def test_temp_dir1(tmpdir):
    print("TEMP DIR:", str(tmpdir))  # <8>

def test_temp_dir2(tmpdir):
    print("TEMP DIR:", str(tmpdir))

def test_temp_dir3(tmpdir):
    print("TEMP DIR:", str(tmpdir))
