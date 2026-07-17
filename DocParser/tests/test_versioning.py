from app.services.versioning import diff_nodes

def test_diff():
    result = diff_nodes(1, 2)
    assert isinstance(result, list)
