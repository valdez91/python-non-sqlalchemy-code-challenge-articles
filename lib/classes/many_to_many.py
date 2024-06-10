class Article:

    all = []
def __init__(self, author, magazine, title):
    self.author = author
    self.magazine = magazine
    self._title = str(title)
    Article.all.append(self)

@property 
def title(self):
    return self._title

@title.setter
def title(self, title):
   if hasattr(self,"title"):AttributeError("Title cannot be changed")
   else:
        if isinstance(title,str):
            if 5<=len(title)<=50:
                self._title=title
            else:
                raise ValueError("Title must be between 5 and 50 characheters")
        else:
            raise TypeError("Title must be a string")

    
class Author:

    all = []
def __init__(self, name):
    self._name = name
    Author.all.append(self)

@property
def name(self):
    return self._name

@name.setter
def name(self, value):
    self.new_names = value
    return self._name

#getting all articles written by the author
def articles(self):
    return[articles for articles in Article.all if articles.author == self]

#getting unique list of authors who have written for the magazine
def magazines(self):
    return list(set([article.magazine for article in self.articles()]))

def add_article(self, magazine, title):
    articles = Article(self, magazine, title)
    return articles

# categories of the magazines the author has contributed to
def topic_areas(self):
    return list(set([article.magazine.category for article in self.articles()])) if self.articles() else None
class Magazine:
    all = []
    def init(self, name, category):
        self._name = name
        self._category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            if 2 <= len(value) <= 16:
                self._name = value
            else: 
                ValueError("Name must be between 2 and 16 characters")
        else:
            TypeError("Name must be a string") 

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str):
            if len(value):
                self._category = value
            else:
                ValueError("Category must be longer than 0 characters")
        else:
            TypeError("Category must be a string")

def articles(self):
    return [articles for articles in Article.all if articles.magazine == self]

def contributors(self):
    return list(set([articles.author for articles in self.articles()]))

def article_titles(self):
    titles = [articles.title for articles in self.articles()]
    return titles if titles else None
   

def contributing_authors(self):
 #dict to hold authors
  authors = {}
  #loop through the articles
  for article in self.articles():
      #check if the author is already in the dict
      if article.author in authors:
          authors[article.author] += 1
      else:
          authors[article.author] = 1
  #create a list of authors who have written more than 2 articles
  contributing_authors = [author for author, count in authors.items() if count >= 2]
  return contributing_authors if contributing_authors else None

@classmethod
def top_publisher(cls):
    if not cls.all:
        return None
    return max(cls.all, key=lambda magazine: len(magazine.articles()))