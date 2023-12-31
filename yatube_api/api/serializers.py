from rest_framework import serializers

from posts.models import Post, Group, Comment


class PostSerializer(serializers.ModelSerializer):
    """ Сериалайзер для модели Post. """
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username')
    comments = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = (
            'id', 'text', 'pub_date', 'author',
            'image', 'group', 'comments'
        )


class GroupSerializer(serializers.ModelSerializer):
    """ Сераилизатор для модели Group. """
    posts = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description', 'posts')


class CommentSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели Comment. """
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username')
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'text', 'created', 'author', 'post')
