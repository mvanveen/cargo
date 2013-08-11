cargo
=====
**Docker Containers for Humans™**

![](supply_crate.jpg)

## Examples

**inspect currently running local containers**

```python
>>> from cargo import Dock
>>> d = Dock()
>>> d 
<Dock [http://localhost:4243] (1.3)>
>>> d.containers
[<Container [9a7a6a52171d]>, <Container [b575c9ece1b9]>, <Container [b225c9398c4b]>]
```

Alternatively, you can get the same result with `cargo.ps`:

```python
>>> import cargo
>>> cargo.ps()
[<Container [9a7a6a52171d]>, <Container [b575c9ece1b9]>, <Container [b225c9398c4b]>]
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

## License

cargo is MIT licensed.
