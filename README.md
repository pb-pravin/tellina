# Tellina

Tellina uses natural language processing (NLP) to translate an English sentence, such as "Find text file in the current folder", into a bash command, such as `find . -name "*.txt"`.

### Install Tensorflow:

Follow the instructions on the [official website](https://www.tensorflow.org/versions/r0.9/get_started/os_setup.html). The simplest way is to install using [`pip3`](https://www.tensorflow.org/versions/r0.11/get_started/os_setup.html#pip-installation).

### Install other dependencies:

```
pip3 install -r requirements.txt
```

### Set up tellina_learning_module submodule:

```
git submodule update --remote
git submodule foreach git pull origin master

cd tellina_learning_module/data/bash
tar -xzvf vocab.tar.xz && rm vocab.tar.xz

cd tellina_learning_module/tools/spellcheck
unxz --keep most_common.txt.xz
```

### Set up databases:

```
python3 manage.py makemigrations
python3 manage.py migrate
```

### Run webapp:

```
export PYTHONPATH=`pwd`

python3 manage.py runserver
```
Visit http://127.0.0.1:8000 in your browser.
