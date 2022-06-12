from browser import document, html
    
container = document["container"]
todo_list = html.H1("My todo list")
container <=todo_list

items = ['Go to school', 'Practice Piano', 'Go to restaurant']

for item in items:
    container <=html.LI(item)
