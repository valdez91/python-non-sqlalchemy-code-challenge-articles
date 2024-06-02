# from author import Author
# from magazine import Magazine
# class Article:
#     _all_articles = []

#     def __init__(self, author, magazine, title):
#         if not isinstance(author, Author):
#             raise ValueError("Author must be an instance of Author class")
#         if not isinstance(magazine, Magazine):
#             raise ValueError("Magazine must be an instance of Magazine class")
#         if not isinstance(title, str) or not (5 <= len(title) <= 50):
#             raise ValueError("Title must be a string between 5 and 50 characters")
        
#         self._author = author
#         self._magazine = magazine
#         self._title = title
#         self.__class__._all_articles.append(self)
    
#     @property
#     def author(self):
#         return self._author

#     @author.setter
#     def author(self, value):
#         if isinstance(value, Author):
#             self._author = value
#         else:
#             raise ValueError("Author must be an instance of Author class")

#     @property
#     def magazine(self):
#         return self._magazine

#     @magazine.setter
#     def magazine(self, value):
#         if isinstance(value, Magazine):
#             self._magazine = value
#         else:
#             raise ValueError("Magazine must be an instance of Magazine class")

#     @property
#     def title(self):
#         return self._title
