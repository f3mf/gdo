# Introduction

Linked Open Data (LOD) for Galleries, Libraries, Archives and Museums.
Machine-readable literary criticism in the age of semantic libraries.

## State-of-the-art

## Workflow

<style>
  [data-md-color-scheme="default"] {
    --md-mermaid-label-bg-color: #EDEDED;
  }

  [data-md-color-scheme="slate"] {
    --md-mermaid-label-bg-color: #363941;
  }
</style>

``` mermaid
flowchart TB
  Domain[Study of the domain]
  Items[Item selection]
  Mining[Metadata mining]
  Ideation[Ideation]
  Records@{ shape: documents, label: "Metadata records" }

  subgraph Knowledge Organization
    Formalization[Formalization]
    Analysis[Metadata analysis]
    Mapping[Mapping]
    Interpretation[Data interpretation]
    Ontology[Ontology design]
    Map([Conceptual map])
    ER([E/R model])
    Theoretical([Theoretical model])
    Conceptual{{Conceptual model}}
  end

  subgraph Knowledge Representation
    Description[Item description]
    Reconciliation[Entity reconciliation]
    RDF@{ shape: processes, label: "RDF Production" }
    Graph[(Knowledge graph)]
  end

  Domain --> Items
  Domain --> Ideation
  Ideation ---> Formalization
  Formalization --> Map
  Formalization --> ER
  Formalization ---> Interpretation
  Items --> Mining
  Items --> Map
  Mining --> Analysis
  Mining --> Records
  Analysis --> Mapping
  Mapping --> Interpretation
  Interpretation --> Ontology
  Interpretation --> Theoretical
  Interpretation -.->|enrichment| ER
  Ontology --> Conceptual

  Records ----> Description
  Conceptual --> Description
  Description --> Reconciliation
  Reconciliation --> RDF
  RDF --> Graph

```

## Goals

### Scalable modeling

### Lean and expressive ontology design

## Challanges

### Automating data collection

### Integrating metadata standards

### Aligning event-centered and resource-centered ontologies

### Limitations of OWL DL