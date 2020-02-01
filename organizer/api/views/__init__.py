from organizer.models import session


def view(func):
    """Add session management to views"""
    def wrapper(*args, **kwargs):
        try:
            response = func(*args, **kwargs)
            session.commit()
        except Exception as exc:
            session.rollback()
            raise exc
        finally:
            session.remove()
        return response

    return wrapper
