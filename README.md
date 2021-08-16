API ENDPOINTS

USER LOGIN/REGISTRATION

User Login
URL: /user/login
Method: POST
Header: {
Authorization: Bearer <jwt access token>
}
Body: {
username: : String  
password: : String
}
Description: Login User
Return Values:

User SignUp
URL: /user/signup
Method: POST
Body: {
username: : String
password: : String
}
Description: Sign Up User
Return Values:

TWEETS

Tweets View All
URL: /tweets
Method: GET
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
