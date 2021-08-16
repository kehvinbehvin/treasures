API ENDPOINTS

# 👦🏻 User

## <strong>POST</strong> {URL}/user/login

<br>

## <strong>User Login</strong>

| field    | data_type | required | unique |     |
| -------- | --------- | -------- | ------ | --- |
| username | String    | true     | true   |     |
| password | String    | true     | -      |

- Login User

Return Values:

1. If successful, will return 2 tokens, keys: access,refresh
2. If unsuccessful, will return error status = 401 unauthorised

## <strong>POST</strong> {URL}/user/signup

<br>

## <strong>User Creation</strong>

| field    | data_type | required | unique |     |
| -------- | --------- | -------- | ------ | --- |
| username | String    | true     | true   |
| password | String    | true     | -      |
| email    | String    | true     | true   |

<br>

- Add new user

Return Values:

1. If successful (Status = 201 Created)
2. If unsuccesful
   1. Because of duplicate username/email --> (Status = 500 Internal Server Error), Exception Value = Duplicate Key Value
   2. Because of empty fields --> (error message: "username, password and email is required to register a user")

# 🍿 Tweets

## <strong>GET</strong> {URL}/tweets

- View all tweets by all users

<br>

<details>

<summary>Example</summary>

```json
[
  {
    "model": "direct_message.direct",
    "pk": 1,
    "fields": {
      "sender": 1,
      "recipient": 2,
      "dm": "hello"
    }
  },
  {
    "model": "direct_message.direct",
    "pk": 2,
    "fields": {
      "sender": 1,
      "recipient": 3,
      "dm": "hello"
    }
  }
]
```

</details>

<br>

## <strong>GET</strong> {URL}/tweets/{:tweetid}
- Get one tweet by ID

<br>

<details>

<summary>Example</summary>

```json
{
"id": 3,
"author": 1,
"message": "hello world",
"date": "2021-08-12T08:35:54.539501Z"
}
```

</details>

<br>


## <strong>DELETE</strong> {URL}/tweets/{:tweet_id}
- Delete a tweet



## <strong>POST</strong> {URL}/tweets

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

TREASURES
Treasure view all
URL: /treasures
Method: GET
Description: View all the treasures existing in the app
Return Values: Array of Objects, Fields: author,name, description, longitude, latitude, date, hunters(array)

Treasure Create new
URL: /treasures
Method: POST
Body: {
"author": user_id,
"name": treasure_name,
"description": treasure_description,
"longitude": Integer,
"latitude": Integer,
"date": date,
"hunters": "",
}
Description: User creates a new treasure for a hunt so there are no hunters to add yet, will explore images
in the future
Return Values: Treasure object

Treasure view one
URL: /treasure/<:treasure_name>
Method: GET
Description: Find a treasure by its name
Return Values: Treasure Object

Treasure add hunter
URL: /treasure/<:treasure_name>
Method: PUT
Body:{
"author": author_id,
"name": treasure_name,
"hunter": hunter_id,
}
Description: Add the user as a hunter to a existing treasure
Return Value: Treasure Object
