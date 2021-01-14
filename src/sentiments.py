def analyze_sentiment_google(text):
    # Imports the Google Cloud client library
    from google.cloud import language_v1

    # Instantiates a client
    client = language_v1.LanguageServiceClient()

    # The text to analyze
    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment

    return sentiment.score


def analyze_sentiment_bert(review_text, model, class_names=['negative', 'neutral', 'positive']):
    import numpy as np
    import torch

    from torch import nn
    from transformers import BertModel, BertTokenizer

    class SentimentClassifier(nn.Module):

      def __init__(self, n_classes):
        super(SentimentClassifier, self).__init__()
        self.bert = BertModel.from_pretrained(model)
        self.drop = nn.Dropout(p=0.3)
        self.out = nn.Linear(self.bert.config.hidden_size, n_classes)

      def forward(self, input_ids, attention_mask):
        _, pooled_output = self.bert(
          input_ids=input_ids,
          attention_mask=attention_mask
        )
        output = self.drop(pooled_output)
        return self.out(output)


    # Init PyTorch with random seed
    RANDOM_SEED = 42
    np.random.seed(RANDOM_SEED)
    torch.manual_seed(RANDOM_SEED)

    # Enable CUDA if available
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    # Tokenize and encode input text
    tokenizer = BertTokenizer.from_pretrained(model)
    model = SentimentClassifier(len(class_names))
    model = model.to(device)

    encoded_review = tokenizer.encode_plus(
        review_text,
        max_length=MAX_LEN,
        add_special_tokens=True,
        return_token_type_ids=False,
        pad_to_max_length=True,
        return_attention_mask=True,
        return_tensors='pt',
    )

    # Predict the sentiment
    input_ids = encoded_review['input_ids'].to(device)
    attention_mask = encoded_review['attention_mask'].to(device)

    output = model(input_ids, attention_mask)
    _, prediction = torch.max(output, dim=1)

    return prediction, class_names[prediction]
