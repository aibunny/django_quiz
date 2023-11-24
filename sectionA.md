# SECTION A


Better view of the questions can be found here: [**Notion**](https://nickel-throne-d4a.notion.site/SECTION-A-51bb1d5c89874195ba2089711744e715)
1. **Give examples of different integration protocols you have come across and give example scripts in python 3 on how to achieve each one. (10 pts)**
		
	In my 4 year experience working as A django and drf developer I have come across multiple integration protocols which varied depending on the applications I was connecting to and the project rquirements I am mostly conversant with:
	
	**a. REST (Representational State Transfer)**  APIs which uses (HTTP/HTTPS)
	
	REST is used where data does not change oftenly and simple interactions are needed such as CRUD operations for databases
	
	 For  REST API in python we use the requests library that supports different request methods such POST, PUT, GET, DELETE and PATCH
	
	```
	import requests
	
	url = "http://api.interintel.com/resource"
	
	#This is an exaple of a get request
	response = requests.get(url)
	data = response.json()
	
	```
	
	**b. GraphQl**
	
	This is a query language for APIs and is mostly used when dealing with complex data structures with multiple inheritance and the clients wants to fetch exactly what they need without under fetching or over-fetching of data. This protocol is faster compared to REST and in django there is a library we use graphene_django which I talk more about in 
	
	```
	import requests
	#url
	url = "http://api.interintel.com/graphql/resource"
	query = """
	{
		resource {
			field1
			field2
		}
	}
	"""
	response = requests.post(url, json={'query': query})
	data = response.json()
	
	```
	
	**c. Websockets**
	
	websockets provide long lived bidirectional communication over a sinlge long lived connection they are suitable for chat appllications, live notifications and collaborative editing such as in live share on vscode which I find fancy. 
	
	```
	#Websocket connection
	
	#use python websocket library
	import websocket
	
	ws = websocket.WebSocket()
	ws.connect("ws://example.com/websocket")
	result = ws.recv()
	ws.close()
	```
	
	I have blogs for the above 3 protocols which can atest to my skills:
	
	Request at [**medium**](https://medium.com/me/stories/public)
	
	GraphQL at [**Power of GaphQ With Graphene Django**](https://medium.com/@aibunny/unleashing-the-power-of-graphql-with-django-and-graphene-a-deep-dive-945199929861) 
	
	Websockets at [**Building a streaming app with django**](https://blog.theaibunny.com/building-a-streaming-app-with-django/)



2. **Give a walkthrough of how you will manage a data streaming application sending one million notifications every hour while giving examples of technologies and configurations you will use to manage load and asynchronous services. (10 pts)**
    
	Managing data streaming application would require a delicate approach since we want our applicaion to respond in time and carry only as much load as it can withstand and we can monitor its behavior and downtime so we can respond it time with the right measures.
	
	To manage this particular use caseof 1 million notifications every hour I would set up a well organized backend, to handle each notification efficiently I’d use a message queue system using tools like RabbitMQ or Apache Kafka. To ensure the sever works without being over burdened by tasks and requests, I would use automated load balancers like ELS(elastic load balancers by AWS) and also have auto scaling policies that specify when to add or remove instances depending on predefined threshhold like if CPU usage excedes 70% the scaling could be vertical or horizontal but I’d prefer to have it horizontal to avoit SPOF(single point of failure).
	
	To make sure that the tasks are sent out without delays I’d hire a team of helpers, which are like asynchronous services, Celery a task queue system would be perfect for this and it would require a message broker such as Redis or RabbitMQ. I’d also monitor celery using Flower. 
	
	To maintain the hourly schedule autonomously I’d set up cron jobs or schedulers like APScheduler that would act as reminders for the system triggering the reponse at precise intervals.
	
	lastly for monitoring and keeping an eye on things, i’d implement logging and use monitoring tools like grafana and prometheus which will give us more insights on how the system is performing.
	
	I have a blog on asynchronous task at **[Streamlining Business Verification with Smile ID and Django REST: A Celery-Powered Solution](https://medium.com/@aibunny/streamlining-business-verification-with-smile-id-and-django-rest-a-celery-powered-solution-340bdc96d998)**


    	
3. **Give examples of different encryption/hashing methods you have come across (one way and two way) and give example scripts in python 3 on how to achieve
    each one. (20 pts)**
        
   The One way algorithm  or an asymmetric algorithmis algorithm whose output can not be reversed once encrpted 		an example I have come across is the Message Digest Algorithm 5 (MD5) and    SHA-256 .
        
    a.MD5
   	It produces a 128-bit hash making it fast compared to SHA-256 but vulnerable to collisions, making it insecure
        Python example:
        
        ```
        #The MD5 example
        import hashlib
        
        def hash_using_md5(input_text:str)->str:
        	md5 = hashlib.md5()
        	md5.update(input_text.encode("utf-8"))
        	hashed_string = md5.hexdigest()
        	return hashed_string
        
        #example 
        md5_hash = hash_using_md5("Hello InterIntel")
        print(f"MD5 HASH: {md5_hash} \n")
        
        #Example output: 
        #MD5 HASH: a59e0f1e7cd9b57642e099e2335857bc
        ```
	b. SHA-256
	It produces a more secure 256-bit hash which is slower compared to MD5 but more secure, commonly used in cryptographic applications for data integrity and security.
	        
	        ```
	        #The SHA-256 example
	        
	        import hashlib
	        
	        def hash_using_sha256(input_text:str)->str:
	            sha256 = hashlib.sha256()
	            sha256.update(input_text.encode("utf-8"))
	            hashed_string= sha256.hexdigest()
	            return hashed_string
	        
	        # Example
	        sha256_hash = hash_using_sha256("Hello InterIntel")
	        print(f"SHA-256 HASH: {sha256_hash} \n")
	        
	        #EXAMPLE OUTPUT
	        #SHA-256 HASH: 7254eec5f35c022df4f5fb94b7288c6c5485eec519f57945e9376f179b720f7a
	        ```
	        
	The two way algorithms I have come across are the RSA and Fernet this algorithms output can be reversed once encrypted but with some few differences.
	        
	a.) Fernet
	  Its a symmetric encryption algorithm that ensures secure communication by using a shared secret key for both encryption and decryption 
	        
	  Python Example:
	        
	        ```
	        #TODO: Run pip install cryptography
	        
	        from cryptography.fernet import Fernet
	        
	        def hash_decrypt_using_fernet(input_text:str, key:str) -> str:
	            ##fernet uses an encrption key to 
	            #encrypt so i passed it in as a parameter
	            cipher = Fernet(key)
	            hashed_string = cipher.encrypt(input_text.encode('utf-8'))
	            decrypted_string = cipher.decrypt(hashed_string).decode('utf-8')
	            return hashed_string, decrypted_string
	        
	        # generate encrption key to use
	        key = Fernet.generate_key()
	        message = "Hello InterIntel"
	        
	        hashed_string, decrypted_string = hash_decrypt_using_fernet(message, key)
	        print("hashed_string:", hashed_string)
	        print("decrypted_string :", decrypted_string)
	        
	        #EXAMPLE OUTPUT
	        #KEY b'5Fhx9by0MILjCMZqMTsJct-_9bf90nQNkxx6_AaTDj0='
	        #FERNET HASH: b'gAAAAABlX5bWyeqh9oYhaUc1t6CKJsV5bnc-abkrm8UHnnZdBa4u9ChAbQfsqn-P8YMUARrxMFBh2MDu_TRAdgNTX_UozvkBKN955o1364O64rOR4hJ-DSA='
	        #decrypted_string : Hello InterIntel
	        ```
	        
	b. RSA
	It uses a pair of keys  a public key for encryption and a private key for decryption. It's known as 		asymmetric encryption.
	        
	Python Example:
	        
	        ```
	        from cryptography.hazmat.primitives import serialization,hashes
	        from cryptography.hazmat.primitives.asymmetric import rsa, padding
	        
	        def encrypt_decrypt_rsa(input_string: str) -> tuple[str, str]:
	            # Generate private and public keys
	            private_key = rsa.generate_private_key(
	                public_exponent=65537,
	                key_size=2048
	            )
	        
	            public_key = private_key.public_key()
	            
	            # Serialize private key to PEM format
	            private_key_pem = private_key.private_bytes(
	                encoding=serialization.Encoding.PEM,
	                format=serialization.PrivateFormat.PKCS8,
	                encryption_algorithm=serialization.NoEncryption()
	            ).decode('utf-8')
	        
	            # Serialize public key to PEM format
	            public_key_pem = public_key.public_bytes(
	                encoding=serialization.Encoding.PEM,
	                format=serialization.PublicFormat.SubjectPublicKeyInfo
	            ).decode('utf-8')
	        
	            print(f"Private Key (PEM format):\n{private_key_pem}")
	            print(f"Public Key (PEM format):\n{public_key_pem}")
	        
	            # Encrypt using the public key
	            hash_algorithm = hashes.SHA256()
	            mgf = padding.MGF1(algorithm=hash_algorithm)
	            hashed_string = public_key.encrypt(
	                input_string.encode('utf-8'),
	                padding.OAEP(
	                    mgf=mgf,
	                    algorithm=hash_algorithm,
	                    label=None
	                )
	            )
	        
	            # Decrypt using the private key
	            decrypted_string = private_key.decrypt(
	                hashed_string,
	                padding.OAEP(
	                    mgf=mgf,
	                    algorithm=hash_algorithm,
	                    label=None
	                )
	            ).decode('utf-8')
	        
	            return hashed_string, decrypted_string
	        
	        # Example
	        message = "Hello InterIntel"
	        
	        rsa_hash, rsa_decrypted_string = encrypt_decrypt_rsa(message)
	        print("RSA HASH:", rsa_hash)
	        print("RSA decrypted string:", rsa_decrypted_string)
	        #EXAMPLE OUTPUT
	        """Private Key (PEM format):
	        -----BEGIN PRIVATE KEY-----
	        MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDaRG3KhO8KjSbe
	        v13LPEnKxYUJSHBfwJoiVsnB/PfRh+Q1W5qXKKumtapcLIpyXtFTao6B6D4/h7gw
	        bapHAnzt75CoGrzPefYbFECsIFJzVtxIKK22LoFXAhlhzaqJLGLkmE3R0leEFHid
	        S8PkCURu6NijCkaTd1rPA9I3tkpCqywnOQRjZQ8bA2jFRkkYmyBt5zpGJrp5u103
	        ks2klgecEK5qlFYnzutPyTC6PAlAcURd383/agfPcrFSTSGIdH7EfhokrDA/aRUR
	        b+dbe0CD3OVSz5EZ11xB8ajrJEI2M/5ri1M8zaJ88gPCoz1EmlE6gKoB8WdYWb0u
	        4Rc49p9/AgMBAAECggEALz7krRO9UoFfSpQNz3JLXtMGiw3dFTzxoEE9BvqlAfvy
	        UAJ2IgYxsbJdH/qcNUmE8hN8qW4GG2ZbXlA+rYRCWpair2CqQhbaSN5HaXrNnh3N
	        LOlxQKAsaxMPP3ZvVaX/+g9luOdY/kQYH6RI0NGYuJE6Y4BT6pPJWkovdNPGm0tf
	        pvY6/JiDETcAYfE/ghFxApUAqPWal9PLcykSAstDw0evk8BxVgj2ZLm7Y62TgBh3
	        iX6bL9Mp1OryuZ1j53tlC3pjOm+WbkmiqtgVW01GxrbdwYFR+CxY7nIYojLSC9SH
	        97YJTsATUH8T7BhrM1cvufIxupkAzhh5XUgwxmQ4wQKBgQD18eNqmz3WsnlYM8fr
	        ME4W9BR59u0A8+2Tqk3FGMribb0s4VfhbJD/9Q0yv5AX8GSl4NsplrVaKyteInLF
	        nhAn4m7d3vs3S8vJwO4uE0IAkIB2KohRyDfub5+4xKfjpqWQ5oPnIl0de+HOOYUd
	        0WmLXVb4qqZkWDQD9NWEqsOxEQKBgQDjMNxw6S+1QVedj/wDQcFzOYsWGcTCRGX2
	        wf2WGd1KF9nTHS00n6BMVsxNt4Xz4ZKQFp9tnRrcV9uiEt57cbaVV6hAn97LJzmE
	        1hsApZ47zNuBYIa01+EGL/XGo6mWkE3Kc7RttpWVtFMm7u1EYFfzERCBpjZ8d1X8
	        +cYFtttHjwKBgEJDNmtNgh6rHShXYyCJdjCW+EFX9sjP741eT++vW1IgENzbpaq1
	        bmeXpUOr+u2INgW/DC0rTpcJlHibPWLi0CV+yzH51qMyR6iG02UUiS7Pv9yWXv3x
	        vKf/6P+F9FnQV0Ev6g/G4WGFM/Q06Rl8hzwmHL2IdKYKYZFDUJeazniRAoGBAJjl
	        BCW0uNepvtYZ1Uc31IHAAxt/ggwfTeOP0CJZC7TWclCCfS7CEnXtoBbZYHutnh38
	        K5TwOuh49CWRv0qiT3cYA/Jh5OUhY7NDB+8ahm/GQR9Dn8RK2HR6iFQDRpk+Sivq
	        TE3dp7OVJLS57NGsaOP64vntqxN+mE7kpWCpG89/AoGAM//8+BpwTcyRiJi3mEN2
	        QKbEBYZTijUVeISjoBhUSPzbVxTcScg+3wayvsAkSYlxHADLwxfu0Zo5Lew477i2
	        ZKIzBunRIC751RJVmAH3tU/HLiwfnorAAl/TqfUzvwS71djepubuu3xEI20KC8uA
	        CkG19klJ3SfXXX5WZEfLX98=
	        -----END PRIVATE KEY-----
	        
	        Public Key (PEM format):
	        -----BEGIN PUBLIC KEY-----
	        MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA2kRtyoTvCo0m3r9dyzxJ
	        ysWFCUhwX8CaIlbJwfz30YfkNVualyirprWqXCyKcl7RU2qOgeg+P4e4MG2qRwJ8
	        7e+QqBq8z3n2GxRArCBSc1bcSCitti6BVwIZYc2qiSxi5JhN0dJXhBR4nUvD5AlE
	        bujYowpGk3dazwPSN7ZKQqssJzkEY2UPGwNoxUZJGJsgbec6Ria6ebtdN5LNpJYH
	        nBCuapRWJ87rT8kwujwJQHFEXd/N/2oHz3KxUk0hiHR+xH4aJKwwP2kVEW/nW3tA
	        g9zlUs+RGddcQfGo6yRCNjP+a4tTPM2ifPIDwqM9RJpROoCqAfFnWFm9LuEXOPaf
	        fwIDAQAB
	        -----END PUBLIC KEY-----
	        
	        RSA HASH: b'\xcd`\xe9\xcde0\xa8H\x90&P\xb0\xa6\t\xebj\xbdoJO\xe49|9\x16\xdfVO\xc3\x90\x87F\x88G\xd4\x8d\x0b~\xbc\xa2%\xabGx\x10\xfc\x90\xcdv\x10\xac\x8a\x1dP\x9a\xd2\xbd\x82`3\xc1\x7f\x8b\x1c\xc6\xb6gc$\x13\xf7M$\x0e\t9\xb1\x99\xd1A\x96\x00\xd5hqq\x1b\xc1>\x98=(\x9b\xfcTa\xd2\x14\x87\xa2|R\x13\xb6\xd6,\xf8\x8a\xb1ijt4R\xc4=\nu\x83Pw\xba\xb9W\xf2+E\xa9\xf8zE\x94\xd8\xee\x89\xafCk\x88>N?\xa9?\xb2\x1c\\\xc7V\x0c\x81\x98\xfc4%\xb9\xd2\xc8\xf2h\xcc\xcf\x82\xaa\xa3v\x08*\x87\x18\xef\xceC\xe4d\x19\x08\xd0\x88b\x9c\x0f\xa5\x831\x95\xc4~Gb\xb7\xa0{\xc0\x95S\x91\xbf\x8d`\xc1L\xf9\x8aa\x84\xbe\x85\xbc&!@\xdbkbm\xeeV\x18.\xea\xbcwI\xa1\xd6e\xc2>$r\xa3\x95\xa7\x02F\x05\x87\xd9\x01\r\x11O0F\x11w\xc9e\x99\xc0k\x81B\x8c3'
        RSA decrypted string: Hello InterIntel"""
        ```
