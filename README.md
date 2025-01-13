export QUART_APP=app.main:app # To define the app
export QUART_DEBUG=1 # To enable auto reload
export PYTHONASYNCIODEBUG=1 # To see endpoints blocking event loop


quart run # for dev mode
uvicorn app.main:app --env-file .env # for production mode