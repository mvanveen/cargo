cargo
=====
**Docker Containers for Humans™**

![](supply_crate.jpg)

**:warning: WARNING** *This is a very early alpha release of cargo.  All development 
for this project is being done in the open.  Contributions are totally welcome, but 
please at least announce and discuss your plans via an issue before submitting a pull 
request so we can all create something beautiful!*

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
