from app.services.utils import sha256

def test_sha256():
    h = sha256("hello")
    assert len(h) == 64
    assert h == sha256("hello")
