cargo
=====
**Docker Containers for Humans™**

![](supply_crate.jpg)

**:warning: WARNING** *This is a very early alpha release of cargo.  All development 
for this project is being done in the open.  Contributions and critiques are totally
welcome, but please at least announce and discuss your plans via an issue before 
submitting a pull request so we can all collectively create something beautiful!*

## Examples

**inspect currently running local containers**

```python
>>> from cargo import Dock
>>> d = Dock()
>>> d.containers
[<Container [9a7a6a52171d]>, <Container [b575c9ece1b9]>, <Container [b225c9398c4b]>]

```
Alternatively, you can get the same result with `cargo.ps`:

```python
>>> import cargo
>>> cargo.ps()
[<Container [9a7a6a52171d]>, <Container [b575c9ece1b9]>, <Container [b225c9398c4b]>]
```

**get dock metadata**

```python
>>> d 
<Dock [http://localhost:4243] (1.3)>
>>> d.info
{u'NFd': 28, u'MemoryLimit': True, u'NGoroutines': 36, u'Images': 112, u'Debug': False, u'Containers': 189}
>>> d.memory_limit
True
```

**inspect command string running in container**

```python
>>> container = d.containers[0]
>>> container.command
u'python -m SimpleHTTPServer'
```

**inspect forwarded container ports**

In this example, we're forwarding port `49155` locally to port 
`8000` within the container.

```python
>>> container = d.containers[0]
>>> container.ports
[(49155, 8000)]
```

**inspect container logs**

In this example we are running `python -m SimpleHTTPServer` to fire up a basic HTTP 
server on port `8000`.  We use `container.ports` to grab out the locally forwarded port, 
issue an HTTP `GET` using python requests, and then inspect the subsequent container 
logs, which now contain an apache logs entry for our `GET` request, :sparkles: 
*as if by magic*! :sparkles:

```python
>>> import cargo
>>> import requests
>>> container = cargo.ps()[0]
>>> container
<Container [9a7a6a52171d]>
>>> container.command
u'python -m SimpleHTTPServer'
>>> container.logs
u''
>>> requests.get('http://localhost:%s' % (container.ports[0][0]))
<Response [200]>
>>> container.logs
u'172.16.42.1 - - [11/Aug/2013 12:49:56] "GET / HTTP/1.1" 200 -\n'
```

## License

cargo is MIT licensed.
