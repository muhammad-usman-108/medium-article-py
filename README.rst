medium-article-py
====================================================

A Python library designed to retrieve articles and user information from Medium. This library offers an easy-to-use method for developers to incorporate Medium content into their applications.


Installation
------------

You can install this library using pip.

.. code-block:: python

    pip install medium-article-py


Usage
------------

Here is a simple example to get you started:

.. code-block:: python

    from medium-article-py import MediumArticles
    username = '<your-medium-username>'

    print(MediumArticles.get_profile_url(username))      
    # Output: https://medium.com/feed/@engrmuhammadusman108


.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Column 1 Header
     - Column 2 Header
   * - Row 1, Column 1
     - Row 1, Column 2
   * - Row 2, Column 1
     - Row 2, Column 2


Contributing
------------

- [Misbah Afzal](https://github.com/misbahafzal)
- [Muhammad Usman](https://github.com/muhammad-usman-108)

LICENSE
------------

This project is licensed under the MIT License - see the [LICENSE](https://github.com/muhammad-usman-108/medium-article-py/blob/main/LICENSE) file for details.