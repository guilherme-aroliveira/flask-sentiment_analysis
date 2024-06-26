# Flask Sentiment Analysis Project

[![License](https://img.shields.io/badge/License-Apache-yellow.svg)](https://opensource.org/license/apache-2-0)

This is a project of the course "Developing AI Applications with Python and Flask" by IBM as part of IBM DevOps course.

### Description

This project consist of building a Python web app using Flask and integrate Embeddable Watson AI libraries. This uses the BERT based Sentiment Analysis function of the Watson NLP Library.

### Usage

In order to use BERT and IBM Watson API it's necessary to import these libraries. This differs from the original project done on Cloud IDE server offered by IBM.

To call the application on python shell:

```python
$ python3
>>> from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
>>> sentiment_analyzer("I'm enjoying to play with ibm watson")
```


### License

Copyright (c) 2024, Guilherme Oliveira. All rights reserved.

Licensed under the Apache License. See [LICENSE](LICENSE)