cargo
=====
**Docker Containers for Humans™**

![](supply_crate.jpg)

**inspect currently running containers locally**

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

**inspect container command**

```python
>>> container = d.containers[0]
>>> container.command
u'python -m SimpleHTTPServer'
```
