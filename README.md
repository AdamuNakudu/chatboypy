# chatboypy

Resolver Bot is a simple flask web app bot that instantly responds to your questions, with a built in database of questions and answers gathered over the course of a few days. The bot can also includes a trainer that can be used by anyone, although perhaps there should be a developer lock on it. This project utilises flask, html + css and some javascript language.
vid url:

app.py + knowledge_base.json

1. Make file for the flask application ending in .py, a folder for the html template, a folder for the css design, and a JSON file for the data on questions and answers.
2. First thing I did was import flask, render_template, request and jsonify as these are the libraries I knew I would need, although more were added as I discovered new ways to do things.
3. The flask web app is then initialised with app = Flask(**name**), as well as the static root file being established as discovered much later on.
4. The functions to load and save the JSON knowledge base file were then defined
5. Then the function find_best_match was defined with the cutoff being the level of accuracy the program will have in identifying the correct response for speciifc user inputs.
6. The get_answer function does exactly that, the answer is given and if the answer is a list, a random one is selected, hence the need to import random. Otherwise, the only available answer is given.
7. The flask route is then identified, directing us to the actual webpage being chat1.html
8. The app route '/ask' handles the users input, finds the best match from the JSON database, and then returns an answer. I also include the 'quit' option here, although it does not actually lead to the end of the program. If there is no match in the database, the bot returns that they do not have the answer. This gives an opportunity for the bot to be trained, in another text box.

chat1.html + style.css

1. Basic template for html is written first, starting with !DOCTYPE html, head, body, etc.
2. CSS file is linked. A bug occured here: CSS file was showing up in IDE preview but not on client side. Solution was to create a static folder for the CSS file and server configuration. In flask, you do this with url_for function to generate correct URLS for static files in href (hyptertext reference). I also created another <!link> in html so preview can be shown in ide. Static also needs to be configured in the app.py file so that the program assumes static files are located in a folder named 'static' at the root level.
3. The body is filled with basic design that allows user to input in a textbox, click a button and get a reply from the bot.
4. Second button and textbox is also included to make training easier.
5. The script section fetches the flask routes /ask and /train.

!TO IMPROVE:

- Allow for similar questions to give you the same answers. Eg: greetings:greetings
- Keywords should also trigger the same answer.
- One text box to seemlessly train the bot, as opposed to a seperate box.
