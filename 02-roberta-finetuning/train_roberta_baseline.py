import os
from pathlib import Path

from datasets import load_from_disk
import numpy as np
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    TrainingArguments,
    Trainer,
    DataCollatorWithPadding,
)
from sklearn.metrics import accuracy_score, f1_score
import torch

os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["TRANSFORMERS_OFFLINE"] = "1"

PROJECT_DIR = Path(__file__).resolve().parents[1]
data_DIR = PROJECT_DIR / "01-ml-baseline" / "data" / "tweet_irony"
cache_DIR = PROJECT_DIR / "hf-cache"
out_DIR = PROJECT_DIR / "models" / "result_roberta_base"
os.makedirs(cache_DIR, exist_ok=True)
os.makedirs(out_DIR, exist_ok=True)

#加载数据
train = load_from_disk(os.path.join(data_DIR,"train"))
test = load_from_disk(os.path.join(data_DIR,"test"))
vali = load_from_disk(os.path.join(data_DIR,"validation"))
print("数据：",len(train),len(test),len(vali))

#加载分词器+模型
model = "roberta-base"
tokenizer = AutoTokenizer.from_pretrained(model, cache_dir=cache_DIR)
model = AutoModelForSequenceClassification.from_pretrained(
    model,
    cache_dir=cache_DIR,
    num_labels = 2,
)
print("分词器：yes，模型：yes")

#数据处理
def tokenizer_fn(batch):
    return tokenizer(batch["text"],padding = True,truncation = True,max_length = 256)
cols_to_remove = [c for c in train.column_names if c not in ("label",)]
train_ds = train.map(tokenizer_fn,batched = True,remove_columns = cols_to_remove)
test_ds = test.map(tokenizer_fn,batched = True,remove_columns = cols_to_remove)
vali_ds = vali.map(tokenizer_fn,batched = True,remove_columns = cols_to_remove)
print("分词后的字段：",train_ds.column_names)

#评分
def computer_metrics(eval_pred):
    logits,labels = eval_pred
    preds = np.argmax(logits,axis = -1)
    return {
        "accuracy":accuracy_score(labels,preds),
        "f1":f1_score(labels,preds,average = "macro")
    }

#  训练  （注重学习）
training_args =TrainingArguments(
    output_dir=out_DIR,
    num_train_epochs = 4,
    per_device_train_batch_size = 16,
    per_device_eval_batch_size = 32,
    learning_rate = 2e-5,
    weight_decay = 0.018,
    warmup_steps = 0.06,
    logging_steps = 50,
    eval_strategy = "epoch",
    save_strategy = "epoch",
    load_best_model_at_end = True,
    metric_for_best_model ="f1",
    greater_is_better = True,
    report_to = "none",
    fp16 = True,
)

data_collator = DataCollatorWithPadding(tokenizer=tokenizer)
trainer = Trainer(
    model = model,
    args = training_args,
    train_dataset = train_ds,
    eval_dataset = vali_ds,
    data_collator = data_collator,
    compute_metrics = computer_metrics,
)
#no train eval test

pre_out = trainer.predict(test_ds)
pre_labels = np.argmax(pre_out.predictions,axis = -1)
true_pred = pre_out.label_ids
acc = accuracy_score(true_pred,pre_labels)
f1 = f1_score(true_pred,pre_labels,average = "macro")
print(f"未微调准确率：{acc:.4f}")
print(f"未微调f1得分：{f1:.4f}")


print("train start")
trainer.train()
print(f"最佳模型来自第 {trainer.state.best_model_checkpoint} 轮")

print("finally eval")
pred_out = trainer.predict(test_ds)
pred_labels = np.argmax(pred_out.predictions,axis = -1)
true_pred = pred_out.label_ids

acc = accuracy_score(true_pred,pred_labels)
f1 = f1_score(true_pred,pred_labels,average = "macro")
print("=" * 40)
print(f"roberta-base 微调后  TEST acc = {acc:.4f}")
print(f"roberta-base 微调后  TEST f1  = {f1:.4f}")
print("=" * 40)

save_path = os.path.join(out_DIR,"best_model")
trainer.save_model(save_path)
tokenizer.save_pretrained(save_path)
print("已保存到:", save_path)
