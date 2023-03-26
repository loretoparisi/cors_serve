# cors_serve
CORS Serving with Python HTTP.
The command `cors_serve` replaces `python -m http.serve` adding necessary scaffholding to support CORS.

## Why cors_serve
To give developers a way to allocate and share data using typed arrays between multiple threads, the `ArrayBuffer` and `SharedArrayBuffer` were introduced, where threading is obtained using Web Workers. This enables the sharing of binary data between the web workers. To preserver the *cross-origin isolation* we need a secure environment that limits access using specific response header from the web server:

- Enable the `cross-origin-opener-policy` (COOP) header at the top level of your document, with same-origin:

```
Cross-Origin-Opener-Policy: same-origin
```

This header isolates the page from any cross-origin pop-ups in the browser so that they will not be able to access documents or send direct messages to them. It also ensures your page is in a secure context with pages with the same top-level origins.

- Enable the `cross-origin-embedder-policy` header (COEP) with a value indicating require-CORP (cross-origin resource policy).

```
Cross-Origin-Embedder-Policy: require-corp
```

This ensures all resources loaded from your website have been loaded with CORP.


## Build
```
python setup.py install
```

## Run
```
cd example/
cors_serve
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

### Change PORT
```
cors_serve 8080
Serving HTTP on 0.0.0.0 port 8080 (http://0.0.0.0:8080/) ...
```

## Example
An example of using `SharedArrayBuffer` is provided in the `example/` folder.
