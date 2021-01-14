import argparse
parser = argparse.ArgumentParser()
parser.add_argument("file", help="full path of the source video file")
parser.add_argument("--save", help="save output as a csv file", action="store_true")
parser.add_argument("--verbose", help="make output verbose", action="store_true")
args = parser.parse_args()


from src import analyze_sentiment
try:
    sentiments = analyze_sentiment(args.file, verbose=args.verbose)
    if args.save:
        import csv
        import os

        outfile = os.path.splitext(args.file)[0] + '.csv'
        with open(outfile, 'w', newline='') as csvfile:
            classes = ['negative', 'neutral', 'positive']
            fields = ['text', 'sentiment', 'score']
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            for (text, score) in sentiments:
                if score < 0:
                    sentiment = 'negative'
                elif score == 0:
                    sentiment = 'neutral'
                else:
                    sentiment = 'positive'
                writer.writerow({'text' : text,
                                 'sentiment' : sentiment,
                                 'score': score})
except Exception as ex:
    print(ex)
