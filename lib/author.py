# from article import Article
# class Author:
#     def __init__(self, name):
#         if isinstance(name, str) and len(name) > 0:
#             self._name = name
#         else:
#             raise ValueError("Name must be a non-empty string")
    
#     @property
#     def name(self):
#         return self._name

#     def articles(self):
#         return [article for article in Article._all_articles if article.author == self]
    
#     def magazines(self):
#         return list(set(article.magazine for article in self.articles()))
    
#     def add_article(self, magazine, title):
#         return Article(self, magazine, title)

#     def topic_areas(self):
#         return list(set(magazine.category for magazine in self.magazines())) if self.articles() else None
