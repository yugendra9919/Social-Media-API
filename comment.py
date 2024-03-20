
class Comment:
    """
    Represents a comment on a post on the social media platform.
    """

    def __init__(self, author, post, content):
        """
        Initializes a Comment object with an author, the post it belongs to, and content.

        Args:
            author (User): The user who authored the comment.
            post (Post): The post this comment belongs to.
            content (str): The content of the comment.

        Raises:
            ValueError: If the comment content is empty.
        """
        if not content:
            raise ValueError("Comment content cannot be empty")
        self.author = author
        self.post = post
        self.content = content


