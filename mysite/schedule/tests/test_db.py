import pytest

@pytest.mark.django_db
def test_my_user():
    me = User.objects.get(username='admin')
    assert me.is_superusers
