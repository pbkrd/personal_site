from main_app.models import Post


def get_all_posts():
    return Post.objects.filter(is_published=True).select_related('cat')[:8]

