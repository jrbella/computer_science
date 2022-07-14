from book_stuff.pages import Page

class Chapter:
    
    def __init__(self, page=None):
        self.head_page = page

    
    # getter
    def get_head_page(self):
        """
        should return the first page of the chapter
        """
        return self.head_page
      



    # insert page at the begining of the chapter
    def insert_page(self, new_entry):
        """
        creates a new page object
        points the new page object at the current head page
        set the head page to the new page object
        set the page number on the new page
        """

        new_page = Page(new_entry)
        # link the page to another page
        new_page.set_next_page(self.get_head_page())
        # set the page page number
        if(self.get_head_page() == None):
            new_page.set_page_number(1)
        else:
            new_page.set_page_number(self.get_head_page().get_page_number() + 1)
        self.head_page =  new_page

    # delete a page
    def remove_page(self, page_number):
        """
        find the page number and delete the page
        """

    # print chapterd

    def print_chapter(self):
        """ 
        print out the chapter
        """

        # debug
        chapter_printer = ""
        current_page = self.get_head_page()
        while current_page:
            if current_page.get_page_text() != None:
                full_string = ""
                full_string += ("\n\n Page Number " + str(current_page.get_page_number()) + "\n\n")
                full_string += str(current_page.get_page_text()) + "\n"
                chapter_printer = full_string + chapter_printer 
            current_page = current_page.get_next_page()
        return chapter_printer
    # insert a page at the end of the chapter