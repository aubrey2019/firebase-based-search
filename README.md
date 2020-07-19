# firebase-based-search

1 Project idea

The general idea of our project is to develop a web where user can do search by keyword(s) and make related queries navigated by the result.
There are two tasks for this project:
  1.Develop a Python program that imports the data from a MySQL database to a Firebase realtime database.
  2.Develop a Web browser based on user interface or mobile app that allows users to explore the content of a relational database stored in Firebase.

In order to the implement functions above, we have several steps to do: 
  1.Design the schema for the web
  2.Upload databases to Firebase
  3.Create inverted index for each word in every table
  4.Design a nested query function
  5.Convert back-end to front-end with achievement of visualization
  
  
  
  
2.Implementation details

   Run the local file app.py, it will show a site address.Copy it(here is http://127.0.0.1:5000/) to the browser.
 
   User can choose database and input keywords. For example, if we select world as our database and input keywords 'North America'(not case-sensitive here). It will return 75 records. And shown by tables. In country table’s result, records that contain 'North America' will ranking higher than the ones that only contain 'North' or 'America'.
 
   At the result page, there will be a hyperlink on the value if the it's a foreign key. User can explore different tables when clicking the hyperlink. For example, if the user clicks '3990', the web page will return 'city' table which contain '3990' as primary key.




3. Performance analysis on query processing & exploration process

  Since we have already uploaded the inverted index to firebase, the time complexity for searching one word is O(n).

  Assume that we have m words for the search query, the time complexity for searching the whole search query will be O(mn). The exploration process is just the same as the procedure above. However, at this time, m will be 1.
  
  The time complexity for exploration process is 0(n). The search will be very fast because we have uploaded the inverted index.
