import requests


class UsersClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def get_users(self):
        return requests.get(f"{self.BASE_URL}/users")
        
    def post_posts(self, data):
        return requests.post(f"{self.BASE_URL}/posts", json=data)
