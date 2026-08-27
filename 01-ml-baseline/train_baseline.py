from download_data import DATA_DIR, load_or_download_dataset
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,f1_score
from collections import Counter
import sys



#数据的处理

def prepare_baseline_data(datasets):
    train_data = datasets['train']
    test_data = datasets['test']
    val_data = datasets['validation']

    x_train = [x["text"] for x in train_data]
    y_train = [y["label"] for y in train_data]

    x_test = [x["text"] for x in test_data]
    y_test = [y["label"] for y in test_data]

    x_val = [x["text"] for x in val_data]
    y_val = [y["label"] for y in val_data]

    print("训练集标签分布：", Counter(y_train))
    print("测试集标签分布：", Counter(y_test))
    print("验证集标签分布：", Counter(y_val))
    return (
        x_train,
        y_train,
        x_test,
        y_test,
        x_val,
        y_val,
    )

#训练
def train_baseline(x_train, y_train, x_val, y_val):
    experiments = [
        {"name":"baseline","max_features":5000,"ngram":(1,1),"C":1.0},
        {"name":"More-word","max_features":10000,"ngram":(1,1),"C":1.0},
        {"name":"bigngram","max_features":5000,"ngram":(1,2),"C":1.0},
        {"name": "strong_reg", "max_features": 5000, "ngram": (1, 1), "C": 0.5},
        {"name": "weak_reg", "max_features": 5000, "ngram": (1, 1), "C": 1.5},
        {"name": "most_reg", "max_features": 5000, "ngram": (1, 1), "C": 0.01},
        {"name": "least_reg", "max_features": 5000, "ngram": (1, 1), "C": 10},
        {"name": "longgram", "max_features": 5000, "ngram": (2, 5), "C": 1.0},
    ]
    best_score = 0
    idx = 0
    for idex,exp in enumerate(experiments):
        print(f"\n{'='*40}")
        print(exp["name"]) #实验组名字
        print(exp["max_features"],exp["ngram"],exp["C"]) #数据
        print(f"{'=' * 40}")

        vectorizer = TfidfVectorizer(max_features = exp["max_features"],ngram_range = exp["ngram"])
        x_train_vec = vectorizer.fit_transform(x_train) #学习
        x_vali_vec = vectorizer.transform(x_val) #考试
        #训练
        model = LogisticRegression(
            max_iter=1000,
            C = exp["C"],
            random_state = 42,
        )
        model.fit(x_train_vec, y_train)

        #测评
        pred = model.predict(x_vali_vec)
        acc = accuracy_score(y_val,pred)
        f1 = f1_score(y_val,pred,average = "macro")

        if f1 > best_score:
            best_score = f1
            idx = idex

        print(f"准确率：{acc:.4f}")
        print(f"F1 score: {f1:.4f}")
        print(f"{'=' * 40}\n")
    return idx,experiments

#最终测试
def eval_test_baseline(x_train, y_train,x_test, y_test,experiments,idx):
    exp = experiments[idx]
    print(exp["name"])
    print(exp["max_features"],exp["ngram"],exp["C"])
    print(f"{'='*40}\n")

    vectorizer = TfidfVectorizer(max_features = exp["max_features"],ngram_range = exp["ngram"])
    x_train_vec = vectorizer.fit_transform(x_train)
    x_test_vec = vectorizer.transform(x_test)
    model = LogisticRegression(
        max_iter=1000,
        C = exp["C"],
        random_state = 42,
    )

    model.fit(x_train_vec, y_train)

    pred = model.predict(x_test_vec)
    acc = accuracy_score(y_test,pred)
    f1 = f1_score(y_test,pred,average = "macro")

    print(f"准确率:{acc:.4f}")
    print(f"得分:{f1:.4f}")
    print(f"{'='*40}\n")

    wrong = [i for i in range(len(y_test)) if pred[i] != y_test[i]]
    print(f"\n预测错 {len(wrong)} 条样本")
    print(f"{'=' * 40}\n")
    for i in wrong[:5]:
        print(x_test[i],pred[i],y_test[i])

def main():
    datasets = load_or_download_dataset(DATA_DIR)
    x_train, y_train, x_test, y_test, x_val, y_val = prepare_baseline_data(datasets)
    idx,experiments = train_baseline(x_train, y_train, x_val, y_val)
    eval_test_baseline(x_train, y_train, x_test, y_test, experiments, idx)

if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    main()

