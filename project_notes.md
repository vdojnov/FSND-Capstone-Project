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


# Getting user_id from token and user info
       
* how to get client_id

        client_id = token.get('sub'))
* SPLIT user_id so you can use_id to request info on the user in the http

        user_id = token.get('sub').split('|')
        print(user_id[0] +"%7C" + user_id[1])

* header with API MANAGEMENT TOKEN: ONE TIME TOKEN. authO_api_token IS TOKEN FROM API MANGEMNT IN AUTH0 (24h expirey)

        headers = { 'authorization': "Bearer " + authO_api_token }

* GET API URL TO GET USER INFO, get url form [here](https://auth0.com/docs/api/management/v2/) 

* [Special characters in http](https://secure.n-able.com/webhelp/NC_9-1-0_SO_en/Content/SA_docs/API_Level_Integration/API_Integration_URLEncoding.html)

        response = requests.get("https://ucsp.auth0.com/api/v2/users/" + user_id[0] +"%7C" + user_id[1] + "?include_fields=false", headers=headers)
* PRINTS USER INFO

        print(json.loads(response.content.decode('utf-8')))
        user_info = json.loads(response.content.decode('utf-8'))

* GET SPECIFIC INFO, IN THIS CASE EMAIL

        user_email = a.get('email')
        print(user_email)

<!-- 
# # how to get user_id
# print(token.get('sub'))
# #SPLIT user_id so you can use_id to request info on the user in the http
# user_id = token.get('sub').split('|')
# print(user_id[0] +"%7C" + user_id[1])
# #header with API MANAGEMENT TOKEN: ONE TIME TOKEN. GET TOKEN FROM API MANGEMNT IN AUTH0 (24h expirey)
# headers = { 'authorization': "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjlKcklIRHJsVWVZMmlmRlVZYmkxNCJ9.eyJpc3MiOiJodHRwczovL3Vjc3AuYXV0aDAuY29tLyIsInN1YiI6Imd2Y1NVbWNVMTdoMGZwVHdzaDNPRFpWMk1VcVJ4MldRQGNsaWVudHMiLCJhdWQiOiJodHRwczovL3Vjc3AuYXV0aDAuY29tL2FwaS92Mi8iLCJpYXQiOjE1ODgyMTcyMTksImV4cCI6MTU4ODMwMzYxOSwiYXpwIjoiZ3ZjU1VtY1UxN2gwZnBUd3NoM09EWlYyTVVxUngyV1EiLCJzY29wZSI6InJlYWQ6Y2xpZW50X2dyYW50cyBjcmVhdGU6Y2xpZW50X2dyYW50cyBkZWxldGU6Y2xpZW50X2dyYW50cyB1cGRhdGU6Y2xpZW50X2dyYW50cyByZWFkOnVzZXJzIHVwZGF0ZTp1c2VycyBkZWxldGU6dXNlcnMgY3JlYXRlOnVzZXJzIHJlYWQ6dXNlcnNfYXBwX21ldGFkYXRhIHVwZGF0ZTp1c2Vyc19hcHBfbWV0YWRhdGEgZGVsZXRlOnVzZXJzX2FwcF9tZXRhZGF0YSBjcmVhdGU6dXNlcnNfYXBwX21ldGFkYXRhIHJlYWQ6dXNlcl9jdXN0b21fYmxvY2tzIGNyZWF0ZTp1c2VyX2N1c3RvbV9ibG9ja3MgZGVsZXRlOnVzZXJfY3VzdG9tX2Jsb2NrcyBjcmVhdGU6dXNlcl90aWNrZXRzIHJlYWQ6Y2xpZW50cyB1cGRhdGU6Y2xpZW50cyBkZWxldGU6Y2xpZW50cyBjcmVhdGU6Y2xpZW50cyByZWFkOmNsaWVudF9rZXlzIHVwZGF0ZTpjbGllbnRfa2V5cyBkZWxldGU6Y2xpZW50X2tleXMgY3JlYXRlOmNsaWVudF9rZXlzIHJlYWQ6Y29ubmVjdGlvbnMgdXBkYXRlOmNvbm5lY3Rpb25zIGRlbGV0ZTpjb25uZWN0aW9ucyBjcmVhdGU6Y29ubmVjdGlvbnMgcmVhZDpyZXNvdXJjZV9zZXJ2ZXJzIHVwZGF0ZTpyZXNvdXJjZV9zZXJ2ZXJzIGRlbGV0ZTpyZXNvdXJjZV9zZXJ2ZXJzIGNyZWF0ZTpyZXNvdXJjZV9zZXJ2ZXJzIHJlYWQ6ZGV2aWNlX2NyZWRlbnRpYWxzIHVwZGF0ZTpkZXZpY2VfY3JlZGVudGlhbHMgZGVsZXRlOmRldmljZV9jcmVkZW50aWFscyBjcmVhdGU6ZGV2aWNlX2NyZWRlbnRpYWxzIHJlYWQ6cnVsZXMgdXBkYXRlOnJ1bGVzIGRlbGV0ZTpydWxlcyBjcmVhdGU6cnVsZXMgcmVhZDpydWxlc19jb25maWdzIHVwZGF0ZTpydWxlc19jb25maWdzIGRlbGV0ZTpydWxlc19jb25maWdzIHJlYWQ6aG9va3MgdXBkYXRlOmhvb2tzIGRlbGV0ZTpob29rcyBjcmVhdGU6aG9va3MgcmVhZDplbWFpbF9wcm92aWRlciB1cGRhdGU6ZW1haWxfcHJvdmlkZXIgZGVsZXRlOmVtYWlsX3Byb3ZpZGVyIGNyZWF0ZTplbWFpbF9wcm92aWRlciBibGFja2xpc3Q6dG9rZW5zIHJlYWQ6c3RhdHMgcmVhZDp0ZW5hbnRfc2V0dGluZ3MgdXBkYXRlOnRlbmFudF9zZXR0aW5ncyByZWFkOmxvZ3MgcmVhZDpzaGllbGRzIGNyZWF0ZTpzaGllbGRzIHVwZGF0ZTpzaGllbGRzIGRlbGV0ZTpzaGllbGRzIHJlYWQ6YW5vbWFseV9ibG9ja3MgZGVsZXRlOmFub21hbHlfYmxvY2tzIHVwZGF0ZTp0cmlnZ2VycyByZWFkOnRyaWdnZXJzIHJlYWQ6Z3JhbnRzIGRlbGV0ZTpncmFudHMgcmVhZDpndWFyZGlhbl9mYWN0b3JzIHVwZGF0ZTpndWFyZGlhbl9mYWN0b3JzIHJlYWQ6Z3VhcmRpYW5fZW5yb2xsbWVudHMgZGVsZXRlOmd1YXJkaWFuX2Vucm9sbG1lbnRzIGNyZWF0ZTpndWFyZGlhbl9lbnJvbGxtZW50X3RpY2tldHMgcmVhZDp1c2VyX2lkcF90b2tlbnMgY3JlYXRlOnBhc3N3b3Jkc19jaGVja2luZ19qb2IgZGVsZXRlOnBhc3N3b3Jkc19jaGVja2luZ19qb2IgcmVhZDpjdXN0b21fZG9tYWlucyBkZWxldGU6Y3VzdG9tX2RvbWFpbnMgY3JlYXRlOmN1c3RvbV9kb21haW5zIHVwZGF0ZTpjdXN0b21fZG9tYWlucyByZWFkOmVtYWlsX3RlbXBsYXRlcyBjcmVhdGU6ZW1haWxfdGVtcGxhdGVzIHVwZGF0ZTplbWFpbF90ZW1wbGF0ZXMgcmVhZDptZmFfcG9saWNpZXMgdXBkYXRlOm1mYV9wb2xpY2llcyByZWFkOnJvbGVzIGNyZWF0ZTpyb2xlcyBkZWxldGU6cm9sZXMgdXBkYXRlOnJvbGVzIHJlYWQ6cHJvbXB0cyB1cGRhdGU6cHJvbXB0cyByZWFkOmJyYW5kaW5nIHVwZGF0ZTpicmFuZGluZyByZWFkOmxvZ19zdHJlYW1zIGNyZWF0ZTpsb2dfc3RyZWFtcyBkZWxldGU6bG9nX3N0cmVhbXMgdXBkYXRlOmxvZ19zdHJlYW1zIGNyZWF0ZTpzaWduaW5nX2tleXMgcmVhZDpzaWduaW5nX2tleXMgdXBkYXRlOnNpZ25pbmdfa2V5cyIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyJ9.RPamETPqbpXe0oUhurqyYsfu_BWo4hXUb4132pFelKAmKCWFVX1_yn9lUrIKk1lMLESC-pYE1QDXybQ4xcDg6sbubkzWH2PqivrF0ptDeAOzczKqgNy-EQc19NOzVVHsfFU1IUM6VCTNINzUYL45u_h9V62qfD6k8I-zv2G569HhccGOMtlhtd1_RivG0OBiyFRyhzBcUlNcqey3u2Ke98okFwOUSRp6FrvP5X5H7WI3TLVyqm8ngt-vPMf2_IIqVRbTqaWzhZu47wORokMbr3Z3EYkVbpXmV9LSeTiqY2iW1sJG1hE2sg0_9DKbb3J9dGemLyGmH7xAooPm9EUT5g" }
# #GET API URL TO GET USER INFO, get url form: https://auth0.com/docs/api/management/v2/ 
# # special characters: https://secure.n-able.com/webhelp/NC_9-1-0_SO_en/Content/SA_docs/API_Level_Integration/API_Integration_URLEncoding.html
# response = requests.get("https://ucsp.auth0.com/api/v2/users/" + user_id[0] +"%7C" + user_id[1] + "?include_fields=false", headers=headers)
# #PRINTS USER INFO
# print(json.loads(response.content.decode('utf-8')))
# a = json.loads(response.content.decode('utf-8'))
# #GET SPECIFIC INFO, IN THIS CASE EMAIL
# one = a.get('email')
# print(one) -->

# README.md file info
* [Template](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [Basic writing and formatting syntax](https://help.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax)

# Make copy of postgres database

```bash
createdb -O ownername -T originaldb newdb
```
