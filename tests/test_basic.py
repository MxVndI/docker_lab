def test_basic():
    """Basic test to ensure pytest is working"""
    assert True

def test_imports():
    """Test that we can import our modules"""
    try:
        from src.main import app
        from src.models import User
        from src.schemas import UserCreate, User as UserSchema
        assert app is not None
        assert User is not None
        assert UserCreate is not None
        assert UserSchema is not None
    except ImportError as e:
        assert False, f"Failed to import modules: {e}" 