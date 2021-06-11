import threading
import queue
import requests
import collections

Item = collections.namedtuple('Item', 'key value')

_queue: queue.Queue = queue.Queue()
_requests = {}
_requests_threads: dict = {}


def update_loop():
    while True:
        item = _queue.get()

        _requests[item.key] = item.value
        _requests_threads[item.key].join()
        del _requests_threads[item.key]


_update_thread = threading.Thread(target=update_loop, daemon=True)
_update_thread.start()


def _async_request(url):
    request = requests.get(url)

    _queue.put(Item(key=url, value=request))


def get(url):
    if url in _requests:
        return _requests[url]

    if url in _requests_threads:
        return None

    request = threading.Thread(target=_async_request, args=(url,))
    _requests_threads[url] = request
    request.start()
    return None