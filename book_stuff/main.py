from book_stuff.pages import Page
from book_stuff.chapter import Chapter

def main():

    # run imported functions here
    # 3 pages
    page_one = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Molestie at elementum eu facilisis sed. Ac turpis egestas maecenas pharetra. Purus viverra accumsan in nisl nisi. Felis eget velit aliquet sagittis. Donec pretium vulputate sapien nec sagittis. Nunc lobortis mattis aliquam faucibus purus in massa tempor. Nec ultrices dui sapien eget mi proin sed. In metus vulputate eu scelerisque felis imperdiet proin fermentum leo. Non consectetur a erat nam at lectus urna. Suspendisse ultrices gravida dictum fusce ut placerat orci nulla pellentesque. Turpis tincidunt id aliquet risus feugiat. Mollis nunc sed id semper risus in hendrerit. Arcu dui vivamus arcu felis bibendum ut tristique et egestas. Purus viverra accumsan in nisl nisi scelerisque eu ultrices. Magna fringilla urna porttitor rhoncus dolor purus non. Risus pretium quam vulputate dignissim suspendisse in est."
    page_two = "Vel turpis nunc eget lorem dolor sed viverra ipsum. Nisi vitae suscipit tellus mauris a diam. Interdum consectetur libero id faucibus nisl. Rhoncus dolor purus non enim praesent elementum facilisis leo. Et tortor consequat id porta nibh. Suscipit adipiscing bibendum est ultricies integer quis. Egestas sed sed risus pretium quam vulputate dignissim suspendisse in. Nulla aliquet porttitor lacus luctus accumsan. Bibendum neque egestas congue quisque. Vitae purus faucibus ornare suspendisse sed. In metus vulputate eu scelerisque felis imperdiet. Sit amet nisl purus in mollis nunc sed id semper. Amet nisl purus in mollis. Et magnis dis parturient montes nascetur ridiculus mus mauris vitae. Vitae tempus quam pellentesque nec nam aliquam sem et tortor. Donec et odio pellentesque diam. Nisi scelerisque eu ultrices vitae auctor eu. Accumsan lacus vel facilisis volutpat est."
    page_three= "Malesuada proin libero nunc consequat interdum varius sit amet mattis. Elit scelerisque mauris pellentesque pulvinar pellentesque habitant morbi tristique. Morbi tincidunt augue interdum velit euismod in pellentesque massa placerat. Nunc mattis enim ut tellus elementum. Amet massa vitae tortor condimentum lacinia quis. In metus vulputate eu scelerisque felis imperdiet proin. Eget sit amet tellus cras adipiscing enim eu turpis egestas. Non sodales neque sodales ut etiam sit amet. Non diam phasellus vestibulum lorem sed. Sed ullamcorper morbi tincidunt ornare massa eget. Libero id faucibus nisl tincidunt eget nullam non nisi. Ut faucibus pulvinar elementum integer enim neque volutpat ac tincidunt. Dignissim suspendisse in est ante. Felis donec et odio pellentesque. Vitae aliquet nec ullamcorper sit. Eget aliquet nibh praesent tristique magna sit amet purus. Bibendum ut tristique et egestas quis ipsum suspendisse. Sem nulla pharetra diam sit amet nisl suscipit adipiscing."
    page_four = "Eu nisl nunc mi ipsum faucibus vitae. Diam vel quam elementum pulvinar. Orci ac auctor augue mauris. Praesent tristique magna sit amet. Scelerisque eu ultrices vitae auctor eu. Commodo odio aenean sed adipiscing. Tempor commodo ullamcorper a lacus vestibulum sed arcu non odio. At tempor commodo ullamcorper a lacus vestibulum. Mollis nunc sed id semper risus in. Eu nisl nunc mi ipsum faucibus vitae. Lacinia quis vel eros donec ac odio tempor orci dapibus. Varius sit amet mattis vulputate. Sagittis nisl rhoncus mattis rhoncus urna neque viverra. Lacus laoreet non curabitur gravida arcu ac tortor dignissim. Et molestie ac feugiat sed lectus vestibulum mattis ullamcorper velit. Tortor vitae purus faucibus ornare suspendisse sed nisi lacus sed."

    # print our chapter
    new_chapter = Chapter()

    # add our pages

    new_chapter.insert_page(page_one)
    new_chapter.insert_page(page_two)
    new_chapter.insert_page(page_three)
    new_chapter.insert_page(page_four)

    print_chapter_text = new_chapter.print_chapter()
    print(print_chapter_text)
# run our application


main()


