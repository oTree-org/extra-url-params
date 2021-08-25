import requests
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import RedirectResponse
from starlette.routing import Route

# required if you set OTREE_AUTH_LEVEL
REST_KEY = ''

# if using Heroku, change this to https://YOURAPP.herokuapp.com
OTREE_SERVER = "http://localhost:8000"

ROOM_NAME = 'my_room_name'

# whatever URL parameter uniquely identifies the participant
# oTree calls it participant_label,
# but other platforms may use 'id' or 'pid', so you can customize that here.
PARTICIPANT_LABEL_PARAM = 'participant_label'


GET = requests.get
POST = requests.post


def call_api(method, *path_parts, **params) -> dict:
    path_parts = '/'.join(path_parts)
    url = f'{OTREE_SERVER}/api/{path_parts}/'
    resp = method(url, json=params, headers={'otree-rest-key': REST_KEY})
    if not resp.ok:
        msg = (
            f'Request to "{url}" failed '
            f'with status code {resp.status_code}: {resp.text}'
        )
        raise Exception(msg)
    return resp.json()


def root(request: Request):
    params = dict(request.query_params)

    participant_label = params.pop(PARTICIPANT_LABEL_PARAM)

    call_api(
        POST,
        'participant_vars',
        room_name=ROOM_NAME,
        participant_label=participant_label,
        vars=dict(params),
    )

    room_url = f'{OTREE_SERVER}/room/{ROOM_NAME}/?participant_label={participant_label}'
    return RedirectResponse(room_url)


app = Starlette(debug=True, routes=[Route('/', root)])
