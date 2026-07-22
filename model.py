import torch
import torch.nn as nn
from transformers import AutoTokenizer, AutoModel
from huggingface_hub import hf_hub_download

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# Load base BERT
bert_model = AutoModel.from_pretrained("bert-base-uncased")


class MyModel(nn.Module):
    def __init__(self, bert):
        super(MyModel, self).__init__()

        self.bert = bert
        self.dropout = nn.Dropout(0.3)
        self.linear1 = nn.Linear(768, 256)
        self.relu = nn.ReLU()
        self.linear2 = nn.Linear(256, 1)

    def forward(self, input_ids, attention_mask):
        pooled_output = self.bert(
            input_ids=input_ids,
            attention_mask=attention_mask,
            return_dict=False
        )[0][:, 0]

        output = self.linear1(pooled_output)
        output = self.relu(output)
        output = self.dropout(output)
        output = self.linear2(output)

        return output


# Load trained model
model = MyModel(bert_model)

# Load trained model
model = MyModel(bert_model)

# Download model from Hugging Face
model_path = hf_hub_download(
    repo_id="Rishit925/Bert-Sarcasm-Detector",
    filename="bert_sarcasm_classifier.pth"
)

# Load weights
model.load_state_dict(
    torch.load(
        model_path,
        map_location=device
    )
)

model.to(device)
model.eval()


def predict(text):

    encoding = tokenizer(
        text,
        max_length=64,
        padding="max_length",
        truncation=True,
        return_tensors="pt"
    )

    input_ids = encoding["input_ids"].to(device)
    attention_mask = encoding["attention_mask"].to(device)

    with torch.no_grad():
        output = model(input_ids, attention_mask)
        probability = torch.sigmoid(output).item()

        if probability >= 0.5:
            prediction = "Sarcastic"
            confidence = probability
        else:
            prediction = "Not Sarcastic"
            confidence = 1 - probability

        return prediction, confidence