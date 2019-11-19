# bert_cn
Chinese sentiment classification based on bert. This code was tested with TensorFlow 1.11.0 and Python 3.6.5

## experiment results (comparing different optimizer) ##

**Hyperparameters:**

max_seq_length=128, train_batch_size=32, learning_rate=1e-6, num_train_epochs=50

**Training Summary:**

| index | platform | device | optimizer | time | loss | accuracy |
| ------| ------ | ------ | ------ | ------ | ------ | ------ |
| 1 | tensorflow | gpu | special adam | 1h | 0.9473789 | 0.815 
| 2 | tensorflow | gpu | adam | 0.5h | **0.4259515** | **0.825** |
