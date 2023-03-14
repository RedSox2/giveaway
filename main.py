import instaloader
from time import sleep

L = instaloader.Instaloader()

post = instaloader.Post.from_shortcode(L.context, 'CpusuF5Oi1c')

comments = post.get_comments()

entries = []

for comment in comments:
    entries.append(comment.owner.username)

print(entries)