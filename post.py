class Post:
    """
    Represents a post on the social media platform.
    """

    def __init__(self, author, content):
        """
        Initializes a Post object with an author and content.

        Args:
            author (User): The user who created the post.
            content (str): The content of the post.

        Raises:
            ValueError: If the post content is empty.
        """
        if not content:
            raise ValueError("Post content cannot be empty")
        self.author = author
        self.content = content
        self.comments = []  # List of comments on this post

    def add_comment(self, comment):
        """
        Adds a comment to this post.

        Args:
            comment (Comment): The comment object to be added.
        """
        self.comments.append(comment)


