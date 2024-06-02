#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

class Author:
    def __init__(self, name):
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set([article.magazine for article in self._articles]))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    def topic_areas(self):
        return list(set([article.magazine.category for article in self._articles]))


class Magazine:
    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set([article.author for article in self._articles]))

    def article_titles(self):
        return [article.title for article in self._articles]

    def contributing_authors(self):
        authors_count = {}
        for article in self._articles:
            authors_count[article.author] = authors_count.get(article.author, 0) + 1
        return [author for author, count in authors_count.items() if count > 2]

    @classmethod
    def top_publisher(cls):
        all_magazines = []  # You need to maintain a list of all Magazine instances somewhere
        if not all_magazines:
            return None
        return max(all_magazines, key=lambda magazine: len(magazine.articles()))


class Article:
    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine
