import twint
import pandas as pd
import webbrowser

def getTweets():
    c = twint.Config()
    c.Lang = "en"
    c.Search = 'request for startup'
    c.Since = "2021-01-01"
    c.Until = "2021-06-07"
    c.Limit = 1
    c.Store_csv = True
    c.Output = "tweets.csv"
    c.Hide_output = True
    # Run
    twint.run.Search(c)

    colsList = ["username", "tweet", "replies_count", "likes_count", "retweets_count"]
    df = pd.read_csv("tweets.csv", usecols=colsList)
    df = df.sort_values(["retweets_count", "likes_count", "replies_count"], ascending=(False, False, False))
    df.drop_duplicates()
    df_html = pd.DataFrame.to_html(df)
    df_html_text = open("tweets.html", "w")
    df_html_text.write(df_html)
    df_html_text.close()

    webbrowser.open_new_tab("tweets.html")

getTweets()