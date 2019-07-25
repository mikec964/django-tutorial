# I ran these in the CLI
# python manage.py shell

import json
from .models import Post


with open('blog/test-posts.json') as f:
    posts_json = json.load(f)
for postd in posts_json:
    posto = Post(title=postd['title'], content=postd['content'], author_id=postd['user_id'])
    posto.save()

# If you've mucked about with users, be sure user_id in test file matches
# actual author_ids
