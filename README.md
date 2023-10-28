# prismtech_test
Django project

Tools:
- Docker Desktop
- Postman

I. Setup
1. Change SOURCEROOT in /prism_docker/.env to path of folder prism_source.
2. Open Docker Desktop, open terminal and run "docker network create prismnetwork".
3. Open file hosts and add hosts:
	127.0.0.1 prismdb
	127.0.0.1 prism-test.me
4. cd to folder prism_docker. run "docker compose up -d"
	
II. Test
1. Open Postman, import collection from file Prism.postman_collection.json
2. Send request to test API.
Except for auth-register and auth-login, All of the requests need authorization to work correctly.
	- Send auth-login and copy the access token in the response
	- Click Prism collection, choose tag Authorization
	- Choose Type is Bearer Token
	- Paste access token to Token label
