import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):

        collector.add_new_book("Гордость и предубеждение и зомби")
        collector.add_new_book("Что делать, если ваш кот хочет вас убить")

        assert len(collector.get_books_genre()) == 2


    @pytest.mark.parametrize("invalid_name", ["", "В" * 41, "Д" * 42])
    def test_add_new_book_book_with_invalid_name_is_not_added_to_collection(
        self, invalid_name, collector
    ):
        collector.add_new_book(invalid_name)
        assert len(collector.get_books_genre()) == 0


    @pytest.mark.parametrize(
        "valid_genre", ["Фантастика", "Ужасы", "Детективы", "Мультфильмы", "Комедии"]
    )
    def test_set_book_genre_successfully_updates_existing_book_genre(
        self, collector, valid_genre
    ):

        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", valid_genre)
        assert collector.get_book_genre("Гарри Поттер") == valid_genre


    @pytest.mark.parametrize("invalid_genre", ["", "Фанфик", "Попаданцы", "Фэнтези"])
    def test_set_book_genre_invalid_updates_not_existing_book_genre(
        self, collector, invalid_genre
    ):

        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", invalid_genre)

        assert collector.get_book_genre("Гарри Поттер") == ""


    def test_that_gets_books_of_specific_genre_from_list_and_returns_an_empty_list(
        self, collector
    ):

        collector.add_new_book("Красная шапочка")
        collector.add_new_book("Гордость и предубеждение и зомби")

        collector.set_book_genre("Красная шапочка", "Мультфильмы")
        collector.set_book_genre("Гордость и предубеждение и зомби", "Детективы")

        result = collector.get_books_with_specific_genre("Мультфильмы")

        assert result == ["Красная шапочка"]

 
    def test_get_books_with_specific_genre_returns_empty_for_invalid_genre(
        self, collector
    ):

        result = collector.get_books_with_specific_genre("Фанфик")

        assert result == []


    def test_get_book_genre_returns_correct_genre_for_existing_book(self, collector):

        collector.add_new_book("Красная шапочка")
        collector.set_book_genre("Красная шапочка","Мультфильмы")

        result = collector.get_book_genre("Красная шапочка")
        assert result == "Мультфильмы"


    def test_get_book_genre_returns_none_for_nonexistent_book(self, collector):

        result = collector.get_book_genre("Фрилансер")
        
        assert result is None


    def test_get_books_genre_returns_dictionary_of_books_and_genres(self,collector):

        collector.add_new_book("Красная шапочка")
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Красная шапочка", "Мультфильмы")
        collector.set_book_genre("Гарри Поттер", "Фантастика")

        result = collector.get_books_genre()

        confirmation = {
            "Красная шапочка" : "Мультфильмы",
            "Гарри Поттер" : "Фантастика"
        }

        assert result == confirmation

  

    def test_get_books_genre_returns_empty_dict_when_no_books(self,collector):

        result = collector.get_books_genre()

        assert result == {}


    def test_get_books_for_children_returns_child_friendly_books(self,collector):

        collector.add_new_book("Красная шапочка")
        collector.add_new_book("Гарри Поттер")
        collector.add_new_book("Три поросёнка")

        collector.set_book_genre("Красная шапочка", "Ужасы")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        collector.set_book_genre("Три поросёнка", "Мультфильмы")

        result = collector.get_books_for_children()

        assert result == ["Гарри Поттер","Три поросёнка"]



    def test_get_books_for_children_returns_empty_list_when_no_child_friendly_books(self, collector):
       
       collector.add_new_book("Сияние")
       collector.set_book_genre("Сияние", "Ужасы")
    
       result = collector.get_books_for_children()

       assert result == []



    def test_add_book_in_favorites_adds_existing_book_to_favorites(self, collector):

        collector.add_new_book("Сияние")
        collector.add_book_in_favorites("Сияние")  
    
        assert collector.get_list_of_favorites_books() == ["Сияние"]

 

    def test_add_book_in_favorites_ignores_nonexistent_book(self, collector):

        collector.add_book_in_favorites("Оно") 

        assert collector.get_list_of_favorites_books() == []


    
    def test_delete_book_from_favorites_removes_book_from_favorites(self, collector):

        collector.add_new_book("Дюна")
        collector.add_book_in_favorites("Дюна")

        collector.delete_book_from_favorites("Дюна")
    
        assert collector.get_list_of_favorites_books() == []




    def test_delete_book_from_favorites_ignores_nonexistent_favorite(self, collector):

        collector.delete_book_from_favorites("Война и мир")
        
        assert collector.get_list_of_favorites_books() == []



    def test_get_list_of_favorites_books_returns_correct_list(self, collector):
        collector.add_new_book("Дюна")
        collector.add_new_book("Гарри Поттер")
        collector.add_book_in_favorites("Дюна")
        collector.add_book_in_favorites("Гарри Поттер")
        
        result = collector.get_list_of_favorites_books()

        assert result == ["Дюна", "Гарри Поттер"]


    def test_get_list_of_favorites_books_returns_empty_list_when_no_favorites(self, collector):
        result = collector.get_list_of_favorites_books()

        assert result == []