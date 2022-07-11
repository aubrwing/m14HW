import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        bookLover1 = BookLover("Aubrey","alw8ef@virginia.edu","Science Fiction")
        bookLover1.add_book("Harry Potter",5)
        test = bookLover1.book_list[bookLover1.book_list.book_name == "Harry Potter"]
        self.assertEqual(len(test),1)
    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        bookLover2 = BookLover("Aubrey","alw8ef@virginia.edu","Science Fiction")
        bookLover2.add_book("Harry Potter",5)
        bookLover2.add_book("Harry Potter",3)
        test2 = bookLover2.book_list[bookLover2.book_list.book_name == "Harry Potter"]
        self.assertEqual(len(test2),1)
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        bookLover3 = BookLover("Aubrey","alw8ef@virginia.edu","Science Fiction")
        bookLover3.add_book("Harry Potter",5)
        self.assertTrue(bookLover3.has_read("Harry Potter"))
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        bookLover4 = BookLover("Aubrey","alw8ef@virginia.edu","Science Fiction")
        bookLover4.add_book("Harry Potter",5)
        self.assertFalse(bookLover4.has_read("When Breath Becomes Air"))
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        bookLover5 = BookLover("Aubrey","alw8ef@virginia.edu","Science Fiction")
        bookLover5.add_book("Harry Potter",5)
        bookLover5.add_book("When Breath Becomes Air",5)
        bookLover5.add_book("Percy Jackson",3)
        self.assertEqual(bookLover5.num_books_read(),3)
    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        bookLover6 = BookLover("Aubrey","alw8ef@virginia.edu","Science Fiction")
        bookLover6.add_book("Harry Potter",4)
        bookLover6.add_book("When Breath Becomes Air",5)
        bookLover6.add_book("Percy Jackson",1)  
        bookLover6.add_book("Dune",2)
        favorite_books = bookLover6.fav_books()
        target = len(favorite_books[favorite_books.book_rating>3])
        self.assertEqual(target,2)
if __name__ == '__main__':
    
    unittest.main(verbosity=3)