from uv_cookiecutter_test.foo import foo


def test_foo():
    assert foo("foo") == "foo"
