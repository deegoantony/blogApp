from djngo.blogApp.models import users,posts

username="anu"
password="Password@123"
# to check it user name and pass word correct
user=[user for user in users if user["username"]==username and user["password"]==password]


def authenticate(**kwargs):
    username=kwargs.get("username")
    password=kwargs.get("password")
    user = [user for user in users if user["username"] == username and user["password"] == password]
    return user



# GET=RETREVE DATA
#POST=CREAT
#PUT/PATCH=EDIT
#DELET=DELETE

session={}
def signin_requried(fn):
    def wrapper(*args,**kwargs):
        if "user" in session:
            return fn(*args,**kwargs)
        else:
            print("u must log in")
    return wrapper




class SignInView:
    def post(self,*args,**kwargs):
        username=kwargs.get("username")
        password=kwargs.get("password")
        user=authenticate(username=username,password=password)
        if user:
            session["user"]=user[0]
            print("success")
        else:
            print("invalid")

class PostView:
    @signin_requried
    def get(self,*args,**kwargs):
        return posts
    #to add a post
    @signin_requried
    def post(self,*args,**kwargs):
        kwargs["userId"]=session["user"]["id"]
        posts.append(kwargs)
        print(posts)
class MyPostListView:
    @signin_requried
    def get(self,*args,**kwargs):
        print(session)
        userId=session["user"]["id"]
        print(userId)
        my_post=[post for post in posts if post["userId"]==userId]
        return my_post

class PostDetailedView:
    @signin_requried
    def get_oblect(self,id):
        post=[post for post in posts if post["postId"]==id]
        return post
    @signin_requried
    def get(self,*args,**kwargs):
        post_Id=kwargs.get("post_Id")
        data=self.get_oblect(post_Id)
        return data

    @signin_requried
    def delete(self,*args,**kwargs):
        post_Id=kwargs.get("post_Id")
        #data=[post for post in posts if post["postId"]==post_Id]
        data=self.get_oblect(post_Id)
        if data:
            post=data[0]
            posts.remove(post)
            print("post is removed")
            print(len(posts))
    @signin_requried
    def put(self,*args,**kwargs):
        post_id=kwargs.get("post_id")
        post=self.get_oblect(post_id)[0]
        data=kwargs.get("data")
        post.update(data)
        print(post)


class LikedView:
    @signin_requried
    def get(self,*args,**kwargs):
        postid=kwargs.get("postid")
        post=[post for post in posts if post["postId"]==postid]
        if post:
            post=post[0]
            userid=session["user"]["id"]
            post["liked_by"].append(userid)
            print(post)



log=SignInView()
log.post(username="anu",password="Password@123")

# mypost=MyPostListView()
# print(mypost.get())
# post_details=PostDetailedView()
# # post_details.delete(post_Id=6)
# # print(post_details.get(post_Id=5))
# data={
#     "title":"hello there"
# }
# post_details.put(post_id=6,data=data)

like=LikedView()
like.get(postid=7)
