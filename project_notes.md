# Starting Python Virtual Environment
**Install and create virtual environment (Windows)**
```bash
py -m pip install --upgrade pip
py -m pip install --user virtualenv
py -m venv env
```

**Then cd to directory with env file:**

**Activate env:**
```bash
.\env\Scripts\activate
```
**Deactivate env:**
```bash
deactivate
```

# PostgreSQL with aws
https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.PostgreSQL.html

# Dealing with user role setup on signup
* https://community.auth0.com/t/how-to-add-roles-permissions-to-a-user-during-signup/27006
* https://auth0.com/docs/authorization/concepts/sample-use-cases-rules


# Getting user_id from token
        owner_id = token.get('sub')

# README.md file info
* [Template](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [Basic writing and formatting syntax](https://help.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax)