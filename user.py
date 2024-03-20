from post import Post
from comment import Comment

class User:
    """
    Represents a user on the social media platform.
    """

    def __init__(self, username):
        """
        Initializes a User object with a username.

        Args:
            username (str): The username of the user.

        Raises:
            ValueError: If the username is empty or contains whitespace.
        """
        if not username or username.isspace():
            raise ValueError("Username cannot be empty or contain whitespace")
        self.username = username
        self.posts = []  # List of posts created by the user
        self.comments = []  # List of comments authored by the user (on any post)

    def create_post(self, content):
        """
        Creates a new post for the user.

        Args:
            content (str): The content of the post.

        Returns:
            Post: The newly created Post object.

        Raises:
            ValueError: If the post content is empty.
        """
        if not content:
            raise ValueError("Post content cannot be empty")
        post = Post(self, content)
        self.posts.append(post)
        return post

    def add_comment(self, post, content):
        """
        Adds a comment to a post by the user.

        Args:
            post (Post): The post to add the comment to.
            content (str): The content of the comment.

        Raises:
            ValueError: If the comment content is empty.
        """
        if not content:
            raise ValueError("Comment content cannot be empty")
        comment = Comment(self, post, content)
        post.add_comment(comment)  # Pass the comment to the post
        self.comments.append(comment)
