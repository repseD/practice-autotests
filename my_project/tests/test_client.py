from my_project.clients.client import UsersClient


def test_get_users():
    client = UsersClient()
    response = client.get_users()

    assert response.status_code == 200

    users = response.json()
    assert isinstance(users, list)
    assert len(users) > 0

    user = users[0]
    assert "id" in user
    assert "name" in user
    assert "username" in user
    assert "email" in user

def test_post_posts():
    client = UsersClient()
    data = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response = client.post_posts(data)
    assert response.status_code == 201
    body = response.json()
    assert body["title"] == data["title"]
    assert body["body"] == data["body"]
    assert body["userId"] == data["userId"]
    assert "id" in body
