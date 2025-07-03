import requests

# Replace with your actual NewsAPI key
API_KEY = "6be6c6267afb48b189282e0a70963a79"
BASE_URL = "https://newsapi.org/v2/top-headlines"

# Available categories
CATEGORIES = ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']

def fetch_news(category=None, keyword=None):
    params = {
        'apiKey': API_KEY,
        'country': 'us',  # You can change to 'us', 'gb', etc.
        'pageSize': 10
    }
    if category:
        params['category'] = category
    if keyword:
        params['q'] = keyword

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if data.get('status') != 'ok':
        print("❌ Failed to fetch news.")
        return

    articles = data.get('articles', [])
    if not articles:
        print("No news found.")
        return

    for i, article in enumerate(articles, 1):
        print(f"\n{i}. {article['title']}")
        print(f"   Source: {article['source']['name']}")
        print(f"   URL: {article['url']}")
        print(f"   Published: {article['publishedAt'][:10]}")

def main():
    print("🗞️ Welcome to the News Aggregator CLI App 🗞️")
    while True:
        print("\nOptions:")
        print("1. View Top News")
        print("2. Filter by Category")
        print("3. Search by Keyword")
        print("4. Exit")
        choice = input("Choose an option (1–4): ")

        if choice == '1':
            fetch_news()
        elif choice == '2':
            print("\nAvailable categories:")
            for cat in CATEGORIES:
                print(f"- {cat}")
            selected = input("Enter a category: ").lower()
            if selected in CATEGORIES:
                fetch_news(category=selected)
            else:
                print("❌ Invalid category.")
        elif choice == '3':
            keyword = input("Enter keyword to search: ")
            fetch_news(keyword=keyword)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("❌ Invalid option. Try again.")

if __name__ == "__main__":
    main()
