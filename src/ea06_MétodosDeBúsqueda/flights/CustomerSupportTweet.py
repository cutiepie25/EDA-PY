import csv
import datetime


# The fields of the class come from the following CSV sample file:
# tweet_id	author_id	inbound	created_at	text	response_tweet_id	in_response_to_tweet_id
# 119237	105834	True	Wed Oct 11 06:55:44 +0000 2017	@AppleSupport causing the reply to be disregarded and the tapped notification under the keyboard is opened😡😡😡	119236	
# 119238	ChaseSupport	False	Wed Oct 11 13:25:49 +0000 2017	@105835 Your business means a lot to us. Please DM your name, zip code and additional details about your concern. ^RR https://t.co/znUu1VJn9r		119239
class CustomerSupportTweet:
    """Class representing a CustomerSupportTweet
    """
    def __init__(self, tweet_id, author_id, inbound, created_at, text, response_tweet_id, in_response_to_tweet_id):
        self.tweet_id = tweet_id
        self.author_id = author_id
        self.inbound = inbound
        # parse a date in the format "Wed Oct 11 06:55:44 +0000 2017" into a datetime object

        self.created_at = datetime.datetime.strptime(created_at, '%a %b %d %H:%M:%S %z %Y')
        self.text = text
        self.response_tweet_id = response_tweet_id
        self.in_response_to_tweet_id = in_response_to_tweet_id
    
    def __str__(self):
        return f"{self.tweet_id}, {self.author_id}, {self.inbound}, {self.created_at}, {self.text}, {self.response_tweet_id}, {self.in_response_to_tweet_id}"

def readCSV(filename: str) -> list:
    with open(filename, 'r') as fh:
        reader = csv.reader(fh, delimiter=',', quotechar='"')
        next(reader)
        return [CustomerSupportTweet(*rec) for rec in reader]




# Example main function:
# Reads the dataset, prints the number of records and the first record
if __name__=="__main__":
    filename = "twcs.csv"
    records = readCSV(filename)
    print(len(records))
    print(records[0])

