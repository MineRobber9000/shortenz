# shortenz

A URL shortener. Built as a stopgap while I work on a fully-fledged web-accessible link shortener.

## How to use

1. Copy `shortnames.tsv.skel` to `shortnames.tsv` and change the default link.
2. Serve the Flask app via WSGI/nginx or similar.

To add shortnames, add a line to `shortnames.tsv`. For example, to make it so `short.link/whatever` goes to Google, you would input:

```
whatever[TAB]https://www.google.com
```
