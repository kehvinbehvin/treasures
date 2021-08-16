API ENDPOINTS

USER LOGIN/REGISTRATION

User Login
URL: /user/login
Method: POST
Body: {
username: : String  
password: : String
}
Description: Login User
Return Values:

1. If successful, will return 2 tokens, keys: access,refresh
2. If unsuccessful, will return error status = 401 unauthorised

User SignUp
URL: /user/signup
Method: POST
Body: {
username: : String
password: : String
}
Description: Sign Up User
Return Values:

1. If successful (Status = 201 Created)
2. If unsuccesful
   1. Because of duplicate username/email --> (Status = 500 Internal Server Error), Exception Value = Duplicate Key Value
   2. Because of empty fields --> (error message: "username, password and email is required to register a user")

TWEETS

Tweets View All
URL: /tweets
Method: GET
Header: {
Authorization: Bearer <jwt access token>
}
Description: View all tweets by all users
Return Values:

Tweets Delete 1
URL: /tweets/:tweetid
Method: DELETE
Description: Delete one tweet
Return Values:

Tweets Find 1
URL: /tweets/:tweetid
Method: GET
Description: Find one tweet
Return Values:

Tweets Post 1
URL: /tweets
Method: POST
Body: {
message: String
}
Description: Post a tweet
Return Values:

DIRECT MESSAGES
DMs - Get conversation between you and your friend
URL: /messages/:userid/:friendid
Method: GET
Description: Retrieve all messages between you and your friend
Return Values:

DMs - Send a message to your friend
URL: /messages
Method: POST
Body: {
sender: :id
recipient: :id
}
Description: Send a message to your friend
Return Values:
