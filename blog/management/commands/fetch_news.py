import requests
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from blog.models import Article

class Command(BaseCommand):
    help = 'Fetches the latest programming news and saves them to the database'

    def handle(self, *args, **kwargs):
        api_key = '400f179428444b879f95d1ea64a56420'
        url = 'https://newsapi.org/v2/everything'
        
        # Date actuelle moins 30 jours pour la date de début
        from_date = (datetime.now() - timedelta(days=180)).strftime('%Y-%m-%d')

        params = {
            'q': 'python OR javascript OR django OR djangorest OR c++ OR oriente objet Or Object Oriend Programming OR datascience OR math ',
            'from': from_date,
            'sortBy': 'popularity',
            'apiKey': api_key
        }

        response = requests.get(url, params=params)
        if response.status_code == 200:
            articles = response.json().get('articles', [])
            for item in articles:
                # Convert publishedAt to datetime object
                published_at = datetime.strptime(item['publishedAt'], '%Y-%m-%dT%H:%M:%SZ')
                
                # Create or update article
                article, created = Article.objects.update_or_create(
                    title=item['title'],
                    defaults={
                        'content': item['description'],
                        'author': item['author'],
                        'publication_date': published_at,
                        'url': item['url'],
                        'url_to_image': item.get('urlToImage'),
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Article "{article.title}" added.'))
                else:
                    self.stdout.write(self.style.SUCCESS(f'Article "{article.title}" updated.'))
        else:
            self.stdout.write(self.style.ERROR('Failed to fetch news.'))
