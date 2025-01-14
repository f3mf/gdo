# Introduction

Linked Open Data (LOD) for Galleries, Libraries, Archives and Museums.
Machine-readable literary criticism in the age of semantic libraries.

Un progetto che sfrutta le potenzialità del web semantico per tradurre in Linked Open Data i principali contributi di critica letteraria su un'opera letteraria, descritta

## State-of-the-art

## Workflow

Il punto di partenza della modellazione è lo studio e la descrizione del dominio. Per noi, ciò è stato rappresentato da un'indagine bibliograifca sui contributi 

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

### Zero overhead
Lean and expressive ontology design

### Integrazione dello spoglio analitico delle risorse nella metadatazione

## Challanges

### Trovare fonti affidabili per opere contemporanee

### Automating data collection

### Integrating metadata standards

### Aligning event-centered and resource-centered ontologies

### Limitations of OWL DL