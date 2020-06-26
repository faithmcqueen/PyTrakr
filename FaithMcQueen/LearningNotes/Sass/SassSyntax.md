#Sass - Syntax
- Sass removes all curly braces and semicolons from your CSS syntax
- Scss uses curly braces and semicolons - the only difference from regular CSS is the use of variables/inheritance
- Your selector sits like normal, left justified on your stylesheet
- Where you would normally place a { to begin styling, you instead hit enter, and your style is indented underneath
- When you do this, you can also nest your styles

###Nesting
- Instead of having many selectors (example: ul {style}, ul li {style}, li a {style}, etc) you can nest your styles underneath one another
- By nesting li UNDER the ul styles, you carry all of that styling to the li and then you can add your additional styling
- This will compile and output to CSS using the selectors that CSS needs without you having to manually type it
- Another example: if you have selected a class (i.e. "container") and you want to select a div inside the container, you would not need to type out .container div - instead, style .container, and then hit enter and type div - then, hit enter again, and hit tab to indent and you are styling .container div
- This creates visual hierarchies for your CSS and helps you visualize how selectors are related to one another, and keeps your styling efficient
- NOTE: overly nested SASS will result in over-qualified CSS -- this is hard to maintain, and bad practice. Use this only when necessary, don't rely too heavily on nesting

###Sass Variables
- a way to store information you want to reuse throughout the stylesheet
- Example -- SASS Syntax:
~~~
$fontstack: Helvetica, sans serif
$primary-color: #333
body
    font-family: $fontstack
    color: $primary-colour
 ~~~      
###Mixins
- mixins lets you make groups of code you will reuse to make it more efficient and less tedious to type out
- to declare, you type @mixin and a name - this will be called later in your sass sheet when you need it, using @include [name]
- EXAMPLE: 
~~~
@mixin transform ($property)
    -webkit-transform: $property
    -ms-transform: $property
    transform: $property

.box
    @include transform(30deg)
~~~ 
###Extend/Inheritance
- Extending uses @extend to call declared sass
- This lets you share CSS properties from one selector to another
- This is key to keeping Sass dry, and efficient
- Uses placeholder class - a special class that ONLY points when it is extended, so it keeps things neat and clean when compiled
- If you never extend the Sass, it will *not* output to CSS
- placeholder class is declared with a % -- %message-shared
- you call it through the @extend function -- @extend %message-shared

###Operators
- can use +, -, *, /, and %
- this allows you to do math in CSS, for things like creating percentages for widths of columns

###Partials
- You can create partial Sass files that contain snippets of CSS, to be included in other Sass files
- Partial Sass files start with underscore: _partial.scss
- This lets Sass know not to compile it - only when @use is used in another stylsheet does it know to call that sheet

###Modules
- modules work with the @use rule, linking partial files (no extensions needed)


####Sources:
    - https://sass-lang.com/
    - https://skl.sh/2VeYa1N (SkillShare Sass project)
    - https://www.youtube.com/watch?v=_a5j7KoflTs