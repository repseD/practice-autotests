# review: ожидалось использование библиотеки QAUtils,
# в т.ч. важный момент, что мы испольузем внутри неё httpx вместо requests

# review: в данном модуле собраны все запросы и он называется client.py, это ок,
# но нужно разделять клиентов по функциональности: users_client.py, posts_client.py, ...
import requests


class UsersClient:
    # review: гуд, что вынес base_url в переменную, но мы выносим их в .env,
    # так как при масштабировании base_url будет использоваться во многих клиентах
    BASE_URL = "https://jsonplaceholder.typicode.com"

    # review: т.к. блока логики нет, то в данном случае не хватает докстринга, описания того, что метод делает
    def get_users(self):
        return requests.get(f"{self.BASE_URL}/users")

    # review: важный момент, класс называется UsersClient, а здесь мы уже обращаемся к ручке,
    # которая работает с постами, т.е. для этой ручки нужен был отдельный модуль posts_client.py
    def post_posts(self, data):
        return requests.post(f"{self.BASE_URL}/posts", json=data)
