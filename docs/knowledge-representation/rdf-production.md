# Knowledge Representation

=== "Il Giuoco dell'Oca"

	Read the [rules](../data/tei/rules.html){:target="_blank"}

	| subject   | predicate                | object                                                |
	|:----------|:-------------------------|:------------------------------------------------------|
	| gdo-w     | rdf:type                 | lrmoo:F1_Work                                         |
	| gdo-w     | rdaw:P10088              | Il Giuoco dell'Oca                                    |
	| gdo-w     | rdaw:P10436              | edoardo-sanguineti                                    |
	| gdo-w     | rdawd:P10004             | http://id.loc.gov/authorities/genreForms/gf2015026020 |
	| gdo-w     | lrmoo:R3_is_realised_in  | gdo-e                                                 |
	| gdo-e     | rdf:type                 | lrmoo:F2_Expression                                   |
	| gdo-e     | rdae:P20312              | Il Giuoco dell'Oca                                    |
	| gdo-e     | rdae:P20001              | rdaco:1020                                            |
	| gdo-e     | rdae:P20006              | it                                                    |
	| gdo-e     | lrmoo:R5_has_component   | regole-gioco                                          |
	| gdo-e     | lrmoo:R5_has_component   | chapter-LXXXVIII                                      |
	| gdo-e     | lrmoo:R5_has_component   | chapter-LXXXVIII                                      |
	| gdo-e     | lrmoo:R5_has_component   | chapter-VII                                           |
	| gdo-e     | lrmoo:R5_has_component   | chapter-VII                                           |
	| gdo-e     | lrmoo:R5_has_component   | chapter-LXXXIII                                       |
	| gdo-e     | lrmoo:R5_has_component   | chapter-LXXXIII                                       |
	| gdo-e     | lrmoo:R5_has_component   | chapter-I                                             |
	| gdo-e     | lrmoo:R5_has_component   | chapter-XXXIX                                         |
	| gdo-e     | lrmoo:R5_has_component   | chapter-LXXXIV                                        |
	| gdo-e     | lrmoo:R5_has_component   | chapter-CIX                                           |
	| gdo-e     | lrmoo:R5_has_component   | chapter-CIX                                           |
	| gdo-e     | lrmoo:R5_has_component   | chapter-CIX                                           |
	| gdo-e     | rdae:P20338              | valerio-riva                                          |
	| gdo-e     | lrmoo:R4i_is_embodied_in | gdo-m                                                 |
	| gdo-m     | rdf:type                 | lrmoo:F3_Manifestation                                |
	| gdo-m     | rdam:P30011              | 1967                                                  |
	| gdo-m     | rdam:P30420              | giangiacomo-feltrinelli-editore                       |
	| gdo-m     | rdam:P30088              | milan                                                 |
	??? turtle "See RDF triples"
	    ```turtle
	    --8<-- ""
	    ```
	??? note "See TEI encoding"
		=== "TEI"

			```xml
			--8<-- "docs/data/tei/rules.xml"
			```
		=== "XSLT"

			```xml
			--8<-- "docs/data/tei/rules.xsl"
			```			

=== "Marca Stella's Game of the Goose"

	| subject               | predicate                | object                                 |
	|:----------------------|:-------------------------|:---------------------------------------|
	| giuoco-marca-stella-w | rdf:type                 | lrmoo:F1_Work                          |
	| giuoco-marca-stella-w | rdaw:P10088              | Il Gioco dell'Oca Marca Stella         |
	| giuoco-marca-stella-w | rdaw:P10004              | https://iconclass.org/43C531           |
	| giuoco-marca-stella-w | owl:sameAs               | https://www.wikidata.org/wiki/Q1548611 |
	| giuoco-marca-stella-w | lrmoo:R3_is_realised_in  | giuoco-marca-stella-e                  |
	| giuoco-marca-stella-e | rdf:type                 | lrmoo:F2_Expression                    |
	| giuoco-marca-stella-e | rdae:P20001              | rdaco:1014                             |
	| giuoco-marca-stella-e | rdae:P20006              | it                                     |
	| giuoco-marca-stella-e | lrmoo:R4i_is_embodied_in | giuoco-marca-stella-m                  |
	| giuoco-marca-stella-m | rdf:type                 | lrmoo:F3_Manifestation                 |
	| giuoco-marca-stella-m | rdam:P30420              | marca-stella                           |
	| giuoco-marca-stella-m | rdam:P30011              | 1949                                   |
	| giuoco-marca-stella-m | rdam:P30088              | milan                                  |
	??? turtle "See RDF triples"
	    ```turtle
	    --8<-- ""
	    ```

=== "Baruchello's Collage"

	| subject             | predicate                | object                                   |
	|:--------------------|:-------------------------|:-----------------------------------------|
	| giuoco-baruchello-w | rdf.type                 | lrmoo:F1_Work                            |
	| giuoco-baruchello-w | rdaw:P10088              | Il Giuoco dell'Oca di Edoardo Sanguineti |
	| giuoco-baruchello-w | rdaw:P10004              | https://vocab.getty.edu/aat/300033963    |
	| giuoco-baruchello-w | rdaw:P10451              | gianfranco-baruchello                    |
	| giuoco-baruchello-w | rdaw:P10219              | 1967                                     |
	| giuoco-baruchello-w | lrmoo:R3_is_realised_in  | giuoco-baruchello-e                      |
	| giuoco-baruchello-e | rdf.type                 | lrmoo_F2_Expression                      |
	| giuoco-baruchello-e | rdae:P20001              | rdaco:1014                               |
	| giuoco-baruchello-e | lrmoo:R4i_is_embodied_in | giuoco-baruchello-m                      |
	| giuoco-baruchello-m | rdf:type                 | lrmoo:F3_Manifestation                   |
	??? turtle "See RDF triples"
	    ```turtle
	    --8<-- ""
	    ```

=== "Cassa Sistina"

	| subject         | predicate                | object                               |
	|:----------------|:-------------------------|:-------------------------------------|
	| cassa-sistina-w | rdf:type                 | lrmoo:F1_Work                        |
	| cassa-sistina-w | rdaw:P10088              | Cassa Sistina                        |
	| cassa-sistina-w | rdaw:P10004              | http://vocab.getty.edu/aat/300047090 |
	| cassa-sistina-w | rdaw:P10427              | mario-ceroli                         |
	| cassa-sistina-w | rdaw:P10219              | 1966                                 |
	| cassa-sistina-w | lrmoo:R3_is_realised_in  | cassa-sistina-e                      |
	| cassa-sistina-e | rdf:type                 | lrmoo:F2_Expression                  |
	| cassa-sistina-e | rdae:P20001              | rdaco:1021                           |
	| cassa-sistina-e | lrmoo:R4i_is_embodied_in | cassa-sistina-m                      |
	| cassa-sistina-m | rdf:type                 | lrmoo:F3_Manifestation               |
	??? turtle "See RDF triples"
	    ```turtle
	    --8<-- ""
	    ```

=== "Vampyr"

	| subject   | predicate                | object                                                |
	|:----------|:-------------------------|:------------------------------------------------------|
	| vampyr-w  | rdf:type                 | lrmoo:F1_Work                                         |
	| vampyr-w  | rdaw:P10088              | Vampyr                                                |
	| vampyr-w  | rdaw:P10004              | http://id.loc.gov/authorities/genreForms/gf2011026321 |
	| vampyr-w  | rdaw:P10418              | carl-theodor-dreyer                                   |
	| vampyr-w  | rdaw:P10422              | carl-theodor-dreyer                                   |
	| vampyr-w  | rdaw:P10218              | france|germany                                        |
	| vampyr-w  | owl:sameAs               | https://www.wikidata.org/wiki/Q304923                 |
	| vampyr-w  | lrmoo:R3_is_realised_in  | vampyr-e                                              |
	| vampyr-e  | rdf:type                 | lrmoo:F2_Expression                                   |
	| vampyr-e  | rdae:P20006              | de                                                    |
	| vampyr-e  | rdae:P20001              | rdaco:1023                                            |
	| vampyr-e  | lrmoo:R4i_is_embodied_in | vampyr-m                                              |
	| vampyr-m  | rdf:type                 | lrmoo:F3_Manifestation                                |
	| vampyr-m  | rdam:P30011              | 1932                                                  |
	??? turtle "See RDF triples"
	    ```turtle
	    --8<-- ""
	    ```

=== "Symbols of Transformation"

	| subject                  | predicate                | object                                                         |
	|:-------------------------|:-------------------------|:---------------------------------------------------------------|
	| symbols-transformation-w | rdf:type                 | lrmoo:F1_Work                                                  |
	| symbols-transformation-w | rdaw:P10088              | Symbols of Transformation                                      |
	| symbols-transformation-w | rdaw:P10004              | http://id.loc.gov/authorities/genreForms/gf2014026074          |
	| symbols-transformation-w | rdaw:P10065              | carl-gustav-jung                                               |
	| symbols-transformation-w | owl:sameAs               | https://id.oclc.org/worldcat/entity/E39PCGgM4td7W4Tr3RX7C9PbBP |
	| symbols-transformation-w | lrmoo:R3_is_realised_in  | symbols-transformation-e                                       |
	| symbols-transformation-e | rdf:type                 | lrmoo:F2_Expression                                            |
	| symbols-transformation-e | rdae:P20001              | rdaco:1020                                                     |
	| symbols-transformation-e | rdae:P20346              | renato-raho                                                    |
	| symbols-transformation-e | rdae:P20006              | it                                                             |
	| symbols-transformation-e | lrmoo:R4i_is_embodied_in | symbols-transformation-m                                       |
	| symbols-transformation-m | rdf:type                 | lrmoo:F3_Manifestation                                         |
	| symbols-transformation-m | rdam:P30011              | 1970                                                           |
	| symbols-transformation-m | rdam:P30088              | turin                                                          |
	| symbols-transformation-m | rdam:P30362              | paolo-boringhieri                                              |
	??? turtle "See RDF triples"
	    ```turtle
	    --8<-- ""
	    ```

=== "The Vak-Vak tree"

	| subject   | predicate                | object                               |
	|:----------|:-------------------------|:-------------------------------------|
	| vak-vak-w | rdf:type                 | lrmoo:F1_Work                        |
	| vak-vak-w | rdaw:P10088              | The Vak-Vak tree                     |
	| vak-vak-w | rdaw:P10004              | http://vocab.getty.edu/aat/300015578 |
	| vak-vak-w | lrmoo:R3_is_realised_in  | vak-vak-e                            |
	| vak-vak-e | rdf:type                 | lrmoo:F2_Expression                  |
	| vak-vak-e | rdae:P20001              | rdaco:1014                           |
	| vak-vak-e | lrmoo:R4i_is_embodied_in | vak-vak-m                            |
	| vak-vak-m | rdf:type                 | lrmoo:F3_Manifestation               |
	| vak-vak-m | rdam:P30011              | 1730                                 |
	| vak-vak-m | rdam:P30088              | constantinople                       |
	| vak-vak-m | rdam:P30362              | muteferrika-ibrahim                  |
	??? turtle "See RDF triples"
	    ```turtle
	    --8<-- ""
	    ```

=== "L'occhio degli occhi"

	| subject              | predicate                | object                               |
	|:---------------------|:-------------------------|:-------------------------------------|
	| occhio-degli-occhi-w | rdf:type                 | lrmoo:F1_Work                        |
	| occhio-degli-occhi-w | rdaw:P10088              | L'occhio degli occhi                 |
	| occhio-degli-occhi-w | rdaw:P10004              | http://vocab.getty.edu/aat/300404586 |
	| occhio-degli-occhi-w | rdaw:P10451              | carol-rama                           |
	| occhio-degli-occhi-w | rdaw:P10219              | 1967                                 |
	| occhio-degli-occhi-w | lrmoo:R3_is_realised_in  | occhio-degli-occhi-e                 |
	| occhio-degli-occhi-e | rdf:type                 | lrmoo:F2_Expression                  |
	| occhio-degli-occhi-e | rdae:P20001              | rdaco:1014                           |
	| occhio-degli-occhi-e | lrmoo:R4i_is_embodied_in | occhio-degli-occhi-m                 |
	| occhio-degli-occhi-m | rdf:type                 | lrmoo:F3_Manifestation               |
	??? turtle "See RDF triples"
	    ```turtle
	    --8<-- ""
	    ```

=== "Marilyn Photo"

	| subject         | predicate                | object                               |
	|:----------------|:-------------------------|:-------------------------------------|
	| marilyn-photo-w | rdf:type                 | lrmoo:F1_Work                        |
	| marilyn-photo-w | rdaw:P10088              | Rooney, Monroe And Anthony           |
	| marilyn-photo-w | rdaw:P10004              | http://vocab.getty.edu/aat/300134989 |
	| marilyn-photo-w | rdaw:P10539              | pictorial-parade                     |
	| marilyn-photo-w | rdaw:P10219              | 1952                                 |
	| marilyn-photo-w | rdaw:P10218              | hollywood                            |
	| marilyn-photo-w | lrmoo:R3_is_realised_in  | marilyn-photo-e                      |
	| marilyn-photo-e | rdf:type                 | lrmoo:F2_Expression                  |
	| marilyn-photo-e | rdae:P20001              | rdaco:1014                           |
	| marilyn-photo-e | lrmoo:R4i_is_embodied_in | marilyn-photo-m                      |
	| marilyn-photo-m | rdf:type                 | lrmoo:F3_Manifestation               |
	??? turtle "See RDF triples"
	    ```turtle
	    --8<-- ""
	    ```

=== "Marilyn Song"

	| subject        | predicate                | object                             |
	|:---------------|:-------------------------|:-----------------------------------|
	| marilyn-song-w | rdf:type                 | lrmoo:F1_Work                      |
	| marilyn-song-w | rdaw:P10088              | Marilyn                            |
	| marilyn-song-w | rdaw:P10004              | http://id.worldcat.org/fast/887553 |
	| marilyn-song-w | rdaw:P10442              | ray-anthony                        |
	| marilyn-song-w | rdaw:P10218              | united-states                      |
	| marilyn-song-w | lrmoo:R3_is_realised_in  | marilyn-song-e                     |
	| marilyn-song-e | rdf:type                 | lrmoo:F2_Expression                |
	| marilyn-song-e | rdae:P20001              | rdaco:1011                         |
	| marilyn-song-e | rdae:P20006              | en-US                              |
	| marilyn-song-e | lrmoo:R4i_is_embodied_in | marilyn-song-m                     |
	| marilyn-song-m | rdf:type                 | lrmoo:F3_Manifestation             |
	| marilyn-song-m | rdam:P30011              | 1952                               |
	| marilyn-song-m | rdam:P30420              | capitol-records                    |
	??? turtle "See RDF triples"
	    ```turtle
	    --8<-- ""
	    ```

=== "Hamilton's Collage"

	| subject     | predicate                | object                                                 |
	|:------------|:-------------------------|:-------------------------------------------------------|
	| just-what-w | rdf_type                 | lrmoo:F1_Work                                          |
	| just-what-w | rdaw:P10088              | Just what is it that makes today's homes so appealing? |
	| just-what-w | rdaw:P10004              | https://vocab.getty.edu/aat/300033963                  |
	| just-what-w | rdaw:P10451              | richard-hamilton                                       |
	| just-what-w | rdaw:P10219              | 1956                                                   |
	| just-what-w | owl:sameAs               | https://www.wikidata.org/wiki/Q3190307                 |
	| just-what-w | lrmoo:R3_is_realised_in  | just-what-e                                            |
	| just-what-e | rdf:type                 | lrmoo:F2_Expression                                    |
	| just-what-e | rdae:P20001              | rdaco:1014                                             |
	| just-what-e | lrmoo:R4i_is_embodied_in | just-what-m                                            |
	| just-what-m | rdf:type                 | lrmoo:F3_Manifestation                                 |
	??? turtle "See RDF triples"
	    ```turtle
	    --8<-- ""
	    ```

=== "Young Romance"

	| subject         | predicate                | object                                                |
	|:----------------|:-------------------------|:------------------------------------------------------|
	| young-romance-w | rdf:type                 | lrmoo:F1_Work                                         |
	| young-romance-w | rdaw:P10088              | Young Romance                                         |
	| young-romance-w | rdaw:P10004              | http://id.loc.gov/authorities/genreForms/gf2014026515 |
	| young-romance-w | rdaw:P10417              | joe-simon|jack-kirby                                  |
	| young-romance-w | rdaw:P10219              | 1947                                                  |
	| young-romance-w | rdaw:P10218              | united-states                                         |
	| young-romance-w | owl:sameAs               | https://www.wikidata.org/wiki/Q3572861                |
	| young-romance-w | lrmoo:R3_is_realised_in  | young-romance-e                                       |
	| young-romance-e | rdf:type                 | lrmoo:F2_Expression                                   |
	| young-romance-e | rdae:P20001              | rdaco:1014|rdaco:1020                                 |
	| young-romance-e | rdae:P20006              | en-US                                                 |
	| young-romance-e | lrmoo:R4i_is_embodied_in | young-romance-m                                       |
	| young-romance-m | rdf:type                 | lrmoo:F3_Manifestation                                |
	| young-romance-m | rdam:P30420              | feature-publications                                  |
	??? turtle "See RDF triples"
	    ```turtle
	    --8<-- ""
	    ```

=== "Go for Your Money"

	| subject             | predicate                | object                                                |
	|:--------------------|:-------------------------|:------------------------------------------------------|
	| go-for-your-money-w | rdf:type                 | lrmoo:F1_Work                                         |
	| go-for-your-money-w | rdaw:P10088              | Go for your money                                     |
	| go-for-your-money-w | rdaw:P10004              | http://id.loc.gov/authorities/genreForms/gf2011026049 |
	| go-for-your-money-w | rdaw:P10451              | magdalo-mussio                                        |
	| go-for-your-money-w | lrmoo:R3_is_realised_in  | go-for-your-money-e                                   |
	| go-for-your-money-e | rdf:type                 | lrmoo:F2_Expression                                   |
	| go-for-your-money-e | rdae:P20001              | rdaco:1014                                            |
	| go-for-your-money-e | lrmoo:R4i_is_embodied_in | go-for-your-money-m                                   |
	| go-for-your-money-m | rdf:type                 | lrmoo:F3_Manifestation                                |
	| go-for-your-money-m | rdam:P30011              | 1966                                                  |
	??? turtle "See RDF triples"
	    ```turtle
	    --8<-- ""
	    ```

=== "The Lady from Shanghai"

	| subject              | predicate                | object                                                |
	|:---------------------|:-------------------------|:------------------------------------------------------|
	| lady-from-shanghai-w | rdf:type                 | lrmoo:F1_Work                                         |
	| lady-from-shanghai-w | rdaw:P10088              | The Lady From Shanghai                                |
	| lady-from-shanghai-w | rdaw:P10004              | http://id.loc.gov/authorities/genreForms/gf2011026250 |
	| lady-from-shanghai-w | rdaw:P10418              | orson-welles                                          |
	| lady-from-shanghai-w | rdaw:P10516              | columbia-pictures                                     |
	| lady-from-shanghai-w | rdaw:P10218              | united-states                                         |
	| lady-from-shanghai-w | owl:sameAs               | https://www.wikidata.org/wiki/Q1214303                |
	| lady-from-shanghai-w | lrmoo:R3_is_realised_in  | lady-from-shanghai-e                                  |
	| lady-from-shanghai-e | rdf:type                 | lrmoo:F2_Expression                                   |
	| lady-from-shanghai-e | rdae:P20006              | en-US                                                 |
	| lady-from-shanghai-e | rdae:P20001              | rdaco:1023                                            |
	| lady-from-shanghai-e | lrmoo:R4i_is_embodied_in | lady-from-shanghai-m                                  |
	| lady-from-shanghai-m | rdf:type                 | lrmoo:F3_Manifestation                                |
	| lady-from-shanghai-m | rdam:P30011              | 1948                                                  |
	??? turtle "See RDF triples"
	    ```turtle
	    --8<-- ""
	    ```


<style>
	table td {
		padding: 0 1.25em !important;
	}

	table th {
		padding: .4em 1.25em !important;
	}

</style>