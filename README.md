Python program to brute force password via blind SQL injection. The username is known to be "natas16" and the password is an alphanumeric string with a length of 32 characters.

Script was written for the online web security challenge: https://overthewire.org/wargames/natas/natas15.html

## The vulnerability: 
Unsanitized inputs allows the user to perform SQL queries through the input form. There are 2 tables, 'username' and 'password.' If the SQL query returns a result the webpage will output the following text, "This user exists."

## The exploit:
Can use the BINARY LIKE comparative operator to determine which alphanumeric characters are contained in the password. The username is known to be "natas16" so the injected SQL query looks like this: **username=natas16" AND "password LIKE BINARY %[char]%**
The program iterates over every alphanumeric character in the [char] variable.

When the website indicates that the query returned a result, the current iteration of [char] is added to a list called bf_chars (brute force characters)

Now we can brute force by iterating over the bf_chars list, rather than all alphanumeric characters. This is made simple because each character can be brute forced independently by using the following SQL query: **username=natas16" AND "password LIKE BINARY [current_pw]%**

The current_pw variable is a string that iterates over the characters stored in list bf_chars. When a match is found, the letter is appended to the end of string current_pw. Exploiting this SQL injection vulnerability we can brute force the password for user "natas16" one character at a time.
