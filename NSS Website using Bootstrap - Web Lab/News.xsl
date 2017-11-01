<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
  <html>
  <body>
  <h2>Latest News</h2>
  <table border="1">
    <tr bgcolor="#9acd32">
      <th>Content</th>
      <th>By</th>
      <th>Date</th>
      <th>Venue</th>
    </tr>
    <xsl:for-each select="page/body/news">
    <tr>
      <td><xsl:value-of select="headline"/></td>
      <td><xsl:value-of select="byline/bytag"/></td>
      <td><xsl:value-of select="dateline/location"/></td>
      <td><xsl:value-of select="dateline/date"/></td>
    </tr>
    </xsl:for-each>
  </table>
  </body>
  </html>
</xsl:template>

</xsl:stylesheet>