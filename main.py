import instaloader

L = instaloader.Instaloader()

post = instaloader.Post.from_shortcode(L.context, 'CpusuF5Oi1c')

print(post.owner_username)

for comment in post.get_comments():
    print(comment)
    break
