# slow_log_to_json
This tool translates mysql slow query logs into json documents.

## Usage examples:
- python2 slow_log_to_json.py /var/lib/mysql/slow-log
- cat /var/lib/mysql/slow-log | python2 slow_log_to_json.py | less
- zcat /var/log/mysql/slow-log-20151102.gz | slow_log_to_json.py | gzip -c > slow_log.json.gz

## Why?
- Run SQL on your json files, gzipped or raw, using [Apache Drill](https://drill.apache.org/docs/querying-plain-text-files/#query-the-data).
- Index your data on [Elasticsearch](https://www.elastic.co/products/elasticsearch).
- Use [jq](https://stedolan.github.io/jq/) on your data.
