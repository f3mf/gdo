# Data production

Snippets of the script used for the conversion from CSV data to RDF data, using csv module and RDFLib library of Python. 
<br>Snippet of the script for the conversion of <em>Il Giuoco dell'Oca</em> at Work WEMI level.

```python title="conversion.py"  linenums="1"
--8<-- "docs/data/scripts/conversion.py:1:53"
```
Snippet of the script for the conversion of all the items at Work WEMI level.

```python title="conversion.py"  linenums="1"
--8<-- "docs/data/scripts/conversion.py:105:190"
```

Snippet of the code where the serialization process into a Turtle file is activated.

```python title="conversion.py"  linenums="1"
--8<-- "docs/data/scripts/conversion.py:1346:1351"
```

### Complete dataset in RDF turtle format

??? turtle "See RDF Dataset"

    ```turtle
    --8<-- "docs/data/dataset/rdf-turtle/gdo.ttl"
    ```

### Example of visualization using RDF Grapher tool

The image below shows a visualization of a snippet of the turtle file concerning the item <em>Just what is it that makes today's homes so different, so appealing?</em>, a collage by Richard Hamilton, described within the chapter LXXXVIII, its relationships with the comics <em>Young Romance</em> and with the interpretation acts. 

<div class="grid cards" markdown>
- ![](../data/diagrams/rdf-just-what.svg)
</div>