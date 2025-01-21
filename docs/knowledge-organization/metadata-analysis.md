# Metadata mining and analysis

In this section we will review the employed methods for metadata collection and analysis, not claiming to be exhaustive because they depends on the cases we encountered.

A good starting point to get an idea of the available data is the [Open GLAM Survey](https://docs.google.com/spreadsheets/d/1WPS-KJptUJ-o8SXtg00llcxq0IKJu8eO6Ege_GrLaNc/htmlview), an ongoing project that documents open access policies in the GLAM (Galleries, Libraries, Archives, and Museums) sector. It includes a spreadsheet that catalogs metadata sources and the associated license.

## Leveraging APIs

Having access to metadata in its raw form, typically a JSON file outputted from a server or a bibliographic record, can offer great insights into its underlying structure, the descriptive fields used, and additional information beyond that visible on online collection websites.

Some collection management software offers compatibility with the [Open Archives Initiative Protocol for Metadata Harvesting](https://www.openarchives.org/pmh/) (OAI-PMH), a protocol that enables repositories to expose their metadata in a standardized way for aggregation purposes. It relies on Dublin Core as a lingua franca of exchange, with the drawback that the simplification of structured records can lead to the conflation of distinct fields, where the original context of the data can no longer be traced.

```xml title="<a href='https://jcb.lunaimaging.com/luna/servlet/oai?verb=GetRecord&identifier=JCB~1~1~207~230331&metadataPrefix=oai_dc' target='_blank' style='color: inherit;'>OAI record for the Vak-Vak tree</a>"
<oai_dc:dc>
  <dc:identifier>https://jcb.lunaimaging.com/luna/servlet/detail/JCB~1~1~207~230331</dc:identifier>
  <dc:date>[1730]</dc:date>
  <dc:date>1701-1750</dc:date>
  <dc:identifier>B730 T186</dc:identifier>
  <dc:identifier>04407-16</dc:identifier>
  <dc:description>The Vak-Vak tree with two winged creatures, one a harpy, the other a zaghsar or talking crow.</dc:description>
  <dc:title>[The vak-vak tree]</dc:title>
</oai_dc:dc>
```

So, if available, it is best to rely on the APIs of the institutions, which directly provide the metadata they hold as organized internally. Of the institutions we consulted, Tate, John Carter Brown Libeary, Centre Pompidou and Trentino library system offered this type of service, although it was not always clearly stated. In fact, often the availability of an API is not indicated but can be verified by analyzing the network connections of the item's page when its population depends on the API itself.

## JSON embed parsing

Many collection websites rely on server-side rendering (SSRs), meaning that the HTML content—with the metadata related to the item—is delivered to the user's browser directly from the server, rather than generating it dynamically on the client side. However, some expose the source of the data in json format within an element of the HTML, allowing the categories used in the institution's servers to be reconstructed.

## Extraction from MARC records

Another incredibly rich source of information for libraries are bibliographic records, traditionally in MARC format. Getting into the record and its specific syntax allows one to understand many aspects of the resource not visible in the HTML rendering for the public.

We observed that in Italy the preferred syntax is generally UNIMARC, while in the United States it is MARC 21. One way to distinguish the two is to look for the required fields in the two MARC flavors: if field `040` is present it is MARC21, if `100` it is UNIMARC.

Style sheets are [available](https://www.loc.gov/standards/mods/mods-conversions.html) for MARC21 for automatic conversion to semantic formats such as MODS, but caution is needed because there may be local fields used by the library that are not converted and information is lost. A useful tool for converting MARC binary or text files to MARC-XML or other format using style sheets is [MARC Report](https://www.marcofquality.com/w/).

## Identifying cataloging standards

Just as in poetry the meter is not the genre, so in metadata the format is not the standard, although they are not entirely unrelated to one another. In our survey in few cases was the catalographic standard clearly indicated, and we had to adopt a classification method to match the structure and content of the metadata available to us to the standard that came closest to representing it.

### In libraries

For libraries, the MARC file allows exact identification of the standard, as its indication is provided in specific fields.

1. MARC Fields:

    - In MARC21: 040 $e (Cataloging Source / Description conventions). The field provides a controlled vocabulary for indicating the standard, the is list of which is available [here](https://www.loc.gov/standards/sourcelist/descriptive-conventions.html).

    - In Unimarc: Area 0 della forma del contenuto (SBN MARC tag 181 $a $b) and Area del tipo di supporto (SBN MARC tag 182 $b).

2. ISBD conformity: in Unimarc Leader pos 18 empty if ISBD-compliant, "i" if partially compliant.

3. Controlled vocabularies used, such as RDA Carrier Type

4. Country and date of record creation

Our survey identified the use of the following standards:

- US:

    - AACR2: Anglo-American Cataloguing Rules
    - DCRM(B): Descriptive Cataloging of Rare Materials (Books)
    - RDA: Resource Description and Access

- Italy:

    - RICA: Regole italiane di catalogazione per autori
    - REICAT: Regole italiane di catalogazione
    - RNA: Regeln zur Erschließung von Nachlässen und Autographen (in Trentino)

### In museums

1. Documentation provided by the institution

2. Specific field names ("notizie_storico_critiche" for ICCD-OAC)

3. Metadata structure (Centre Pompidou and Tate Data Models)

#### Centre Pompidou

<div class="grid-right" markdown>
  <p style="margin-top: 0px !important;" markdown>
    ![Overview of the Digital Pompidou data model](../data/references/centre-pompidou-data-model-light.png#only-light)
    ![Overview of the Digital Pompidou data model](../data/references/centre-pompidou-data-model-dark.png#only-dark)
  </p>
</div>

As an example of the process used, we describe the rationale behind identifying the standard for a contemporary art museum that does not provide it.
Centre Pompidou organizes internally its data in RDF as Linked Enterprise Data, but does not expose them[@bermes2014]. The data model appears clearly inspired by CIDOC-CRM event modeling, with some shortcuts to relate some data directly to resources and not events.

For this reason, we chose as a representative standard for metadata provided by Centre Pompidou the LIDO schema (Lightweight Information Describing
Objects), developed by ICOM to make available for publication a variety of information related to both museum objects and their digital representation. LIDO extends CDWA Lite and is underpinned by CIDOC-CRM, inheriting its event-centered approach.

### Non-institutional providers

The heterogeneous nature of the resources under consideration—consumer items related to pop culture, niche contemporary art—led us to rely in part on non-institutional sources. However, even in this case it is possible to check whether the descriptive approach is sufficiently authoritative and deserves confidence.

#### Grand Comics Database

The metadata source for comics is the reference site for the comics community, has a steering committee and precise guidelines for compiling records. We found that the way they treat the descriptive layers of comics magazines aligns to the cataloging standards for Serial resources in the United States.

#### Capti

Capti is a web portal developed within the Italian national project _Spreading visual culture: contemporary art through periodicals, archives and illustrations_ (2013-2016), coordianted by Giorgio Bacci of Scuola Normale Superiore of Pisa. It involved meritorious work on the detailed description of periodical instalments down to single illustrations, flyers, and advertisements. For these metadata we identified the International Standard Bibliographic Description for Serials and Other Continuing Resources (ISBD(CR)) as providing a sufficiently granular descriptive framework, which is the same standard [used](https://cultura.comune.fi.it/system/files/2018-12/PERIODICI_xSola_letturax_0.pdf) by the Gabinetto scientifico-letterario G. P. Vieusseux in Florence, an institution that among its activities similarly deals with digitization of modern periodicals. This project is noteworthy for the innovative approach at the time: through collaboration with source libraries, it enhanced standard bibliographic descriptions of periodicals—traditionally excluding content—by integrating analytically described digitizations.

## Overview

{{ read_csv('../data/tables/scouting.csv', keep_default_na=False) }}

\bibliography

[^*]: Presumed standard not provided by the institution.
[^artsupp]: Also [archived](https://web.archive.org/web/20250107144743/https%3A%2F%2Fartsupp.com%2Fen%2Fartisti%2Fgianfranco-baruchello%2Fgioco-dell-oca) on Janunary 7<sup>th</sup> 2025.
[^bfi]: Also [archived](https://web.archive.org/web/20250107143541/https%3A%2F%2Fcollections-search.bfi.org.uk%2Fweb%2FDetails%2FChoiceFilmWorks%2F150047864) on Janunary 7<sup>th</sup> 2025.
[^capti]: Also [archived](https://web.archive.org/web/20250107170449/http://www.capti.it/index.php?ParamCatID=10&IDFascicolo=799&artgal=38&key=8559&lang=EN) on Janunary 7<sup>th</sup> 2025.