from djngo.blogApp.models import users, posts

username = "vinu"
password = "Password@123"
user = [i for i in users if i["username"] == username and i["password"] == password]


def authenticate(**kwargs):
    username = kwargs.get("username")
    password = kwargs.get("password")
    user = [i for i in users if i["username"] == username and i["password"] == password]
    return user


session = {}


class SignIN:
    def get(self, *args, **kwargs):
        username = kwargs.get("username")
        password = kwargs.get("password")
        use = authenticate(username=username, password=password)
        if use:
            session["user"] = user[0]
            print("success")
        else:
            print("invalid")


class PostView:
    def get(self, *args, **kwargs):
        return posts

    def post(self, *args, **kwargs):
        kwargs["userId"] = session["user"]["id"]
        posts.append(kwargs)
        print(posts)
class MyPostView:
    def get(self,*args,**kwargs):
        print(session)
        useid=session["user"]["id"]
        post=[post for post in posts if post["userId"]==useid]
        print(post)


signin = SignIN()
signin.get(username="vinu", password="Password@123")

mypost=MyPostView()
mypost.get()

