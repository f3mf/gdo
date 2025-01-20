import rdflib
import csv
import re
from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import RDF, RDFS, XSD, OWL

g = rdflib.Graph()

miro = Namespace("https://w3id.org/miro/")
lrmoo = Namespace("http://iflastandards.info/ns/lrm/lrmoo/")
rdaw = Namespace("http://rdaregistry.info/Elements/w/")
rdae = Namespace("http://rdaregistry.info/Elements/e/")
rdam = Namespace("http://rdaregistry.info/Elements/m/")
rdaco = Namespace("http://rdaregistry.info/termList/RDAContentType/")
crm = Namespace("http://www.cidoc-crm.org/cidoc-crm/")
hico = Namespace("http://purl.org/emmedi/hico")
cito = Namespace("http://purl.org/spar/cito/")
prov = Namespace("http://www.w3.org/ns/prov#")

# Associate prefix to the namespace in turtle
g.bind("miro", miro) 
g.bind("lrmoo", lrmoo) 
g.bind("rdaw", rdaw) 
g.bind("rdae", rdae) 
g.bind("rdam", rdam) 
g.bind("rdaco", rdaco) 
g.bind("crm", crm) 
g.bind("hico", hico) 
g.bind("cito", cito) 
g.bind("prov", prov) 

# CSV GDO-W

# Open the CSV file and read it into a Dict
with open('/content/drive/MyDrive/Colab Notebooks/DEFINITIVO - gdo-w.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    # Iterate through each row and get the value associated
    for row in csv_reader:
      work_label = row["lrmoo:F1_Work"]
      work_uri = miro+"work/"+work_label
      title_w_label = row['rdaw:P10088 "has title of work"']
      author_label = row['rdaw:P10436 "has author person"']
      author_uri = miro+"agent/"+author_label
      type_work = row['rdaw:P10004 "has category of work"']
      wemi_w_label = row["lrmoo:R3_is_realised_in"]
      wemi_w_uri = miro+"expression/"+wemi_w_label

      # Add triples
      g.add(( URIRef(work_uri), RDF.type , lrmoo.F1 ))
      g.add((URIRef(work_uri), rdaw.P10088, Literal(title_w_label,datatype=XSD.string)))
      g.add((URIRef(work_uri), rdaw.P10065, URIRef(author_uri)))
      g.add((URIRef(work_uri), rdaw.P10004, Literal(type_work, datatype=XSD.anyURI)))
      g.add((URIRef(work_uri), lrmoo.R3, URIRef(wemi_w_uri)))

#CSV GDO-E

# Open the CSV file and read it into a Dict
with open('/content/drive/MyDrive/Colab Notebooks/DEFINITIVO - gdo-e.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    # Iterate through each row and get the value associated
    for row in csv_reader:
      expression_label = row["lrmoo:F2_Expression"]
      expression_uri = miro+"expression/"+expression_label
      title_e_label = row['rdae:P20312 "has title of expression"']
      component_label = row['lrmoo:R5_has_component']
      component_uri = miro+"section/"+component_label
      content_label = row['rdae:P20001 "has content type"']
      content_uri = rdaco+content_label
      language_label = row['rdae:P20006 "has language of expression"']
      editor_label = row['rdae:P20338 "has editor person"']
      editor_uri = miro+"agent/"+editor_label
      wemi_e_label = row["lrmoo:R4i_is_embodied_in"]
      wemi_e_uri = miro+"manifestation/"+wemi_e_label

      # Add triples
      g.add((URIRef(expression_uri), RDF.type, lrmoo.F2))
      g.add((URIRef(expression_uri), rdae.P20312, Literal(title_e_label,datatype=XSD.string)))
      g.add((URIRef(expression_uri), lrmoo.R5, URIRef(component_uri)))
      g.add((URIRef(expression_uri), rdae.P20001, URIRef(content_uri)))
      g.add((URIRef(expression_uri), rdae.P20006, Literal(language_label,datatype=XSD.language)))
      g.add((URIRef(expression_uri), rdae.P20338, URIRef(editor_uri)))
      g.add((URIRef(expression_uri), lrmoo.R4, URIRef(wemi_e_uri)))

#CSV GDO-M

# Open the CSV file and read it into a Dict
with open('/content/drive/MyDrive/Colab Notebooks/DEFINITIVO - gdo-m.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    # Iterate through each row and get the value associated
    for row in csv_reader:
      manifestation_label = row["lrmoo:F3_Manifestation"]
      manifestation_uri = miro+"manifestation/"+manifestation_label
      publication_label = row['rdam:P30011 "has date of publication"']
      place_publication_label = row['rdam:P30088 "has place of publication"']
      place_publication_uri = miro+"place/"+place_publication_label
      publisher_corp_body_label = row['rdam:P30420 "has publisher corporate body"']
      publisher_corp_body_uri = miro+"agent/"+publisher_corp_body_label

      # Add triples
      g.add((URIRef(manifestation_uri), RDF.type, lrmoo.F3))
      g.add((URIRef(manifestation_uri), rdam.P30011, Literal(publication_label,datatype=XSD.integer)))
      g.add((URIRef(manifestation_uri), rdam.P30088, URIRef(place_publication_uri)))
      g.add((URIRef(manifestation_uri), rdam.P30420, URIRef(publisher_corp_body_uri)))

#CSV ITEM-W

# Open the CSV file and read it into a Dict
with open('/content/drive/MyDrive/Colab Notebooks/DEFINITIVO - item-w.csv', mode='r') as csv_file:
  csv_reader = csv.DictReader(csv_file)
  # Iterate through each row
  for row in csv_reader:
    #Iterate through each key of the row
    for key in row.keys():
      # Retrieves the value of the current key and removes whitespaces
      value = row.get(key).strip()

      # Reg ex for capital letters and URIs
      capital_letter_regex = re.compile(r'^[A-Z]')
      http_regex = re.compile(r'\bhttps?://\S+')

      # Add a triple that associates the first column's value in the row with the type of entity
      g.add((URIRef(miro + "work/"+str(row.get(list(row.keys())[0]))), RDF.type, lrmoo.F1))

      # Skip the first column
      if key != list(row.keys())[0]:

        # Check if the value is not empty
        if value:

          # Subject of the URI
          subj = URIRef(miro+"work/"+str(row.get("lrmoo:F1")))

          # Split the predicate in prefix and suffix
          column_split = str(key).split(":")
          prefix = column_split[0]
          suffix = column_split[1]

          # Create a Dict of the namespaces (key=prefix; uri=value)
          namespaces = {"miro":"https://w3id.org/miro/",
          "lrmoo" : "http://iflastandards.info/ns/lrm/lrmoo/",
          "rdaw" : "http://rdaregistry.info/Elements/w/",
          "rdae" : "http://rdaregistry.info/Elements/e/",
          "rdam": "http://rdaregistry.info/Elements/m/",
          "rdaco": "http://rdaregistry.info/termList/RDAContentType/",
          "owl" : "http://www.w3.org/TR/owl-ref/",
          "rdfs" : "http://www.w3.org/TR/rdf11-schema/",
          "crm" : "http://www.cidoc-crm.org/cidoc-crm/"}

          # Check if the prefix is in the Dict and create the predicate URI
          if prefix in namespaces:
            base_uri = namespaces[prefix]
            predicate = URIRef(base_uri+suffix)
            if prefix == "owl":
              predicate = OWL.sameAs
            if prefix == "rdfs":
              predicate = RDFS.label

          # Determine the object
          obj = ''
          # String=value with capital letters
          if capital_letter_regex.match(value):
            obj = Literal(value, datatype=XSD.string)
          # Data time=value is a digit
          elif value.isdigit():
            obj = Literal(int(value), datatype=XSD.dateTime)
          # Data language=value is a language code
          elif value == "it" or value == "en-US" or value == "de":
            obj = Literal(value, datatype=XSD.language)
          # String URI=value is a URI
          elif http_regex.match(value):
              obj = Literal(value, datatype=XSD.anyURI)
          # if value contains ":", split it
          elif ":" in value:
            prefix, suffix = value.split(":")
            if prefix in namespaces:
              obj = URIRef(namespaces[prefix] + suffix)
            else:
              obj = URIRef(value)
          # Value corresponding to column
          elif key=="rdaw:P10218" or key=="rdaw:P30088":
              obj = URIRef(miro+"place/"+str(value))
          elif key=="lrmoo:R68i" or key=="lrmoo:R68" or key=="miro:evokes":
              obj = URIRef(miro+"work/"+str(value))
          elif key=="lrmoo:R3":
            obj = URIRef(miro+"expression/"+str(value))
          # Otherwise, value=URI
          else:
              obj = URIRef(miro+"agent/"+str(value))
          # Add triples
          g.add((subj, predicate, obj))

#CSV ITEM-E

# Open the CSV file and read it into a Dict
with open('/content/drive/MyDrive/Colab Notebooks/DEFINITIVO - item-e.csv', mode='r') as csv_file:
  csv_reader = csv.DictReader(csv_file)
  for row in csv_reader:
    for key in row.keys():
      value = row.get(key).strip()

      capital_letter_regex = re.compile(r'^[A-Z]')
      http_regex = re.compile(r'\bhttps?://\S+')

      # Add a triple that associates the first column's value in the row with the type of entity
      g.add((URIRef(miro + "expression/"+str(row.get(list(row.keys())[0]))), RDF.type, lrmoo.F2))

      # Skip the first column
      if key != list(row.keys())[0]:

        # Check if the value is not empty
        if value:

          # Subject of the URI
          subj = URIRef(miro+"expression/"+str(row.get("lrmoo:F2")))

          # Split the predicate in prefix and suffix
          column_split = str(key).split(":")
          prefix = column_split[0]
          suffix = column_split[1]

          # Create a Dict of the namespaces (key=prefix; uri=value)
          namespaces = {"miro":"https://w3id.org/miro/",
          "lrmoo" : "http://iflastandards.info/ns/lrm/lrmoo/",
          "rdaw" : "http://rdaregistry.info/Elements/w/",
          "rdae" : "http://rdaregistry.info/Elements/e/",
          "rdam": "http://rdaregistry.info/Elements/m/",
          "rdaco": "http://rdaregistry.info/termList/RDAContentType/",
          "owl" : "http://www.w3.org/TR/owl-ref/",
          "rdfs" : "http://www.w3.org/TR/rdf11-schema/",
          "crm" : "http://www.cidoc-crm.org/cidoc-crm/"}

          # Check if the prefix is in the Dict and create the predicate URI
          if prefix in namespaces:
            base_uri = namespaces[prefix]
            predicate = URIRef(base_uri+suffix)
            if prefix == "owl":
              predicate = OWL.sameAs
            if prefix == "rdfs":
              predicate = RDFS.label

          # Determine the object
          obj = ''
          # String=value with capital letters
          if capital_letter_regex.match(value):
            obj = Literal(value, datatype=XSD.string)
          # Data time=value is a digit
          elif value.isdigit():
            obj = Literal(int(value), datatype=XSD.dateTime)
          # Data language=value is a language code
          elif value == "it" or value == "en-US" or value == "de":
            obj = Literal(value, datatype=XSD.language)
          # String URI=value is a URI
          elif http_regex.match(value):
              obj = Literal(value, datatype=XSD.anyURI)
          # if value contains ":", split it
          elif ":" in value:
            prefix, suffix = value.split(":")
            if prefix in namespaces:
              obj = URIRef(namespaces[prefix] + suffix)
            else:
              obj = URIRef(value)
          # Value corresponding to column
          elif key=="lrmoo:R75" or  key=="crm:P65i":
            obj = URIRef(miro+"expression/"+str(value))
          elif key=="lrmoo:R4i":
            obj = URIRef(miro+"manifestation/"+str(value))
          # Otherwise, value=URI
          else:
              obj = URIRef(miro+"agent/"+str(value))
          g.add((subj, predicate, obj))

# CSV ITEM-M

# Open the CSV file and read it into a Dict
with open('/content/drive/MyDrive/Colab Notebooks/DEFINITIVO - item-m.csv', mode='r') as csv_file:
  csv_reader = csv.DictReader(csv_file)
  for row in csv_reader:
    for key in row.keys():
      value = row.get(key).strip()

      capital_letter_regex = re.compile(r'^[A-Z]')
      http_regex = re.compile(r'\bhttps?://\S+')

      # Add a triple that associates the first column's value in the row with the type of entity
      g.add((URIRef(miro + "manifestation/"+str(row.get(list(row.keys())[0]))), RDF.type, lrmoo.F3))

      # Skip the first key
      if key != list(row.keys())[0]:

        # Check if the value is not empty
        if value:

          # Subject of the URI
          subj = URIRef(miro+"manifestation/"+str(row.get("lrmoo:F3")))
          #subj = URIRef(miro + str(row.get(list(row.keys())[0])))

          # Split the predicate in prefix and suffix
          column_split = str(key).split(":")
          prefix = column_split[0]
          suffix = column_split[1]

          # Create a Dict of the namespaces (key=prefix; uri=value)
          namespaces = {"miro":"https://w3id.org/miro/",
          "lrmoo" : "http://iflastandards.info/ns/lrm/lrmoo/",
          "rdaw" : "http://rdaregistry.info/Elements/w/",
          "rdae" : "http://rdaregistry.info/Elements/e/",
          "rdam": "http://rdaregistry.info/Elements/m/",
          "rdaco": "http://rdaregistry.info/termList/RDAContentType/",
          "owl" : "http://www.w3.org/TR/owl-ref/",
          "rdfs" : "http://www.w3.org/TR/rdf11-schema/",
          "crm" : "http://www.cidoc-crm.org/cidoc-crm/"}

          # Check if the prefix is in the Dict and create the predicate URI
          if prefix in namespaces:
            base_uri = namespaces[prefix]
            predicate = URIRef(base_uri+suffix)
            if prefix == "owl":
              predicate = OWL.sameAs
            if prefix == "rdfs":
              predicate = RDFS.label

          # Determine the object
          obj = ''
          # String=value with capital letters
          if capital_letter_regex.match(value):
            obj = Literal(value, datatype=XSD.string)
          # Data time=value is a digit
          elif value.isdigit():
            obj = Literal(int(value), datatype=XSD.dateTime)
          # Data language=value is a language code
          elif value == "it" or value == "en-US" or value == "de":
            obj = Literal(value, datatype=XSD.language)
          # String URI=value is a URI
          elif http_regex.match(value):
              obj = Literal(value, datatype=XSD.anyURI)
          # if value contains ":", split it
          elif ":" in value:
            prefix, suffix = value.split(":")
            if prefix in namespaces:
              obj = URIRef(namespaces[prefix] + suffix)
            else:
              obj = URIRef(value)
          # Value corresponding to column
          elif key=="rdam:P30088":
              obj = URIRef(miro+"place/"+str(value))
          # Otherwise, value=URI
          else:
              obj = URIRef(miro+"agent/"+str(value))
          g.add((subj, predicate, obj))

#CSV INTERPRETATION-ACT

# Open the CSV file and read it into a Dict
with open('/content/drive/MyDrive/Colab Notebooks/DEFINITIVO - interpretationAct.csv', mode='r') as csv_file:
  csv_reader = csv.DictReader(csv_file)
  for row in csv_reader:
    for key in row.keys():
      value = row.get(key).strip()
      
      capital_letter_regex = re.compile(r'^[A-Z]')
      http_regex = re.compile(r'\bhttps?://\S+')

      # Add a triple that associates the first column's value in the row with the type of entity
      g.add((URIRef(miro + "interpretationAct/"+str(row.get(list(row.keys())[0]))), RDF.type, hico.InterpretationAct))

      # Skip the first key
      if key != list(row.keys())[0]:

        # Check if the value is not empty
        if value:

          # Subject of the URI
          subj = URIRef(miro+"interpretationAct/"+str(row.get("hico:InterpretationAct")))
          #subj = URIRef(miro + str(row.get(list(row.keys())[0])))

          # Split the predicate in prefix and suffix
          column_split = str(key).split(":")
          prefix = column_split[0]
          suffix = column_split[1]

          # Create a Dict of the namespaces (key=prefix; uri=value)
          namespaces = {"miro":"https://w3id.org/miro/",
          "lrmoo" : "http://iflastandards.info/ns/lrm/lrmoo/",
          "rdaw" : "http://rdaregistry.info/Elements/w/",
          "rdae" : "http://rdaregistry.info/Elements/e/",
          "rdam": "http://rdaregistry.info/Elements/m/",
          "rdaco": "http://rdaregistry.info/termList/RDAContentType/",
          "owl" : "http://www.w3.org/TR/owl-ref/",
          "rdfs" : "http://www.w3.org/TR/rdf11-schema/",
          "crm" : "http://www.cidoc-crm.org/cidoc-crm/",
          "hico": "http://purl.org/emmedi/hico",
          "cito" : "http://purl.org/spar/cito/",
          "prov": "http://www.w3.org/ns/prov#"}

          # Check if the prefix is in the Dict and create the predicate URI
          if prefix in namespaces:
            base_uri = namespaces[prefix]
            predicate = URIRef(base_uri+suffix)
            if prefix == "owl":
              predicate = OWL.sameAs
            if prefix == "rdfs":
              predicate = RDFS.label

          # Determine the object
          obj = ''
          # String=value with capital letters
          if capital_letter_regex.match(value):
            obj = Literal(value, datatype=XSD.string)
          # Data time=value is a digit
          elif value.isdigit():
            obj = Literal(int(value), datatype=XSD.dateTime)
          # Data language=value is a language code
          elif value == "it" or value == "en-US" or value == "de":
            obj = Literal(value, datatype=XSD.language)
          # String URI=value is a URI
          elif http_regex.match(value):
              obj = Literal(value, datatype=XSD.anyURI)
          # if value contains ":", split it
          elif ":" in value:
            prefix, suffix = value.split(":")
            if prefix in namespaces:
              obj = URIRef(namespaces[prefix] + suffix)
            else:
              obj = URIRef(value)
          # Value corresponding to column
          elif key=="hico:isExtractedFrom":
              obj = URIRef(miro+"publication/"+str(value))
          elif key=="hico:hasInterpretationCriterion":
              obj = URIRef(miro+"criterion/"+str(value))
          elif key=="hico:hasInterpretationType":
              obj = URIRef(miro+"type/"+str(value))
          elif key=="cito:disagreesWith":
              obj = URIRef(miro+"interpretationAct/"+str(value))
          elif key=="cito:agreesWith":
              obj = URIRef(miro+"interpretationAct/"+str(value))
          # Otherwise, value=URI
          else:
              obj = URIRef(miro+str(value))
          g.add((subj, predicate, obj))

#CSV TEXTUAL-REFERENCE

# Open the CSV file and read it into a Dict
with open('/content/drive/MyDrive/Colab Notebooks/DEFINITIVO - textual-reference.csv', mode='r') as csv_file:
  csv_reader = csv.DictReader(csv_file)
  for row in csv_reader:
    for key in row.keys():
      value = row.get(key).strip()

      ref_regex = re.compile(r'^[A-Z\[]')
      http_regex = re.compile(r'\bhttps?://\S+')

      # Add a triple that associates the first column's value in the row with the type of entity
      g.add((URIRef(miro + "reference/"+str(row.get(list(row.keys())[0]))), RDF.type, lrmoo.F2))

      # Skip the first key
      if key != list(row.keys())[0]:

        # Check if the value is not empty
        if value:

          # Subject of the URI
          subj = URIRef(miro+"reference/"+str(row.get("lrmoo:F2")))
          #subj = URIRef(miro + str(row.get(list(row.keys())[0])))

          # Split the predicate in prefix and suffix
          column_split = str(key).split(":")
          prefix = column_split[0]
          suffix = column_split[1]

          # Create a Dict of the namespaces (key=prefix; uri=value)
          namespaces = {"miro":"https://w3id.org/miro/",
          "lrmoo" : "http://iflastandards.info/ns/lrm/lrmoo/",
          "rdaw" : "http://rdaregistry.info/Elements/w/",
          "rdae" : "http://rdaregistry.info/Elements/e/",
          "rdam": "http://rdaregistry.info/Elements/m/",
          "rdaco": "http://rdaregistry.info/termList/RDAContentType/",
          "owl" : "http://www.w3.org/TR/owl-ref/",
          "rdfs" : "http://www.w3.org/TR/rdf11-schema/",
          "crm" : "http://www.cidoc-crm.org/cidoc-crm/",
          "hico": "http://purl.org/emmedi/hico",
          "cito" : "http://purl.org/spar/cito/",
          "prov": "http://www.w3.org/ns/prov#"}

          # Check if the prefix is in the Dict and create the predicate URI
          if prefix in namespaces:
            base_uri = namespaces[prefix]
            predicate = URIRef(base_uri+suffix)
            if prefix == "owl":
              predicate = OWL.sameAs
            if prefix == "rdfs":
              predicate = RDFS.label

          # Determine the object
          obj = ''
          # String URI=value is a URI
          if ref_regex.match(value):
            obj = Literal(value, datatype=XSD.string)
          # if value contains ":", split it
          elif ":" in value:
            prefix, suffix = value.split(":")
            if prefix in namespaces:
              obj = URIRef(namespaces[prefix] + suffix)
            else:
              obj = URIRef(value)
          # Otherwise, value=URI
          else:
              obj = URIRef(miro+str(value))
          g.add((subj, predicate, obj))

#CSV PUB-W

# Open the CSV file and read it into a Dict
with open('/content/drive/MyDrive/Colab Notebooks/DEFINITIVO - pub-w.csv', mode='r') as csv_file:
  csv_reader = csv.DictReader(csv_file)
  for row in csv_reader:
    for key in row.keys():
      value = row.get(key).strip()

      capital_letter_regex = re.compile(r'^[A-Z]')
      http_regex = re.compile(r'^http://')
      https_regex = re.compile(r'^https://')

      # Add a triple that associates the first column's value in the row with the type of entity
      g.add((URIRef(miro + "publication/"+str(row.get(list(row.keys())[0]))), RDF.type, lrmoo.F1))

      # Skip the first key
      if key != list(row.keys())[0]:

        # Check if the value is not empty
        if value:

          # Subject of the URI
          subj = URIRef(miro+"publication/"+str(row.get("lrmoo:F1")))
          #subj = URIRef(miro + str(row.get(list(row.keys())[0])))

          # Split the predicate in prefix and suffix
          column_split = str(key).split(":")
          prefix = column_split[0]
          suffix = column_split[1]

          # Create a Dict of the namespaces (key=prefix; uri=value)
          namespaces = {"miro":"https://w3id.org/miro/",
          "lrmoo" : "http://iflastandards.info/ns/lrm/lrmoo/",
          "rdaw" : "http://rdaregistry.info/Elements/w/",
          "rdae" : "http://rdaregistry.info/Elements/e/",
          "rdam": "http://rdaregistry.info/Elements/m/",
          "rdaco": "http://rdaregistry.info/termList/RDAContentType/",
          "owl" : "http://www.w3.org/TR/owl-ref/",
          "rdfs" : "http://www.w3.org/TR/rdf11-schema/",
          "crm" : "http://www.cidoc-crm.org/cidoc-crm/",
          "hico": "http://purl.org/emmedi/hico",
          "cito" : "http://purl.org/spar/cito/",
          "prov": "http://www.w3.org/ns/prov#"}

          # Check if the prefix is in the Dict and create the predicate URI
          if prefix in namespaces:
            base_uri = namespaces[prefix]
            predicate = URIRef(base_uri+suffix)
            if prefix == "owl":
              predicate = OWL.sameAs
            if prefix == "rdfs":
              predicate = RDFS.label

          # Determine the object
          obj = ''
          # String=value with capital letters
          if capital_letter_regex.match(value):
            obj = Literal(value, datatype=XSD.string)
          # Data time=value is a digit
          elif value.isdigit():
            obj = Literal(int(value), datatype=XSD.dateTime)
          # Data language=value is a language code
          elif value == "it" or value == "en-US" or value == "de":
            obj = Literal(value, datatype=XSD.language)
          # String URI=value is a URI
          elif http_regex.match(value) or https_regex.match(value):
              obj = Literal(value, datatype=XSD.anyURI)
          # if value contains ":", split it
          elif ":" in value:
            prefix, suffix = value.split(":")
            if prefix in namespaces:
              obj = URIRef(namespaces[prefix] + suffix)
            else:
              obj = URIRef(value)
          # Value corresponding to column
          elif key=="rdaw:P10065":
              obj = URIRef(miro+"agent/"+str(value))
          elif key=="lrmoo:R3":
              obj = URIRef(miro+"expression/"+str(value))
          # Otherwise, value=URI
          else:
              obj = URIRef(miro+str(value))
          g.add((subj, predicate, obj))

#CSV PUB-E

# Open the CSV file and read it into a Dict
with open('/content/drive/MyDrive/Colab Notebooks/DEFINITIVO - pub-e.csv', mode='r') as csv_file:
  csv_reader = csv.DictReader(csv_file)
  for row in csv_reader:
    for key in row.keys():
      value = row.get(key).strip()

      capital_letter_regex = re.compile(r'^[A-Z]')
      http_regex = re.compile(r'\bhttps?://\S+')

      # Add a triple that associates the first column's value in the row with the type of entity
      g.add((URIRef(miro + "publication/"+str(row.get(list(row.keys())[0]))), RDF.type, lrmoo.F2))

      # Skip the first key
      if key != list(row.keys())[0]:

        # Check if the value is not empty
        if value:

          # Subject of the URI
          subj = URIRef(miro+"publication/"+str(row.get("lrmoo:F2")))
          #subj = URIRef(miro + str(row.get(list(row.keys())[0])))

          # Split the predicate in prefix and suffix
          column_split = str(key).split(":")
          prefix = column_split[0]
          suffix = column_split[1]

          # Create a Dict of the namespaces (key=prefix; uri=value)
          namespaces = {"miro":"https://w3id.org/miro/",
          "lrmoo" : "http://iflastandards.info/ns/lrm/lrmoo/",
          "rdaw" : "http://rdaregistry.info/Elements/w/",
          "rdae" : "http://rdaregistry.info/Elements/e/",
          "rdam": "http://rdaregistry.info/Elements/m/",
          "rdaco": "http://rdaregistry.info/termList/RDAContentType/",
          "owl" : "http://www.w3.org/TR/owl-ref/",
          "rdfs" : "http://www.w3.org/TR/rdf11-schema/",
          "crm" : "http://www.cidoc-crm.org/cidoc-crm/",
          "hico": "http://purl.org/emmedi/hico",
          "cito" : "http://purl.org/spar/cito/",
          "prov": "http://www.w3.org/ns/prov#"}

          # Check if the prefix is in the Dict and create the predicate URI
          if prefix in namespaces:
            base_uri = namespaces[prefix]
            predicate = URIRef(base_uri+suffix)
            if prefix == "owl":
              predicate = OWL.sameAs
            if prefix == "rdfs":
              predicate = RDFS.label

          # Determine the object
          obj = ''
          # String=value with capital letters
          if capital_letter_regex.match(value):
            obj = Literal(value, datatype=XSD.string)
          # Data time=value is a digit
          elif value.isdigit():
            obj = Literal(int(value), datatype=XSD.dateTime)
          # Data language=value is a language code
          elif value == "it" or value == "en-US" or value == "de":
            obj = Literal(value, datatype=XSD.language)
          # String URI=value is a URI
          elif http_regex.match(value):
              obj = Literal(value, datatype=XSD.anyURI)
          # if value contains ":", split it
          elif ":" in value:
            prefix, suffix = value.split(":")
            if prefix in namespaces:
              obj = URIRef(namespaces[prefix] + suffix)
            else:
              obj = URIRef(value)
          # Value corresponding to column
          elif key=="rdaw:P10065":
              obj = URIRef(miro+"agent/"+str(value))
          elif key=="crm:P148":
              obj = URIRef(miro+"expression/"+str(value))    
          elif key=="lrmoo:R3":
              obj = URIRef(miro+"expression/"+str(value))
          elif key=="lrmoo:R4i":
              obj = URIRef(miro+"manifestation/"+str(value))
          # Otherwise, value=URI
          else:
              obj = URIRef(miro+str(value))
          g.add((subj, predicate, obj))

#CSV PUB-M

# Open the CSV file and read it into a Dict
with open('/content/drive/MyDrive/Colab Notebooks/DEFINITIVO - pub-m.csv', mode='r') as csv_file:
  csv_reader = csv.DictReader(csv_file)
  for row in csv_reader:
    for key in row.keys():
      value = row.get(key).strip()

      capital_letter_regex = re.compile(r'^[A-Z]')
      http_regex = re.compile(r'\bhttps?://\S+')

      # Add a triple that associates the first column's value in the row with the type of entity
      g.add((URIRef(miro + "publication/"+str(row.get(list(row.keys())[0]))), RDF.type, lrmoo.F3))

      # Skip the first key
      if key != list(row.keys())[0]:

        # Check if the value is not empty
        if value:

          # Subject of the URI
          subj = URIRef(miro+"publication/"+str(row.get("lrmoo:F3")))
          #subj = URIRef(miro + str(row.get(list(row.keys())[0])))

          # Split the predicate in prefix and suffix
          column_split = str(key).split(":")
          prefix = column_split[0]
          suffix = column_split[1]

          # Create a Dict of the namespaces (key=prefix; uri=value)
          namespaces = {"miro":"https://w3id.org/miro/",
          "lrmoo" : "http://iflastandards.info/ns/lrm/lrmoo/",
          "rdaw" : "http://rdaregistry.info/Elements/w/",
          "rdae" : "http://rdaregistry.info/Elements/e/",
          "rdam": "http://rdaregistry.info/Elements/m/",
          "rdaco": "http://rdaregistry.info/termList/RDAContentType/",
          "owl" : "http://www.w3.org/TR/owl-ref/",
          "rdfs" : "http://www.w3.org/TR/rdf11-schema/",
          "crm" : "http://www.cidoc-crm.org/cidoc-crm/",
          "hico": "http://purl.org/emmedi/hico",
          "cito" : "http://purl.org/spar/cito/",
          "prov": "http://www.w3.org/ns/prov#"}

          # Check if the prefix is in the Dict and create the predicate URI
          if prefix in namespaces:
            base_uri = namespaces[prefix]
            predicate = URIRef(base_uri+suffix)
            if prefix == "owl":
              predicate = OWL.sameAs
            if prefix == "rdfs":
              predicate = RDFS.label

          # Determine the object
          obj = ''
          # String=value with capital letters
          if capital_letter_regex.match(value):
            obj = Literal(value, datatype=XSD.string)
          # Data time=value is a digit
          elif value.isdigit():
            obj = Literal(int(value), datatype=XSD.dateTime)
          # Data language=value is a language code
          elif value == "it" or value == "en-US" or value == "de":
            obj = Literal(value, datatype=XSD.language)
          # String URI=value is a URI
          elif http_regex.match(value):
              obj = Literal(value, datatype=XSD.anyURI)
          # if value contains ":", split it
          elif ":" in value:
            prefix, suffix = value.split(":")
            if prefix in namespaces:
              obj = URIRef(namespaces[prefix] + suffix)
            else:
              obj = URIRef(value)
          # Value corresponding to column
          elif key=="rdam:P30083":
              obj = URIRef(miro+"agent/"+str(value))
          elif key=="rdam:P30088":
              obj = URIRef(miro+"place/"+str(value))
          # Otherwise, value=URI
          else:
              obj = URIRef(miro+str(value))
          g.add((subj, predicate, obj))

#CSV EKPH RELATION

# Open the CSV file and read it into a Dict
with open('/content/drive/MyDrive/Colab Notebooks/DEFINITIVO - relations-ekph.csv', mode='r') as csv_file:
  csv_reader = csv.DictReader(csv_file)
  for row in csv_reader:
    for key in row.keys():
      value = row.get(key).strip()

      capital_letter_regex = re.compile(r'^[A-Z]')
      http_regex = re.compile(r'\bhttps?://\S+')

      # Add a triple that associates the first column's value in the row with the type of entity
      g.add((URIRef(miro + "EkphrasticRelation/"+str(row.get(list(row.keys())[0]))), RDF.type, miro.EkphrasticRelation))

      # Skip the first key
      if key != list(row.keys())[0]:

        # Check if the value is not empty
        if value:

          # Subject of the URI
          subj = URIRef(miro+"EkphrasticRelation/"+str(row.get("miro:EkphrasticRelation")))
          #subj = URIRef(miro + str(row.get(list(row.keys())[0])))

          # Split the predicate in prefix and suffix
          column_split = str(key).split(":")
          prefix = column_split[0]
          suffix = column_split[1]

          # Create a Dict of the namespaces (key=prefix; uri=value)
          namespaces = {"miro":"https://w3id.org/miro/",
          "lrmoo" : "http://iflastandards.info/ns/lrm/lrmoo/",
          "rdaw" : "http://rdaregistry.info/Elements/w/",
          "rdae" : "http://rdaregistry.info/Elements/e/",
          "rdam": "http://rdaregistry.info/Elements/m/",
          "rdaco": "http://rdaregistry.info/termList/RDAContentType/",
          "owl" : "http://www.w3.org/TR/owl-ref/",
          "rdfs" : "http://www.w3.org/TR/rdf11-schema/",
          "crm" : "http://www.cidoc-crm.org/cidoc-crm/",
          "hico": "http://purl.org/emmedi/hico",
          "cito" : "http://purl.org/spar/cito/",
          "prov": "http://www.w3.org/ns/prov#"}

          # Check if the prefix is in the Dict and create the predicate URI
          if prefix in namespaces:
            base_uri = namespaces[prefix]
            predicate = URIRef(base_uri+suffix)
            if prefix == "owl":
              predicate = OWL.sameAs
            if prefix == "rdfs":
              predicate = RDFS.label

          # Determine the object
          obj = ''
          # String=value with capital letters
          if capital_letter_regex.match(value):
            obj = Literal(value, datatype=XSD.string)
          # Data time=value is a digit
          elif value.isdigit():
            obj = Literal(int(value), datatype=XSD.dateTime)
          # Data language=value is a language code
          elif value == "it" or value == "en-US" or value == "de":
            obj = Literal(value, datatype=XSD.language)
          # String URI=value is a URI
          elif http_regex.match(value):
              obj = Literal(value, datatype=XSD.anyURI)
          # if value contains ":", split it
          elif ":" in value:
            prefix, suffix = value.split(":")
            if prefix in namespaces:
              obj = URIRef(namespaces[prefix] + suffix)
            else:
              obj = URIRef(value)
          # Value corresponding to column
          elif key=="miro:hasMediumA":
              obj = URIRef(miro+"expression/"+str(value))
          elif key=="miro:hasMediumB":
              obj = URIRef(miro+"expression/"+str(value))
          elif key=="miro:hasFeature":
              obj = Literal(value, datatype=XSD.string)
          elif key=="prov:wasGeneratedBy":
              obj = URIRef(miro+"interpretationAct/"+str(value))
          # Otherwise, value=URI
          else:
              obj = URIRef(miro+str(value))
          g.add((subj, predicate, obj))

#CSV SUB-OB EKPH

# Open the CSV file and read it into a Dict
with open('/content/drive/MyDrive/Colab Notebooks/DEFINITIVO - sub-ob-epk.csv', mode='r') as csv_file:
  csv_reader = csv.DictReader(csv_file)
  for row in csv_reader:
    for key in row.keys():
      value = row.get(key).strip()

      capital_letter_regex = re.compile(r'^[A-Z]')
      http_regex = re.compile(r'\bhttps?://\S+')

      # Add a triple that associates the first column's value in the row with the type of entity
      g.add((URIRef(miro + "expression/"+str(row.get(list(row.keys())[0]))), RDF.type, lrmoo.F2))

      # Skip the first key
      if key != list(row.keys())[0]:

        # Check if the value is not empty
        if value:

          # Subject of the URI
          subj = URIRef(miro+"expression/"+str(row.get("lrmoo:F2")))
          #subj = URIRef(miro + str(row.get(list(row.keys())[0])))

          # Split the predicate in prefix and suffix
          column_split = str(key).split(":")
          prefix = column_split[0]
          suffix = column_split[1]

          # Create a Dict of the namespaces (key=prefix; uri=value)
          namespaces = {"miro":"https://w3id.org/miro/",
          "lrmoo" : "http://iflastandards.info/ns/lrm/lrmoo/",
          "rdaw" : "http://rdaregistry.info/Elements/w/",
          "rdae" : "http://rdaregistry.info/Elements/e/",
          "rdam": "http://rdaregistry.info/Elements/m/",
          "rdaco": "http://rdaregistry.info/termList/RDAContentType/",
          "owl" : "http://www.w3.org/TR/owl-ref/",
          "rdfs" : "http://www.w3.org/TR/rdf11-schema/",
          "crm" : "http://www.cidoc-crm.org/cidoc-crm/",
          "hico": "http://purl.org/emmedi/hico",
          "cito" : "http://purl.org/spar/cito/",
          "prov": "http://www.w3.org/ns/prov#"}

          # Check if the prefix is in the Dict and create the predicate URI
          if prefix in namespaces:
            base_uri = namespaces[prefix]
            predicate = URIRef(base_uri+suffix)
            if prefix == "owl":
              predicate = OWL.sameAs
            if prefix == "rdfs":
              predicate = RDFS.label

          # Determine the object
          obj = ''
          # String=value with capital letters
          if capital_letter_regex.match(value):
            obj = Literal(value, datatype=XSD.string)
          # Data time=value is a digit
          elif value.isdigit():
            obj = Literal(int(value), datatype=XSD.dateTime)
          # Data language=value is a language code
          elif value == "it" or value == "en-US" or value == "de":
            obj = Literal(value, datatype=XSD.language)
           # String URI=value is a URI
          elif http_regex.match(value):
              obj = Literal(value, datatype=XSD.anyURI)
          # if value contains ":", split it
          elif ":" in value:
            prefix, suffix = value.split(":")
            if prefix in namespaces:
              obj = URIRef(namespaces[prefix] + suffix)
            else:
              obj = URIRef(value)
          # Otherwise, value=URI
          else:
              obj = URIRef(miro+"expression/"+str(value))
          g.add((subj, predicate, obj))

# CSV MEDIA COMBINATION

# Open the CSV file and read it into a Dict
with open('/content/drive/MyDrive/Colab Notebooks/DEFINITIVO - mediacombination.csv', mode='r') as csv_file:
  csv_reader = csv.DictReader(csv_file)
  for row in csv_reader:
    for key in row.keys():
      value = row.get(key).strip()

      capital_letter_regex = re.compile(r'^[A-Z]')
      http_regex = re.compile(r'\bhttps?://\S+')

      # Add a triple that associates the first column's value in the row with the type of entity
      g.add((URIRef(miro + "MediaCombination/"+str(row.get(list(row.keys())[0]))), RDF.type, miro.MediaCombination))

      # Skip the first key
      if key != list(row.keys())[0]:

        # Check if the value is not empty
        if value:

          # Subject of the URI
          subj = URIRef(miro+"MediaCombination/"+str(row.get("miro:MediaCombination")))
          #subj = URIRef(miro + str(row.get(list(row.keys())[0])))

          # Split the predicate in prefix and suffix
          column_split = str(key).split(":")
          prefix = column_split[0]
          suffix = column_split[1]

          # Create a Dict of the namespaces (key=prefix; uri=value)
          namespaces = {"miro":"https://w3id.org/miro/",
          "lrmoo" : "http://iflastandards.info/ns/lrm/lrmoo/",
          "rdaw" : "http://rdaregistry.info/Elements/w/",
          "rdae" : "http://rdaregistry.info/Elements/e/",
          "rdam": "http://rdaregistry.info/Elements/m/",
          "rdaco": "http://rdaregistry.info/termList/RDAContentType/",
          "owl" : "http://www.w3.org/TR/owl-ref/",
          "rdfs" : "http://www.w3.org/TR/rdf11-schema/",
          "crm" : "http://www.cidoc-crm.org/cidoc-crm/",
          "hico": "http://purl.org/emmedi/hico",
          "cito" : "http://purl.org/spar/cito/",
          "prov": "http://www.w3.org/ns/prov#"}

          # Check if the prefix is in the Dict and create the predicate URI
          if prefix in namespaces:
            base_uri = namespaces[prefix]
            predicate = URIRef(base_uri+suffix)
            if prefix == "owl":
              predicate = OWL.sameAs
            if prefix == "rdfs":
              predicate = RDFS.label

          # Determine the object
          obj = ''
          # String=value with capital letters
          if capital_letter_regex.match(value):
            obj = Literal(value, datatype=XSD.string)
          # Data time=value is a digit
          elif value.isdigit():
            obj = Literal(int(value), datatype=XSD.dateTime)
          # Data language=value is a language code
          elif value == "it" or value == "en-US" or value == "de":
            obj = Literal(value, datatype=XSD.language)
           # String URI=value is a URI
          elif http_regex.match(value):
              obj = Literal(value, datatype=XSD.anyURI)
          # if value contains ":", split it
          elif ":" in value:
            prefix, suffix = value.split(":")
            if prefix in namespaces:
              obj = URIRef(namespaces[prefix] + suffix)
            else:
              obj = URIRef(value)
          # Value corresponding to column
          elif key=="miro:hasMediumA":
              obj = URIRef(miro+"expression/"+str(value))
          elif key=="miro:hasMediumB":
              obj = URIRef(miro+"expression/"+str(value))
          elif key=="prov:wasGeneratedBy":
              obj = URIRef(miro+"interpretationAct/"+str(value))
          # Otherwise, value=URI
          else:
              obj = URIRef(miro+str(value))
          g.add((subj, predicate, obj))

# CSV MEDIA TRANSPOSITION

# Open the CSV file and read it into a Dict
with open('/content/drive/MyDrive/Colab Notebooks/DEFINITIVO - mediatrasposition.csv', mode='r') as csv_file:
  csv_reader = csv.DictReader(csv_file)
  for row in csv_reader:
    for key in row.keys():
      value = row.get(key).strip()

      capital_letter_regex = re.compile(r'^[A-Z]')
      http_regex = re.compile(r'\bhttps?://\S+')

      # Add a triple that associates the first column's value in the row with the type of entity
      g.add((URIRef(miro + "MediaTrasposition/"+str(row.get(list(row.keys())[0]))), RDF.type, miro.MediaTrasposition))

      # Skip the first key
      if key != list(row.keys())[0]:

        # Check if the value is not empty
        if value:

          # Subject of the URI
          subj = URIRef(miro+"MediaTrasposition/"+str(row.get("miro:MediaTrasposition")))
          #subj = URIRef(miro + str(row.get(list(row.keys())[0])))

          # Split the predicate in prefix and suffix
          column_split = str(key).split(":")
          prefix = column_split[0]
          suffix = column_split[1]

          # Create a Dict of the namespaces (key=prefix; uri=value)
          namespaces = {"miro":"https://w3id.org/miro/",
          "lrmoo" : "http://iflastandards.info/ns/lrm/lrmoo/",
          "rdaw" : "http://rdaregistry.info/Elements/w/",
          "rdae" : "http://rdaregistry.info/Elements/e/",
          "rdam": "http://rdaregistry.info/Elements/m/",
          "rdaco": "http://rdaregistry.info/termList/RDAContentType/",
          "owl" : "http://www.w3.org/TR/owl-ref/",
          "rdfs" : "http://www.w3.org/TR/rdf11-schema/",
          "crm" : "http://www.cidoc-crm.org/cidoc-crm/",
          "hico": "http://purl.org/emmedi/hico",
          "cito" : "http://purl.org/spar/cito/",
          "prov": "http://www.w3.org/ns/prov#"}

          # Check if the prefix is in the Dict and create the predicate URI
          if prefix in namespaces:
            base_uri = namespaces[prefix]
            predicate = URIRef(base_uri+suffix)
            if prefix == "owl":
              predicate = OWL.sameAs
            if prefix == "rdfs":
              predicate = RDFS.label

          # Determine the object
          obj = ''
          # String=value with capital letters
          if capital_letter_regex.match(value):
            obj = Literal(value, datatype=XSD.string)
          # Data time=value is a digit
          elif value.isdigit():
            obj = Literal(int(value), datatype=XSD.dateTime)
          # Data language=value is a language code
          elif value == "it" or value == "en-US" or value == "de":
            obj = Literal(value, datatype=XSD.language)
           # String URI=value is a URI
          elif http_regex.match(value):
              obj = Literal(value, datatype=XSD.anyURI)
          # if value contains ":", split it
          elif ":" in value:
            prefix, suffix = value.split(":")
            if prefix in namespaces:
              obj = URIRef(namespaces[prefix] + suffix)
            else:
              obj = URIRef(value)
          # Value corresponding to column
          elif key=="miro:hasMediumA":
              obj = URIRef(miro+"expression/"+str(value))
          elif key=="miro:hasMediumB":
              obj = URIRef(miro+"expression/"+str(value))
          elif key=="prov:wasGeneratedBy":
              obj = URIRef(miro+"interpretationAct/"+str(value))
          # Otherwise, value=URI
          else:
              obj = URIRef(miro+str(value))
          g.add((subj, predicate, obj))

# CSV MEDIA REFERENCE

# Open the CSV file and read it into a Dict
with open('/content/drive/MyDrive/Colab Notebooks/DEFINITIVO - mediareference.csv', mode='r') as csv_file:
  csv_reader = csv.DictReader(csv_file)
  for row in csv_reader:
    for key in row.keys():
      value = row.get(key).strip()

      capital_letter_regex = re.compile(r'^[A-Z]')
      http_regex = re.compile(r'\bhttps?://\S+')

      # Add a triple that associates the first column's value in the row with the type of entity
      g.add((URIRef(miro + "MediaReference/"+str(row.get(list(row.keys())[0]))), RDF.type, miro.MediaReference))

      # Skip the first key
      if key != list(row.keys())[0]:

        # Check if the value is not empty
        if value:

          # Subject of the URI
          subj = URIRef(miro+"MediaReference/"+str(row.get("miro:MediaReference")))
          #subj = URIRef(miro + str(row.get(list(row.keys())[0])))

          # Split the predicate in prefix and suffix
          column_split = str(key).split(":")
          prefix = column_split[0]
          suffix = column_split[1]

          # Create a Dict of the namespaces (key=prefix; uri=value)
          namespaces = {"miro":"https://w3id.org/miro/",
          "lrmoo" : "http://iflastandards.info/ns/lrm/lrmoo/",
          "rdaw" : "http://rdaregistry.info/Elements/w/",
          "rdae" : "http://rdaregistry.info/Elements/e/",
          "rdam": "http://rdaregistry.info/Elements/m/",
          "rdaco": "http://rdaregistry.info/termList/RDAContentType/",
          "owl" : "http://www.w3.org/TR/owl-ref/",
          "rdfs" : "http://www.w3.org/TR/rdf11-schema/",
          "crm" : "http://www.cidoc-crm.org/cidoc-crm/",
          "hico": "http://purl.org/emmedi/hico",
          "cito" : "http://purl.org/spar/cito/",
          "prov": "http://www.w3.org/ns/prov#"}

          # Check if the prefix is in the Dict and create the predicate URI
          if prefix in namespaces:
            base_uri = namespaces[prefix]
            predicate = URIRef(base_uri+suffix)
            if prefix == "owl":
              predicate = OWL.sameAs
            if prefix == "rdfs":
              predicate = RDFS.label

          # Determine the object
          obj = ''
          # String=value with capital letters
          if capital_letter_regex.match(value):
            obj = Literal(value, datatype=XSD.string)
          # Data time=value is a digit
          elif value.isdigit():
            obj = Literal(int(value), datatype=XSD.dateTime)
          # Data language=value is a language code
          elif value == "it" or value == "en-US" or value == "de":
            obj = Literal(value, datatype=XSD.language)
           # String URI=value is a URI
          elif http_regex.match(value):
              obj = Literal(value, datatype=XSD.anyURI)
          # if value contains ":", split it
          elif ":" in value:
            prefix, suffix = value.split(":")
            if prefix in namespaces:
              obj = URIRef(namespaces[prefix] + suffix)
            else:
              obj = URIRef(value)
          # Value corresponding to column
          elif key=="miro:hasMediumA":
              obj = URIRef(miro+"expression/"+str(value))
          elif key=="miro:hasMediumB":
              obj = URIRef(miro+"expression/"+str(value))
          elif key=="prov:wasGeneratedBy":
              obj = URIRef(miro+"interpretationAct/"+str(value))
          # Otherwise, value=URI
          else:
              obj = URIRef(miro+str(value))
          g.add((subj, predicate, obj))

# CSV AUTHORITY CONTROL AGENTS

# Open the CSV file and read it into a Dict
with open('/content/drive/MyDrive/Colab Notebooks/DEFINITIVO - authority file-agent.csv', mode='r') as csv_file:
  csv_reader = csv.DictReader(csv_file)
  # Iterate through each row
  for row in csv_reader:
    for key in row.keys():
      # Retrieves the value of the current key and removes whitespaces
      value = row.get(key).strip()

      # Reg ex for capital letters
      capital_letter_regex = re.compile(r'^[A-Z]')
      http_regex = re.compile(r'^http://')
      https_regex = re.compile(r'^https://')

      # Add a triple that associates the first column's value in the row with the crm:E39 type
      g.add((URIRef(miro + "agent/" + str(row.get(list(row.keys())[0]))), RDF.type, crm.E39))

      # Skip the first key
      if key != list(row.keys())[0]:

        # Check if the value is not empty
        if value:

          # Subject of the URI
          subj = URIRef(miro+"agent/"+str(row.get("crm:E39")))
          #subj = URIRef(miro + str(row.get(list(row.keys())[0])))

          # Split the predicate in prefix and suffix
          column_split = str(key).split(":")
          prefix = column_split[0]
          suffix = column_split[1]

          # Create a Dict of the namespaces (key=prefix; uri=value)
          namespaces = {"miro":"https://w3id.org/miro/",
          "lrmoo" : "http://iflastandards.info/ns/lrm/lrmoo/",
          "rdaw" : "http://rdaregistry.info/Elements/w/",
          "rdae" : "http://rdaregistry.info/Elements/e/",
          "rdam": "http://rdaregistry.info/Elements/m/",
          "rdaco": "http://rdaregistry.info/termList/RDAContentType/",
          "owl" : "http://www.w3.org/TR/owl-ref/",
          "rdfs" : "http://www.w3.org/TR/rdf11-schema/",
          "crm" : "http://www.cidoc-crm.org/cidoc-crm/"}

          # Check if the prefix is in the Dict and create the predicate URI
          if prefix in namespaces:
            base_uri = namespaces[prefix]
            predicate = URIRef(base_uri+suffix)
            if prefix == "owl":
              predicate = OWL.sameAs
            if prefix == "rdfs":
              predicate = RDFS.label

          # Determine the object
          obj = ''

          # String=value with capital letters
          if capital_letter_regex.match(value):
            obj = Literal(value, datatype=XSD.string)
          # Data time=value is a digit
          elif value.isdigit():
            obj = Literal(int(value), datatype=XSD.dateTime)
          # Data language=value is a language code
          elif value == "it" or value == "en-US" or value == "de":
            obj = Literal(value, datatype=XSD.language)
           # String URI=value is a URI
          elif https_regex.match(value) or http_regex.match(value):
              obj = Literal(value, datatype=XSD.anyURI)
          else:
            # Otherwise, value=URI
            obj = URIRef(miro+str(value))

          # Add triples
          g.add((subj, predicate, obj))

# CSV AUTHORITY CONTROL PLACES

# Open the CSV file and read it into a Dict
with open('/content/drive/MyDrive/Colab Notebooks/DEFINITIVO - authority file-places.csv', mode='r') as csv_file:
  csv_reader = csv.DictReader(csv_file)
  # Iterate through each row
  for row in csv_reader:
    for key in row.keys():
      # Retrieves the value of the current key and removes whitespaces
      value = row.get(key).strip()

      # Reg ex for capital letters
      capital_letter_regex = re.compile(r'^[A-Z]')
      http_regex = re.compile(r'^http://')
      https_regex = re.compile(r'^https://')

      # Add a triple that associates the first column's value in the row with the crm:E53 type
      g.add((URIRef(miro + "place/" + str(row.get(list(row.keys())[0]))), RDF.type, crm.E53))

      # Skip the first key
      if key != list(row.keys())[0]:

        # Check if the value is not empty
        if value:

          # Subject of the URI
          subj = URIRef(miro+"place/"+str(row.get("crm:E53")))
          #subj = URIRef(miro + str(row.get(list(row.keys())[0])))

          # Split the predicate in prefix and suffix
          column_split = str(key).split(":")
          prefix = column_split[0]
          suffix = column_split[1]

          # Create a Dict of the namespaces (key=prefix; uri=value)
          namespaces = {"miro":"https://w3id.org/miro/",
          "lrmoo" : "http://iflastandards.info/ns/lrm/lrmoo/",
          "rdaw" : "http://rdaregistry.info/Elements/w/",
          "rdae" : "http://rdaregistry.info/Elements/e/",
          "rdam": "http://rdaregistry.info/Elements/m/",
          "rdaco": "http://rdaregistry.info/termList/RDAContentType/",
          "owl" : "http://www.w3.org/TR/owl-ref/",
          "rdfs" : "http://www.w3.org/TR/rdf11-schema/",
          "crm" : "http://www.cidoc-crm.org/cidoc-crm/"}

          # Check if the prefix is in the Dict and create the predicate URI
          if prefix in namespaces:
            base_uri = namespaces[prefix]
            predicate = URIRef(base_uri+suffix)
            if prefix == "owl":
              predicate = OWL.sameAs
            if prefix == "rdfs":
              predicate = RDFS.label

          # Determine the object
          obj = ''

          # String=value with capital letters
          if capital_letter_regex.match(value):
            obj = Literal(value, datatype=XSD.string)
          # Data time=value is a digit
          elif value.isdigit():
            obj = Literal(int(value), datatype=XSD.dateTime)
          # Data language=value is a language code
          elif value == "it" or value == "en-US" or value == "de":
            obj = Literal(value, datatype=XSD.language)
           # String URI=value is a URI
          elif https_regex.match(value) or http_regex.match(value):
              obj = Literal(value, datatype=XSD.anyURI)
          else:
            # Otherwise, value=URI
            obj = URIRef(miro+str(value))

          # Add triples
          g.add((subj, predicate, obj))


# Serialize the graph to a TTL file
g.serialize(destination="gdo.ttl", format="ttl")

# Optionally, print the triples in the graph for verification
#for s, p, o in g.triples((None, None, None)):
    #print(s, p, o)
