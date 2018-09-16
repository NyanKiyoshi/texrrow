from flask import Blueprint, Response, current_app

import keyboard

sendkeys_bp = Blueprint(
    url_prefix='/sendkeys', name='sendkeys', import_name=__name__)


@sendkeys_bp.route('/next', methods=('POST',))
def next():
    keyboard.send(current_app.config['NEXT_SLIDE_KEY'])
    return Response(status=204)


@sendkeys_bp.route('/prev', methods=('POST',))
def prev():
    keyboard.send(current_app.config['PREV_SLIDE_KEY'])
    return Response(status=204)


@sendkeys_bp.route('/raw/<string:content>', methods=('POST',))
def raw(content):  # noqa
    raise NotImplemented
