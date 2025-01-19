# Introduction

## State-of-the-art

## Workflow

The starting point of modelling is the study and description of the chosen domain. For us, this was represented by a bibliographic survey of critical contributions that investigated the varied relationships established by the novel at the center of our research with other works of art.

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
    Conceptual([Conceptual map])
    ER([E/R model])
    Theoretical([Theoretical model])
    Formal{{Formal model}}
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
  Formalization --> Conceptual
  Formalization --> ER
  Formalization ---> Interpretation
  Items --> Mining
  Items --> Conceptual
  Mining --> Analysis
  Mining --> Records
  Analysis --> Mapping
  Mapping --> Interpretation
  Interpretation --> Ontology
  Interpretation --> Theoretical
  Interpretation -.->|enrichment| ER
  Ontology --> Formal

  Records ----> Description
  Formal --> Description
  Description --> Reconciliation
  Reconciliation --> RDF
  RDF --> Graph

```

## Goals

### Focus on competency questions

### Lean and expressive ontology design

### Analytical perusal of resources

## Challanges

### Automating data collection

### Reliability of contemporary artworks information

### Integrating metadata standards

### Aligning event-centered and resource-centered ontologies

### Limitations of OWL DL