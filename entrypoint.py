try:
    from app import create_app
    application = create_app()
except ImportError:
    raise RuntimeError("Couldn't import dependencies")
