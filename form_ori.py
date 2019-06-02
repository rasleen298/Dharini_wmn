<!DOCTYPE html>
<html>

   <head>
      <title>Text Input Control</title>
   </head>
	
   <body>
      <form >
         First name: <input type = "text" name = "first_name" />
         <br>
         Last name: <input type = "text" name = "last_name" />
      </form>
	
	<form action="http://localhost:5000/signup" method="post">
	 Description : <br />
         <textarea rows = "5" cols = "50" name = "description">
            Enter description here...
         </textarea>
         <input type = "submit" name = "submit" value = "Submit" />
      </form>
	<form>
         <input type = "reset" name = "reset"  value = "Reset" />
         
         <input type = "image" name = "imagebutton" src = "img.jpg" />
      </form>
   </body>
	
</html>
