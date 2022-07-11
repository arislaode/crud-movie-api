import unittest
from app.db.model import Movie

class MovieTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''

        self.new_movie = Movie(id=1234, title='Turning Red', rating=8.5, image="\\x2f396a2f34414151536b5a4a52674142415145424c4145734141442f3277424441")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_movie,Movie))

    def test_init(self):
        self.assertEqual(self.new_movie.id,1234)
        self.assertEqual(self.new_movie.title,"Turning Red")
        self.assertEqual(self.new_movie.rating,8.5)
        self.assertEqual(self.new_movie.image,"\\x2f396a2f34414151536b5a4a52674142415145424c4145734141442f3277424441")


if __name__ == "__main__":
    unittest.main()