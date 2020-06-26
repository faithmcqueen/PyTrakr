#Sass - Setting Up
##Setting up Sass on your machine
- Need to install Sass onto your computer
- Can do this through the command line using npm or homebrew:
-- brew install sass/sass/sass
- Sass can be written using .sass or .scss -- there are syntax changes (see Syntax below)

## How do we use it?
- Once Sass file is complete, compile it to CSS through cmd terminal
- Use commands: sass style.sass:style.css
- This turns Sass or Scss files into regular CSS
- If you only run this command you need to run it every time you make a change
- To set up a listener so this works automatically for you, use the following command:
- sass --watch syle.sass:style.css
- this sets up a listener to auto compile into CSS anytime you mae a change

##Benefits of Sass
- Sass helps keep your code more dry, clear, and efficient
Stylesheets can be long and complex, and Sass allows for: nesting, mixins, extending, inheritance, etc
- You can store commonly reused code in variables, to make it more efficient when styling
- This is most helpful when you are making changes -- for example, if your brand colour changes, you only need to change it in one place
- Having code that is reused held in variables also helps to ensure brand standards are kept, and that a website has a uniform look


####Sources:
    - https://sass-lang.com/
    - https://www.youtube.com/watch?v=Rnxyf6Vyqiw

