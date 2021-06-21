# Application Process

# Step 1 - MySQL Database
I installed MySQL and proceeded to created a database and script two tables. The first table is the User table which captures the First Name, Last Name and Date of Birth of the User.
The second table captures the financial data of the user. 

# Step 2 - HTML
 
In my solution there are two html files. The home.html file sets up the home page where a user inputs their First Name, Last Name and Date of Birth.
The index.html file is where the user will upload their financial data.

# Step 3 - Python

 ## db_connection.py 

  In this python file a connection is made to the database. Usually I would store any credentials in an Azure Key Vault and reference this in my code for security reasons. 
  Here I wrote a function that inserts the data into the User table. The auto-increment setting in the database was giving issues so I improvised and generated random numbers for   the UserId. This is not best practice as eventually the database will fail. 
  
 ## read_files.py
 
 In this python file a connection is made to the database as well. To ensure a the connection is succesful I list the names of all the databases. I then wrote a function that  parses the excel file and then using a for loop I inserted each row into thedatabase. 
 
 ## main.py
 
 This python file ties everything together. Before I reference any functions I first render the html files. 
 
 
 # Improvements
 1. The User should input all information on a single web page. In my design I did not account for that. The main issue with this would be created a relationship between the two tables. 
 2. Saving any credentials in a secure manner. 
 3. Ensuring the data types are correct. This includes enabling an auto generated ID column for both tables.  
  



