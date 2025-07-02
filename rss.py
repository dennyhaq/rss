import feedparser

def baca_rss(url):
    print(f"Membaca RSS dari: {url}\n")
    feed = feedparser.parse(url)

    if feed.bozo:
        print("Gagal parsing RSS feed. Cek URL atau format feed.")
        print("Error:", feed.bozo_exception)
        return

    if 'title' in feed.feed:
        print(f"Feed Title: {feed.feed.title}\n")
    else:
        print("Feed tidak memiliki judul.")

    if not feed.entries:
        print("Feed kosong, tidak ada item berita.")
        return

    for i, entry in enumerate(feed.entries, 1):
        print(f"{i}. {entry.title}")
        #print(f"   Link: {entry.link}")
        #print("-" * 40)

if __name__ == "__main__":
    url = "https://lapi.kumparan.com/v2.0/rss/"
    baca_rss(url)
    