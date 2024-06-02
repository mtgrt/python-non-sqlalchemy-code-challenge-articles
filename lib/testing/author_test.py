from classes.many_to_many import Author, Magazine, Article
import pytest

class TestAuthor:
    def test_name_is_immutable_string(self):
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        assert isinstance(author_1.name, str)
        assert isinstance(author_2.name, str)
        with pytest.raises(AttributeError):
            author_1.name = "ActuallyTopher"

    def test_has_many_articles(self):
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author_1, magazine, "How to wear a tutu with style")
        article_2 = Article(author_1, magazine, "Dating life in NYC")
        article_3 = Article(author_2, magazine, "How to be single and happy")
        assert len(author_1.articles) == 2

    def test_articles_of_type_articles(self):
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine = Magazine("Vogue", "Fashion")
        Article(author_1, magazine, "How to wear a tutu with style")
        Article(author_2, magazine, "Dating life in NYC")
        assert isinstance(author_1.articles[0], Article)

    def test_has_many_magazines(self):
        author_1 = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        magazine_3 = Magazine("GQ", "Fashion")
        Article(author_1, magazine_1, "How to wear a tutu with style")
        Article(author_1, magazine_2, "2023 Eccentric Design Trends")
        assert magazine_1 in author_1.magazines

    def test_magazines_of_type_magazine(self):
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        magazine_3 = Magazine("GQ", "Fashion")
        Article(author_1, magazine_1, "How to wear a tutu with style")
        Article(author_1, magazine_2, "2023 Eccentric Design Trends")
        Article(author_2, magazine_3, "How to be single and happy")
        assert isinstance(author_1.magazines[0], Magazine)

    def test_magazines_are_unique(self):
        author_1 = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        Article(author_1, magazine_1, "How to wear a tutu with style")
        Article(author_1, magazine_2, "2023 Eccentric Design Trends")
        Article(author_1, magazine_2, "Carrara Marble is so 2020")
        assert len(set(author_1.magazines)) == len(author_1.magazines)

    def test_add_article(self):
        author_1 = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        article_1 = author_1.add_article(magazine_1, "How to wear a tutu with style")
        article_2 = author_1.add_article(magazine_2, "2023 Eccentric Design Trends")
        article_3 = author_1.add_article(magazine_2, "Carra Marble is so 2020")
        assert isinstance(article_1, Article)
        assert len(author_1.articles) == 3

