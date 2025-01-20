<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
   xmlns:tei="http://www.tei-c.org/ns/1.0">
   <xsl:template match="/">
      <html>
            <head>
               <title>Il Giuoco dell'Oca</title>
               <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet"/>
               <h2 style="text-align:center; color:#B81A61; font-family:verdana; font-size:160%; font-weight: bold;"><em><xsl:value-of select="/tei:TEI/tei:teiHeader/tei:fileDesc/tei:titleStmt/tei:title/text()"/></em></h2>
               <h3 style="text-align:center; color:#B81A61; font-family:verdana; font-size:100%;">Project Team</h3>
               <h3 style="text-align:center; color:#B81A61; font-family:verdana; font-size:100%;"><xsl:value-of select="/tei:TEI/tei:teiHeader/tei:fileDesc/tei:titleStmt/tei:respStmt/tei:name/text()"/></h3>
            </head>
         <body style="background-color:#1E2129;">
            <div class="container" style="padding-top: 40px;">
               <div class="row">
                  <div class="col-md-8">
                     <xsl:for-each select="tei:TEI/tei:text/tei:front/tei:div[@type='rules']/tei:l">
                           <xsl:apply-templates select="."/>
                     </xsl:for-each>
                  </div>
                  <div class="col-md-4">
                     <h2 style="color:#B81A61; font-size:20px; text-align:center; font-family:verdana; font-weight: bold;">Style</h2>
                     <table border= "1px solid black;">
                        <tr color="#1E2129">
                           <th style="color:#FFFFFF; font-size:20px; font-family:verdana; font-weight: bold;">Tipology</th>
                           <th style="color:#FFFFFF; font-size:20px; font-family:verdana; font-weight: bold;">Description</th>
                        </tr>
                         <tr>
                            <td  lenght="100%" style="color: #8c144a; font-family:verdana; font-weight: bold;">Anaphor</td>
                            <td lenght="100%" style="color: #FFFFFF; font-family:verdana;"><xsl:value-of select="/tei:TEI/tei:teiHeader/tei:encodingDesc/tei:classDecl/tei:taxonomy/tei:category[@xml:id='anaphor']/tei:desc/text()"/></td>
                         </tr>
                        <tr>
                           <td lenght="100%" style="color: #a1647f; font-family:verdana; font-weight: bold;">Enjambement strong</td>
                           <td lenght="100%" style="color: #FFFFFF; font-family:verdana;">Strong disruption of the metric-syntactic unitary cohesion of a verse</td>
                        </tr>
                        <tr>
                           <td lenght="100%" style="color: #e8aec8; font-family:verdana;">Enjambement weak</td>
                           <td lenght="100%" style="color: #FFFFFF; font-family:verdana;">Weak disruption of the metric-syntactic unitary cohesion of a verse</td>
                        </tr>
                     </table>
                  </div>  
               </div> 
            </div>            
         </body>
      </html>
   </xsl:template>
   
   <xsl:template match="@*|node()">
      <xsl:copy>
         <xsl:apply-templates select="@*|node()" />
      </xsl:copy>
   </xsl:template>
   
   <xsl:template match="tei:interp[@ana='#anaphor']">
      <span style="color: #8c144a;">
         <xsl:apply-templates select="@*|node()" />
      </span>
   </xsl:template>
   
   <xsl:template match="tei:l">
      <p style="color:#FFFFFF; font-size:15px;">
         <xsl:apply-templates select="@*|node()"/>
      </p>
   </xsl:template>
   
   <xsl:template match="tei:l[@enjamb='strong']">
      <p style="color:#FFFFFF; font-size:15px; text-decoration: underline 3px; text-decoration-color: #a1647f;">
         <xsl:apply-templates select="@*|node()"/>
      </p>   
   </xsl:template>
   
   <xsl:template match="tei:l[@enjamb='weak']">
      <p style="color:#FFFFFF; font-size:15px; text-decoration: underline 2px; text-decoration-color: #e8aec8;">
         <xsl:apply-templates select="@*|node()"/>
      </p>   
   </xsl:template>
</xsl:stylesheet>


 

