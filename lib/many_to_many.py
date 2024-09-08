class Author:
    all=[]
    def __init__(self,name):
        if not isinstance(name,str) or not name: #This checks whether the title is an empty string or any other "falsy" value
            raise Exception("Please Enter a valid name")
        self.name=name
        Author.all.append(self)
    
    def contracts(self):
        return[contract for contract in Contract.all if contract.author ==self]
    
    def books(self):
        return[contract.book for contract in self.contracts()]
    
    def sign_contract(self,book, date, royalties):
        if not isinstance(book,Book):
            raise Exception("Invalid book. Must be an instance of Book.")
        contract=Contract(self,book,date,royalties)
        return contract
    
    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())


class Book:
    all=[]
    def __init__(self,title):
        if not isinstance(title,str) or not title:
            raise Exception("Please Enter a valid title")
        self.title=title
        Book.all.append(self)
    
    def contracts(self):
        return[contract for contract in Contract.all if contract.book ==self]
    
    def authors(self):
        return[contract.author for contract in self.contracts()]


class Contract:
    all=[]
    def __init__(self,author,book,date,royalties):
        
        if not isinstance(author, Author):
                raise Exception("Invalid author. Must be an instance of Author.")
        if not isinstance(book, Book):
            raise Exception("Invalid book. Must be an instance of Book.")
        if not isinstance(date, str) or not date:
            raise Exception("Invalid date. Date must be a non-empty string.")
        if not isinstance(royalties, int) or royalties < 0:
            raise Exception("Royalties must be a non-negative integer.")
        
        self.book =book
        self.date=date
        self.author=author
        self.royalties=royalties
        Contract.all.append(self)
    
    @classmethod  
    def contracts_by_date(cls, date):
        if not isinstance(date, str) or not date:
            raise Exception("Invalid date. Date must be a non-empty string.")
        return [contract for contract in cls.all if contract.date == date]