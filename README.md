Hi, please follow the following steps to get these scripts to work:

1. Feel free to either create a new python virutal environment `python -m venev env` then do a `source env/bin/activate`. Or you can use your conda or however you have setup python on your local
2. `pip install -r requirements.txt` to install dependencies
3. You will need to set a few environment variables to access this class' database - you can set these by editing the `creds.sh` file and then doing a `source creds.sh`.
4. Feel free to change the query and stringify function.
5. Run `python kafka_consumer.py` before running `python kafka_producer.py` and voila!