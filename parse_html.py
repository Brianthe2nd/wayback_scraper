from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import re
import os
import traceback


# html = '''<link rel="canonical" href="https://web.archive.org/web/20200903151445/https://twitter.com/nekrovevo/status/1301536632558899207">'''

def get_archive_link(soup):
    href_value2 = soup.select_one('link[rel="canonical"]')["href"]
    
    return href_value2

def parse_tweet(tweet_container):
    pass


def parse_twitter_datetime(date_str: str) -> datetime:
    return datetime.strptime(date_str, "%I:%M %p - %d %b %Y")

def parse_username(strong_tag):
    parts = []
    for child in strong_tag.children:
        # If it's plain text, keep it
        if child.name is None:
            if child.strip():
                parts.append(child.strip())
        # If it's the hidden span (contains real emoji)
        elif child.get("class") and "visuallyhidden" in child["class"]:
            emoji = child.get_text(strip=True)
            if emoji:
                parts.append(emoji)
        # Ignore the image-based emoji spans (duplicates)
        else:
            continue

    # Join all pieces together
    username = "".join(parts)
    return username

#permalink-overlay > div.PermalinkOverlay-modal > div.PermalinkOverlay-content > div > div > div.permalink.light-inline-actions.stream-uncapped.has-replies.original-permalink-page > div.permalink-inner.permalink-tweet-container.ThreadedConversation.ThreadedConversation--permalinkTweetWithAncestors > div > div.ReplyingToContextBelowAuthor > a > span > b

def parse_html(soup,title):
    main_container = soup.select_one('div[role="main"]')
    ancestor_container = main_container.select_one("div.permalink-in-reply-tos")
    descendant_container = main_container.select_one("div.replies-to")
    link_container = main_container.select_one("div.permalink-tweet-container")
    # ancestor_tweets = ancestor_container.select("ol.stream-items li.stream-item")
    
    # for tweet_container in ancestor_tweets:
    #     tweet =
    tweet_text_elem  = link_container.select_one("div.js-tweet-text-container p.js-tweet-text") 
    tweet_text = tweet_text_elem.get_text().strip().replace('\n', '')
    tweet_text = re.sub(r"\s+", " ", tweet_text).strip()
    if "https" in tweet_text:
        tweet_text = tweet_text.split("https")[0]
    if "pic.twitter" in tweet_text:
        tweet_text = tweet_text.split("pic.twitter")[0]

    time_elem = link_container.select_one("div.js-tweet-details-fixer.tweet-details-fixer span > span")
    time_text = time_elem.get_text().strip()
    
    # print("The tweet is :", tweet_text)
    print("The time is:", parse_twitter_datetime(time_text))
    time_text = parse_twitter_datetime(time_text)
    username = parse_username(link_container.select_one("strong.fullname"))
    mentions = None
    if ancestor_container is None:
        reply = False
    else:
        reply = True
        mentions = link_container.select_one("div.ReplyingToContextBelowAuthor span.username > b")
        if mentions is None:
            mentions_container = link_container.select_one("span.username > b")
            if mentions_container != None:
                mentions = mentions_container.get_text().strip()
            else:
                mentions = username
            
        else:
            mentions = mentions.get_text().strip()
        
    quote_container = link_container.select_one("div.QuoteTweet")
    if quote_container is None:
        quote = False
    else:
        quote = True
        mentions = quote_container.select_one("span.username > b")
        if mentions == None:
            mentions_container = link_container.select_one("span.username > b")
            if mentions_container != None:
                mentions = mentions_container.get_text().strip()
            else:
                mentions = username
            
        else:
            mentions = mentions.get_text().strip()
        
    
    link = get_archive_link(soup)
    if  "web.archive.org" not in link and "twitter" in link:
        timeline = title.split("_")[0]
        link = f"https://web.archive.org/web/{timeline}/{link}"
        
    
    image_container = link_container.select_one("div.AdaptiveMediaOuterContainer")
    if image_container is None:
        image = False
    else:
        image = True
    print("Tweet text:", tweet_text)
    print("Username:", username)
    print("Mentions:",mentions)
    print("Date:",time_text)
    print("Image:",image)
    print("Link:",link)
    print("Quote:",quote)
    print("Reply:",reply)
    
    tweet_obj = {
        "tweet_text": tweet_text,
        "username": username,
        "mentions": mentions,
        "date": time_text,
        "image": image,
        "link": link,
        "quote": quote,
        "reply": reply}
    
    return tweet_obj

def main(): 
    tweets = []
    error_tweets = []
    nekro_posts = os.listdir("archive")
    for post in nekro_posts:
        if post.endswith(".html"):
            try:
                with open(f"archive/{post}", "r", encoding="utf-8") as f:
                    html = f.read()
                soup = BeautifulSoup(html, "html.parser")
                tweet = parse_html(soup,post)
                tweets.append(tweet)

            except Exception as e:
                
                print("Error",e ,"in:",post)
                error_tweets.append(post)
                traceback.print_exc()
                error_message = traceback.format_exc()
                error_tweets.append(error_message)
    
    df = pd.DataFrame(tweets)
    df.to_csv("tweets.csv", index=False)
    
    with open("error_tweets.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(error_tweets))
                


if __name__  == "__main__":
    main()

