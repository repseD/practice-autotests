from my_project.clients.client import UsersClient

# review: в двух тестовых методах ты инициализируешь клиента,
# это дублирование кода и ненужное повторение действия для теста, по-хорошему создать здесь тестовый класс:
# class TestClient: в котором ты один раз для всех тестов проинициализируешь клиента,
# а дальше в тестах будешь через self обращаться к нему

# review: отсутствуют аннотации allure как на тестовых методах, так и в шагах тестов
def test_get_users():
    client = UsersClient()
    response = client.get_users()

    # review: в QAUtils эта проверка встроена в механизм запросов, её не пришлось бы выполнять
    assert response.status_code == 200

    users = response.json()
    assert isinstance(users, list)
    assert len(users) > 0

    # review: данные проверки - контрактное тестирование.
    # Помимо того, что проверяется их наличие здесь же можно проверить ещё и их типы
    user = users[0]
    assert "id" in user
    assert "name" in user
    assert "username" in user
    assert "email" in user

# review: в прошлом тесте шаги были выделены переходами на новую строку,
# это увеличивало читаемость теста, в данном тесте их не стало
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
