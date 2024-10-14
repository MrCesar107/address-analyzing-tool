# Address Analyzing Tool

A tool for analyzing and detection of malicious addresses (URLs, IPs, Hashes)

## Development

In one terminal window, start Vite in development mode
`$ npm run dev`

In other terminal window, start Flask in debug mode
`$ flask --debug --app main run --port 8080`

## Production

First build the production assets
`$ npm run build`

Then boot the production server
`$ gunicorn --workers 4 --bind 127.0.0.1:8000 'main:app'`
