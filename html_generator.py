# Creates outer div and h2 tag for every lesson. 
#   part_index: lesson number
#   part_title: lessons title
#   sections: the inner content for every lesson
def generate_chapter_HTML(part_index, part_title, sections):
    block1 = '''
    <div class="part">
        <h2 id="part-''' + str(part_index) + '">' + str(part_index)+'.' + part_title + '</h2>' # Setting chapter number and title.
    block2 = sections + '''
    </div>'''
    return block1 + block2

# Creates HTML for lessons subcategories.
#   part_index is lesson number
#   section_index: order number in subcategory
#   section_title: subcategory title
#   section_secription: subcategory description
def generate_section_HTML( part_index, section_index, section_title, section_description):
    block1 = '''    
        <div class="section" id="section-''' + str(part_index) + '-' + str(section_index) + '">' #Setting chapter and subsection for the id.   
    block2 = '''    
            <div class="section-title">''' + section_title + '</div>' # Section title
    block3 = '''
            <div class="section-description">
                '''     + section_description         #And the description.
    block4 = '''                
            </div>
        </div>'''
    return block1 + block2 + block3 + block4

# Creates HTML for table of content.
#   part_index is lesson number
#   section_index: order number in subcategory
#   section_title: subcategory title
def generate_toc_HTML(part_index, section_index, section_title):
    block1 = '''
                    <li><a href="#section-'''+str(part_index)+'-'+str(section_index)+ '">'+section_title+'</a></li>'
                
    return block1

# Extracts data from list and passes it to generate_section_HTML and then in generate_chapter_HTML. Returns HTML for a lesson.
#   chapter: list with lesson's data
def make_HTML(chapter):
    if len(chapter) != 0:       # Checks for empty list
        part_index = chapter[0]
        part_title = chapter[1]
        section = chapter[2]
        sections = ''
        if len(section) != 0:
            for el in section:
                section_index = el[0]
                section_title = el[1]
                section_description = el[2]
                sections += generate_section_HTML( part_index, section_index, section_title, section_description)   
    return generate_chapter_HTML(part_index, part_title, sections)

# Extracts data from list with lessons. Returns HTML for all lessons in the list.
def multiple_chapters(chapters):
    html = ''
    if len(chapters) != 0:      #Checks if empty
        for chapter in chapters:
            html += make_HTML(chapter)
    return html

# Extracts data from a list, passes it to generate_toc_HTML and creates HTML for the content table.
def make_toc_HTML(chapter):
    part_index = chapter[0]
    if chapter[2]:              #Checks for value
        sections = chapter[2]
        sections_content = ''
        for section in sections:
            section_index = section[0]
            section_title = section[1]
            sections_content += generate_toc_HTML(part_index, section_index, section_title)
    return sections_content




# Lists for Part 5

chapter5 = [5]
chapter_title5 = "Programming"
chapter5.append(chapter_title5)

section5_1 = [1]
section_title5_1 = "What is programming?"
section_description5_1 = "<p>Programming is the process of giving computers certain instructions using a programming language. There are many different programming languages, but the language we're using in our study is called Python.</p>"
section5_1.extend([section_title5_1, section_description5_1]) #found this in python docs. hope you don't mind, using it ;)

section5_2 = [2]
section_title5_2 = "Why using programming languages?"
section_description5_2 = "<p>We use programming languages because of their unambiguity. In natural languages one thing may mean different things where as in programming languages every command is unambiguous meaning there is only one interpretation.</p>"
section5_2.extend([section_title5_2, section_description5_2])

sections_part_5 = []
sections_part_5.extend([section5_1, section5_2])

chapter5.append(sections_part_5)

#Lists for Part 6

chapter6 = [6]
chapter_title6 = "Python"
chapter6.append(chapter_title6)

section6_1 = [1]
section_title6_1 = "Python expressions"
section_description6_1 = "<p>Just like the grammar rules in natural languages there are rules in every programming language called syntax that have to be followed. Expression is something that has a value. We can also make an expression by combining other expressions with a set of operators (e.g. +, -, *, /).</p>"
section6_1.extend([section_title6_1, section_description6_1])

section6_2 = [2]
section_title6_2 = "Variables"
section_description6_2 = "<p>Variable is a name created by us that refers to a value. The way to introduce a variable is by using an assignment statement (e.g. name = expression). A name could be any combination of characters as long as it starts with a letter and is not one of the Python keywords. Variables can change their value.</p>"
section6_2.extend([section_title6_2, section_description6_2])

sections_part_6 = []
sections_part_6.extend([section6_1, section6_2])

chapter6.append(sections_part_6)

# List for all the lists:

chapters = []
chapters.extend([chapter5, chapter6])

print "HTML for Lesson 5 - Table of content:"
print "-------------------------------------"
print make_toc_HTML(chapter5)
print
print "HTML for Lesson 6 - Table of content:"
print "-------------------------------------"
print make_toc_HTML(chapter6)
print
print "HTML for Lessons 5 and 6 - Full Text:"
print "------------------------------------"
print multiple_chapters(chapters)




