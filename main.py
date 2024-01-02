import requests
from fastapi import FastAPI
from fastapi.responses import RedirectResponse, Response

app = FastAPI()

headers = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Headers": "*",
    "Cache-Control": "no-store, no-cache, must-revalidate, max-age=0",
    "Pragma": "no-cache",
    "Expires": "0",
}


@app.get("/link/unlock")
async def unlock_link(agent: str, apikey: str, link: str, response: Response):
    response.headers.update(headers)

    data = requests.get(f"https://api.alldebrid.com/v4/link/unlock?agent={agent}&apikey={apikey}&link={link}").json()
    if data.get("status") == "success":
        video_url = data["data"]["link"]
    else:
        print(data)
        video_url = "https://882b9915d0fe-mediafusion.baby-beamup.club/static/exceptions/api_error.mp4"

    return RedirectResponse(url=video_url, headers=response.headers)
