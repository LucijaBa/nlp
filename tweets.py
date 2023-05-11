import csv
import snscrape.modules.twitter as sntwitter

query = "(#humour) lang:en"
tweets = []
limit = 1000000

count = 0
currentTweet = ''
with open('humour.csv' , 'w', encoding="utf-8") as file:
    w = csv.writer(file)
    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        if count == limit: 
            break
        else: 
            try:
                currentTweet = tweet.rawContent.replace(";", "")
                if "http" in currentTweet:
                    continue
                #removedHashes = list(filter(lambda x:x[0]!='#', currentTweet.split()))
                #if len(removedHashes) <= 3:
                    #continue
                #currentTweet = " ".join(removedHashes)
                w.writerow([currentTweet.replace("\n", "")])
                print(count)
                count += 1
            except:
                bepis = 5
