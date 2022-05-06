[![Open in Streamlit - DOESNT WORK YET](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)]()

# Art generator
This is essentially a streamlit app to run [Dalle Flow](https://github.com/jina-ai/dalle-flow#client).

## How to run this

```
git clone https://github.com/NTTDATAInnovation/avocado-chair.git
cd avocado-chair
poetry install
poetry run streamlit run app.py
```

## Compute server
As a default, the app calls the DALL-E Flow test server. This works well but it's of course risky. To spin up our own compute server, follow this guide

Create an `.env file` and place the url for the custom compute server in it, like so

```
[SERVER]
url = grpc://dalle-flow.jina.ai:51005
```
