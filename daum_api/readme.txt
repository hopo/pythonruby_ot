### kakao link REST api


# User login and get code
https://kauth.kakao.com/oauth/authorize
?client_id=d9a3abf69a902d0da2421bf4913aed
&redirect_uri=http://localhost:9999/oauth
&response_type=code

# Get acess_token
https://kauth.kakao.com/oauth/token
?grant_type=authorization_code
&client_id=d9a3abf69a902d0da2421bf4913aed
&redirect_uri=http://localhost:9999/oauth
&code=fj29eYSk_lCYSqvrJV3vJsNb5Yi4PoibHjLv5kj0zk_0_mH5jeeam9qMO24zW7heKSIgopdaYAAAFnF5zA7g


# Profile request
https://kapi.kakao.com/v1/api/talk/profile
?access_token=dJUcQLPsPDlpa3APttf8X4K1NsZhZLrLh-_AopdaYAAAFnF5-jvg




