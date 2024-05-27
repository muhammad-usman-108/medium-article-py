# medium-article-py
A Python library designed to retrieve articles and user information from Medium. This library offers an easy-to-use method for developers to incorporate Medium content into their applications.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Scripts](#scripts)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Installation

You can install this library using pip.

```pip install medium-article-py```

## Usage

Here is a simple example to get you started:

```python
from medium-article-py import MediumArticles
username = '<your-medium-username>'

print(MediumArticles.get_profile_url(username))      
# Output: https://medium.com/feed/@engrmuhammadusman108

```

### Functions


| Function | Arguments | Output |
|---------|---------| ---------|
| getData| _username_: string | string | 
| getProfileUrl| _username_: string| string |
| getProfileTitle| _username_: string| string |
| getProfileAuthor| _username_: string| string |
| getProfileDescription| _username_: string| string |
| getProfileImageUrl| _username_: string| string |
| getLatestArticleTitle| _username_: string| array[string]|
| getLatestArticlePublicationDate| _username_: string| string |
| getLatestArticleUrl| _username_: string| string |
| getLatestArticleDescription| _username_: string| html |
| getLatestArticle| _username_: string| object |
| getLatestArticlesTitle| _username_: string| string |


## Contributing

- [Misbah Afzal](https://github.com/misbahafzal)
- [Muhammad Usman](https://github.com/muhammad-usman-108)

## LICENSE

This project is licensed under the MIT License - see the [LICENSE](https://github.com/muhammad-usman-108/medium-article-api/blob/main/LICENSE) file for details.
