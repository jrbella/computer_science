# create a page class
class Page:

    def __init__(self, page_text, next_page=None, page_number=None):
        """
        initializes the Page Object
        """
        self.page_text = page_text
        self.page_number = page_number
        self.next_page = next_page

    # getters
    def get_page_number(self):
        """
        should return a page number
        """
        return self.page_number

    def get_page_text(self):
        """
        should return the page text
        """
        return self.page_text

    def get_next_page(self):
        """
        should return the next page node (object)
        """
        return self.next_page

    # setters
    def set_page_number(self, page_number):
        """
        should update the page number on the Page object
        to the argument passed into it
        """
        self.page_number = page_number

    def set_page_text(self, new_text):
        """
        should take a new_text argument and update
        the Page Object with the argument
        """
        self.page_text = new_text
    
    def set_next_page(self, next_page):
        """
        I want to link a page, so I update the Page linked_object
        to another Page object
        """
        self.next_page = next_page

