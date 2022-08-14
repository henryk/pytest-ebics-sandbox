def test_sandbox_init(ebics_sandbox):
    assert ebics_sandbox
    assert ebics_sandbox.base_url


def test_sandbox_ping(ebics_sandbox):
    assert ebics_sandbox.ping()


def test_sandbox_rotate_keys(ebics_sandbox):
    assert ebics_sandbox.rotate_keys()


def test_sandbox_subscriber(ebics_sandbox):
    assert ebics_sandbox.new_subscriber()


# FIXME create, delete users
# FIXME Create running bank
# FIXME Non-session scoped sandbox
