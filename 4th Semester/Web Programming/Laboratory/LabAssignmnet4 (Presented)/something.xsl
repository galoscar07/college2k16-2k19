<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
  <html>
      <head>
          <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" />
          <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js" />
          <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" />
      </head>
  <body>
    <h2>Project</h2>
    <table border="1">
      <tr bgcolor="#9acd32">
        <th>Type</th>
        <th>Content</th>
      </tr>
      <xsl:for-each select="collection/object">
        <tr>
            <td><xsl:value-of select="type"/></td>
            <td>
              <xsl:if test='type="site"'>
                <a class="text-uppercase" href="{string}"><xsl:value-of select="string"/></a>
                </xsl:if>
               <xsl:if test='type="image"'>
                <img class="img-circle" src="{string}" alt="some image"/>
                </xsl:if>
                <xsl:if test='type="text"'>
                <p class="text-danger"><xsl:value-of select="string"/></p>
                </xsl:if>
            </td>
        </tr>
      </xsl:for-each>
    </table>
  </body>
  </html>
</xsl:template>

</xsl:stylesheet>