from urllib.parse import parse_qsl, quote, splitquery, urlencode


def escape_urn(urn):
    if urn and urn.startswith('/'):
        # remove any trailing to prevent from injecting the HTTP protocol using
        # double slashes
        urn = urn.lstrip('/')
        urn, query = splitquery(urn)

        # we don't want to redirect with any control characters,
        # we have to escape them
        urn = quote(urn)

        if query:
            urn += '?%s' % urlencode(parse_qsl(query))

        new_urn = '/' + urn
        return new_urn
