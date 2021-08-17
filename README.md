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

## <strong>GET</strong> {URL}/tweets/

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

## <strong>POST</strong> {URL}/tweets/

- Post a new tweet

| field   | data_type | required | unique |     |
| ------- | --------- | -------- | ------ | --- |
| author  | user_id   | true     | true   |
| message | String    | true     | -      |
| date    | String    | true     | true   |

## <strong>DELETE</strong> {URL}/tweets/{:tweet_id}

- Delete a tweet

<br>

# 🍉 Direct Messages

## <strong>GET</strong> {URL}/messages/{:userid}/{:friendid}

- Get conversation between you and your friend

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
  }
]
```

</details>

<br>

## <strong>POST</strong> {URL}/messages/

- Send a message to your friend

| field     | data_type    | required | unique |     |
| --------- | ------------ | -------- | ------ | --- |
| sender    | sender_id    | true     | true   |
| recipient | recipient_id | true     | true   |
| dm        | String       | true     | true   |

<br>

# 🍺 Treasures

## <strong>GET</strong> {URL}/treasures/

- View all the treasures

<details>

<summary>Example</summary>

```json
[
  {
    "author": 1,
    "name": "BIGGEST TREASURE OF ALL",
    "description": "gold bars, rolex, bentley",
    "longitude": "1.356070000000000",
    "latitude": "103.954230000000000",
    "date": "2021-08-16T13:51:52.318530Z",
    "hunters": [2]
  }
]
```

</details>

<br>

## <strong>GET</strong> {URL}/treasures/{:treasure_name}

- Get one treasure via name

## <strong>POST</strong> {URL}/treasures/

- Post a new treasure

| field       | data_type | required | unique |     |
| ----------- | --------- | -------- | ------ | --- |
| author      | admin_id  | -        | -      |
| name        | String    | -        | -      |     |
| description | String    | true     | -      |
| longitude   | Integer   | true     | -      |
| latitude    | Integer   | true     | -      |     |
| date        | String    | true     | -      |
| hunters     | Array     | false    | -      |     |

## <strong>PUT</strong> {URL}/treasures/{:treasure_name}

- Add hunters to the treasure object

| field  | data_type     | required | unique |     |
| ------ | ------------- | -------- | ------ | --- |
| author | user_id       | true     | true   |
| name   | treasure_name | true     | -      |
| hunter | hunter_id     | true     | true   |

<br>

# 📖 Profile

## <strong>GET</strong> {URL}/profile/

- Get all the profiles

## <strong>POST/PUT</strong> {URL}/profile/{user_id}

- Create/Edit user profile

| field    | data_type        | required | unique |     |
| -------- | ---------------- | -------- | ------ | --- |
| user_id  | user_id          | -        | -      |
| nickname | String           | -        | -      |     |
| address  | String           | -        | -      |
| age      | Integer          | -        | -      |
| about_me | String           | -        | -      |     |
| friends  | Array[friend_id] | -        | -      |

## New Stuff to add

1. Changed the URL for direct messages --> For finding messages between user and friend
2. Changed the return value for user_profiles, now, the friends id's are populated with the friend's username
3. Added new API endpoint for treasures --> treasures/participated-> returns all the treasures that the user
   participated in.
4. Added Likes to Tweets and also added new endpoint for liking tweets.

## Add in JWT

1. How to refresh JWT Token
