# NLP-001 · Worked solutions

1. “The login is working” versus “The login is not working.” Negation changes meaning.
2. Variable names such as x or language names such as C can carry information. The default two-character word rule may discard them, so consider a task-specific tokenizer using validation data.
3. Keep all messages in a conversation in one partition. If predicting future support traffic, also consider a chronological split. Do not distribute near-duplicate replies across train and test.

[Questions](questions.md)
