import user

# or from user import User
from post import Post
app_user_one = user.User("rr@gg.com", "Riks R", "ppp1", "student")
app_user_one.get_user_info()
app_user_one.change_status("in job market")
app_user_one.get_user_info()


app_user_two = user.User("z43@gg.com", "Bobby L", "zz1", "student")
app_user_two.get_user_info()

new_post = Post("Going for it", app_user_two.name)
new_post.get_post_info()