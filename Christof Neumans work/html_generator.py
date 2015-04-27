# this first function provides the outline text for the final HTML, now we have to 
# get the right values for concept_title and concept_description
def generate_concept_HTML(concept_title, concept_description): 
	html_text_1 = '''
<div class="concept">
	<div class="concept_title">
		''' + concept_title 
	html_text_2 = '''
    </div
    <div class="concept_description">
    	<p>
    	''' + concept_description
	html_text_3 = '''
    	</p>
    </div>
</div> '''
	full_html_text = html_text_1 + html_text_2 + html_text_3
	return full_html_text

def make_HTML(concept): # takes a list as its input
	concept_title = concept[0] # next two lines return the title and description in nested list
	concept_description = concept[1]
	return generate_concept_HTML(concept_title, concept_description) 
	#returns the HTML text from above in, when applied to the list found here** 
	# however its only one list item...

Example_list_of_concepts = [['python', 'Python is a programming language'],
						['HTML', ' Stands for HyperText Markup Language']]

def make_html_for_many_concepts(list_of_concepts):
	HTML = ""
	for concept in list_of_concepts:
		concept_HTML = make_HTML(concept)
		HTML = HTML + concept_HTML
	return HTML

print make_html_for_many_concepts(Example_list_of_concepts)
