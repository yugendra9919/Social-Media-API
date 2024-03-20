from user import User
from post import Post
from comment import Comment

# Create some users
user1 = User("alice")
user2 = User("bob")

# Create posts
post1 = user1.create_post("Hello everyone!")
post2 = user2.create_post("Great weather today!")

# Add comments
user2.add_comment(post1, "Nice post, Alice!")
user1.add_comment(post2, "Me too!")

# Print user information
print("User: %s" % user1.username)
print("  Posts:")
for post in user1.posts:
    print("    - %s" % post.content)
    print("      Comments:")
    for comment in post.comments:
        print("        - %s: %s" % (comment.author.username, comment.content))

print("User: %s" % user2.username)
print("  Posts:")
for post in user2.posts:
    print("    - %s" % post.content)
    print("      Comments:")
    for comment in post.comments:
        print("        - %s: %s" % (comment.author.username, comment.content))

