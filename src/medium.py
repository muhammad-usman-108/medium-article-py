import requests

class MediumArticles:
    def __init__(self):
        self.URL = 'https://api.rss2json.com/v1/api.json?rss_url=https://medium.com/feed/'
        self.error = {
            "message": "Invalid username..."
        }

    def get_base_url(self, username: str) -> str:
        if username.strip().startswith('@'):
            username = username[1:]
        return f"{self.URL}@{username}"

    def get_data(self, username: str) -> dict:
        try:
            response = requests.get(self.get_base_url(username))
            response.raise_for_status()
            data = response.json()
            return data
        except requests.exceptions.RequestException as e:
            print(f'An error occurred while fetching data: {e}')
            return {'error': 'An error occurred while fetching data'}

    def check_error(self, response: dict) -> bool:
        return response.get('status') != 'ok'

    def get_profile_url(self, username: str) -> str:
        try:
            data = self.get_data(username)
            if self.check_error(data):
                return self.error["message"]
            return data['feed']['url']
        except Exception as e:
            print(f'An error occurred while getting profile URL: {e}')
            return self.error["message"]

    def get_profile_title(self, username: str) -> str:
        try:
            data = self.get_data(username)
            if self.check_error(data):
                return self.error["message"]
            return data['feed']['title']
        except Exception as e:
            print(f'An error occurred while getting profile title: {e}')
            return self.error["message"]

    def get_profile_author(self, username: str) -> str:
        try:
            data = self.get_data(username)
            if self.check_error(data):
                return self.error["message"]
            return data['feed']['author']
        except Exception as e:
            print(f'An error occurred while getting profile author: {e}')
            return self.error["message"]

    def get_profile_description(self, username: str) -> str:
        try:
            data = self.get_data(username)
            if self.check_error(data):
                return self.error["message"]
            return data['feed']['description']
        except Exception as e:
            print(f'An error occurred while getting profile description: {e}')
            return self.error["message"]

    def get_profile_image_url(self, username: str) -> str:
        try:
            data = self.get_data(username)
            if self.check_error(data):
                return self.error["message"]
            return data['feed']['image']
        except Exception as e:
            print(f'An error occurred while getting profile image URL: {e}')
            return self.error["message"]

    def get_latest_article_title(self, username: str) -> str:
        try:
            data = self.get_data(username)
            if self.check_error(data):
                return self.error["message"]
            return data['items'][0]['title']
        except Exception as e:
            print(f'An error occurred while getting latest article title: {e}')
            return self.error["message"]

    def get_latest_article_publication_date(self, username: str) -> str:
        try:
            data = self.get_data(username)
            if self.check_error(data):
                return self.error["message"]
            return data['items'][0]['pubDate']
        except Exception as e:
            print(f'An error occurred while getting latest article publication date: {e}')
            return self.error["message"]

    def get_latest_article_url(self, username: str) -> str:
        try:
            data = self.get_data(username)
            if self.check_error(data):
                return self.error["message"]
            return data['items'][0]['link']
        except Exception as e:
            print(f'An error occurred while getting latest article URL: {e}')
            return self.error["message"]

    def get_latest_article_description(self, username: str) -> str:
        try:
            data = self.get_data(username)
            if self.check_error(data):
                return self.error["message"]
            return data['items'][0]['description']
        except Exception as e:
            print(f'An error occurred while getting latest article description: {e}')
            return self.error["message"]

    def get_latest_article(self, username: str) -> dict:
        try:
            data = self.get_data(username)
            if self.check_error(data):
                return self.error["message"]
            return data['items'][0]
        except Exception as e:
            print(f'An error occurred while getting latest article: {e}')
            return self.error["message"]

    def get_latest_articles_title(self, username: str) -> list:
        try:
            data = self.get_data(username)
            if self.check_error(data):
                return self.error["message"]
            res = [item['title'] for item in data['items']]
            return res
        except Exception as e:
            print(f'An error occurred while getting latest article titles: {e}')
            return self.error["message"]

# Example usage
# if __name__ == "__main__":
#     medium = MediumArticles()
#     username = "@engrmuhammadusman108"
#     print(medium.get_profile_url(username))
#     print(medium.get_profile_title(username))
#     print(medium.get_profile_author(username))
#     print(medium.get_profile_description(username))
#     print(medium.get_profile_image_url(username))
#     print(medium.get_latest_article_title(username))
#     print(medium.get_latest_article_publication_date(username))
#     print(medium.get_latest_article_url(username))
#     print(medium.get_latest_article_description(username))
#     print(medium.get_latest_article(username))
#     print(medium.get_latest_articles_title(username))
