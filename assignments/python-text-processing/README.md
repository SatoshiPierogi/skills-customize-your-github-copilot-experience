# 📘 Assignment: Python Text Processing

## 🎯 Objective

Learn how to read and write text files in Python and perform useful text-processing tasks such as tokenization, counting words, filtering lines, and finding and replacing text. This assignment focuses on practical string manipulation, file I/O, and lists/dictionaries for aggregation.

## 📝 Tasks

### 🛠️ Implement Text File Analysis
#### Description
Create a Python script that reads a text file and performs basic analysis: count words, compute unique words, find the most common words, and output a report. The script should be robust to punctuation, whitespace, and letter case.

#### Requirements
Completed program should:
- Read a text file path provided by the user (via command-line arg or prompt).
- Tokenize the text into words (case-insensitive), ignoring common punctuation.
- Print total word count and number of unique words.
- Show the top 10 most frequent words and their counts.
- Optionally write a simple report to an output file when provided.

### 🛠️ Implement Text Transformations (Optional)
#### Description
Add features that modify and write text output such as replacing words, filtering lines by a keyword, or generating a cleaned version of the file.

#### Requirements
Completed program may include any of the following:
- Replace all occurrences of a word and save the transformed file.
- Filter out empty lines or lines that do not match a pattern.
- Offer a `--case-sensitive` flag for counting.
- Export a CSV summary of word counts.

---

### Example usage
```
$ python starter-code.py --input sample.txt --top 10 --output report.txt
Total words: 567
Unique words: 234
Top 10 words:
the: 32
and: 26
to: 20
...
Report written to report.txt
```

Use `starter-code.py` in this folder as a scaffold—complete the TODOs and add tests if you like.

**Skills practiced:** File I/O, string manipulation, dictionaries, command-line interfaces (argparse), and basic data aggregation.
