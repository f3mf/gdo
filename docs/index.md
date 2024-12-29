# Introduction

Linked Open Data (LOD) for Galleries, Libraries, Archives and Museums.
Machine-readable literary criticism in the age of semantic libraries.

## State-of-the-art

## Workflow

``` mermaid
flowchart TB
  D[Study of the domain]
  IS[Item selection]
  MM[Metadata mining]
  I[Ideation]
  m[(Metadata)]

  subgraph Knowledge Organization
    C[Conception]
    MA[Metadata analysis]
    M[Mapping]
    DI[Data interpretation]
    OD[Ontology design]
    CM([Conceptual map])
    ER([E/R model])
    TM([Theoretical model])
    CMo{{Conceptual model}}
  end

  subgraph Knowledge Representation
    ID[Item description]
    NR[Name reconciliation]
    RDF@{ shape: processes, label: "RDF Production" }
    f[(Knowledge graph)]
  end

  D --> IS
  D --> I
  I ---> C
  C --> CM
  C --> ER
  C ---> DI
  IS --> MM
  IS --> CM
  MM --> MA
  MM --> m
  MA --> M
  M --> DI
  DI --> OD
  DI --> TM
  DI -.->|enrich| ER
  OD --> CMo

  m ----> ID
  CMo --> ID
  ID --> NR
  NR --> RDF
  RDF --> f

```

## Goals

### Scalable modeling

### Lean and expressive ontology design

## Challanges

### Automating data collection

### Integrating metadata standards

### Aligning event-centered and resource-centered ontologies

### Limitations of OWL DL