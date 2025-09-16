# **llm-payment-receipt-generator**

<p align="center"> 🚀 This script is designed to test nano banana model, generating fakes payment receipts</p>

<h3>🏁 Table of Contents</h3>

<br>

===================

<!--ts-->

💻 [Dependencies and Environment](#dependenciesandenvironment)

☕ [Using](#using)

👷 [Author](#author)

<!--te-->

===================

Attention! All sample receipt files are fake! ⚠️

<div id="dependenciesandenvironment"></div>

## 💻 **Dependencies and Environment**

**Gemini**: This project uses the paid Google Gemini API, it's necessary to [configure a valid Gemini API Key](https://aistudio.google.com/apikey) and link a billing account to it. Ensure you have a `.env` file with the environment variable **API_KEY**.

![gemini key with linked billing account](./docs/gemini_key.png)

<div id="using"></div>

## ☕ **Using**

First, check the [dependencies](#dependenciesandenvironment) process

You can clean the environment using

```
$ make clean
```

To pass dynamic values ​​to fields, check the required and optional parameters in the [`src/args.py`](src/args.py) file.

To execute you can run the script using

```
$ python main.py
```

<div id="author"></div>

#### **👷 Author**

Made by Glener Pizzolato! 🙋

[![Linkedin Badge](https://img.shields.io/badge/-Glener-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/glener-pizzolato/)](https://www.linkedin.com/in/glener-pizzolato-6319821b0/)
[![Gmail Badge](https://img.shields.io/badge/-glenerpizzolato@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:glenerpizzolato@gmail.com)](mailto:glenerpizzolato@gmail.com)
