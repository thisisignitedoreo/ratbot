import base64
coded_string = '''T1RRNE1qVTVNelV3T1RNMk5EUTVNRGsxLlloNU5Wdy5fdDJXU0VBNGxGcDIzM3ZXaGVFYVNwWUVaT2M='''
tkn = base64.b64decode(coded_string)
settings = {
    'token': tkn,
    'bot': 'RatBot',
    'id': 948259350936449095,
    'prefix': 'r!'
}
