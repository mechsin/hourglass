# hourglass
Point Counter and Tracker for rewards system

## Development

The sqlite database name should be hourglass.db

The database can be created quickly with the following command

`sqlite3 hourglass.db < schema.sql`

You can start the flask server by doing the following

`export FLASK_APP=hourglass.py`
`flask run`
or alternatively to run in the background
`flask run &`

During development you can set debug mode to on with the following
`export FLASK_ENV=development`

If your on Windows and in powershell you would do the following
`$env:FLASK_APP="hourglass.py"`
