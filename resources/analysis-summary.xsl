<?xml version="1.0" encoding="ISO-8859-1"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:output method="html"
                version="1.0"
                encoding="ISO-8859-1"
                omit-xml-declaration="yes"
                standalone="yes"
                doctype-public="-//W3C//DTD XHTML 1.0 Transitional//EN"
                doctype-system="http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"
                cdata-section-elements="value"
                indent="yes"
                media-type="text/html"/>

    <xsl:template match="/">

        <html>
            <head>
                <title>Match-up Analysis</title>
                <link rel="stylesheet" type="text/css" href="styleset.css"/>
            </head>
            <body>

                <h2>Match-up Analysis Report</h2>

                <h3>Processing Information</h3>

                <table>
                    <tr>
                        <td class="name">Performed at:</td>
                        <td class="value">
                            <xsl:value-of select="analysisSummary/performedAt"/>
                        </td>
                    </tr>
                    <tr>
                        <td class="name">Number of match-ups:</td>
                        <td class="value">
                            <xsl:value-of select="analysisSummary/recordCount"/>
                        </td>
                    </tr>
                    <tr>
                        <td class="name">Model variables:</td>
                        <td class="value">
                            <xsl:for-each select="analysisSummary/modelVariables/modelVariable">
                                <xsl:value-of select="text()"/>
                                <br/>
                            </xsl:for-each>
                        </td>
                    </tr>
                    <tr>
                        <td class="name">Reference variables:</td>
                        <td class="value">
                            <xsl:for-each select="analysisSummary/referenceVariables/referenceVariable">
                                <xsl:value-of select="text()"/>
                                <br/>
                            </xsl:for-each>
                        </td>
                    </tr>
                </table>

                <h3>Analysis Configuration</h3>

                <table>
                    <tr class="table_header">
                        <td>
                            Parameter
                        </td>
                        <td>
                            Value
                        </td>
                        <td>
                            Unit
                        </td>
                    </tr>
                    <xsl:for-each select="analysisSummary/configuration/property">
                        <tr>
                            <td class="name">
                                <xsl:value-of select="name"/>
                            </td>
                            <td class="std">
                                <xsl:value-of select="value"/>
                            </td>
                            <td class="std">
                                <xsl:value-of select="unit"/>
                            </td>
                        </tr>
                    </xsl:for-each>
                </table>

                <xsl:for-each select="analysisSummary/statistics/statistic[@type='relative']">
                    <h3>Relative Statistics for
                        <xsl:value-of select="model_name"/>
                        with
                        <xsl:value-of select="ref_name"/>
                    </h3>

                    <table>
                        <tr class="table_header">
                            <td>
                                Statistical Term
                            </td>
                            <td>
                                Value
                            </td>
                        </tr>
                        <xsl:for-each select="properties/property">
                            <tr>
                                <td class="name">
                                    <xsl:value-of select="name"/>
                                </td>
                                <td class="value">
                                    <xsl:value-of select="value"/>
                                </td>
                            </tr>
                        </xsl:for-each>
                    </table>
                </xsl:for-each>

                <xsl:for-each select="analysisSummary/statistics/statistic[@type='model']">
                    <h3>Statistics for
                        <xsl:value-of select="model_name"/>
                    </h3>

                    <table>
                        <tr class="table_header">
                            <td>
                                Statistical Term
                            </td>
                            <td>
                                Value
                            </td>
                        </tr>
                        <xsl:for-each select="properties/property">
                            <tr>
                                <td class="name">
                                    <xsl:value-of select="name"/>
                                </td>
                                <td class="value">
                                    <xsl:value-of select="value"/>
                                </td>
                            </tr>
                        </xsl:for-each>
                    </table>
                </xsl:for-each>

                <xsl:for-each select="analysisSummary/statistics/statistic[@type='reference']">
                    <h3>Statistics for
                        <xsl:value-of select="ref_name"/>
                    </h3>

                    <table>
                        <tr class="table_header">
                            <td>
                                Statistical Term
                            </td>
                            <td>
                                Value
                            </td>
                        </tr>
                        <xsl:for-each select="properties/property">
                            <tr>
                                <td class="name">
                                    <xsl:value-of select="name"/>
                                </td>
                                <td class="value">
                                    <xsl:value-of select="value"/>
                                </td>
                            </tr>
                        </xsl:for-each>
                    </table>
                </xsl:for-each>

                <h3>Matchups</h3>

                <table class="matchup">
                    <tr class="table_header">
                        <td>Matchup #</td>
                        <td>Time</td>
                        <td>Depth</td>
                        <td>Lat</td>
                        <td>Lon</td>
                        <td>Reference Time</td>
                        <td>Reference Depth</td>
                        <td>Reference Lat</td>
                        <td>Reference Lon</td>
                        <xsl:for-each select="analysisSummary/matchups/variables/var">
                            <td><xsl:value-of select="text()"/></td>
                        </xsl:for-each>
                    </tr>

                    <xsl:for-each select="analysisSummary/matchups/matchup">
                    <tr>
                        <td>
                            <xsl:value-of select="recordNumber"/>
                        </td>
                        <td class="value">
                            <xsl:value-of select="time"/>
                        </td>
                        <td class="value">
                            <xsl:value-of select="depth"/>
                        </td>
                        <td class="value">
                            <xsl:value-of select="lat"/>
                        </td>
                        <td class="value">
                            <xsl:value-of select="lon"/>
                        </td>
                        <td class="value">
                            <xsl:value-of select="reference_time"/>
                        </td>
                        <td class="value">
                            <xsl:value-of select="reference_depth"/>
                        </td>
                        <td class="value">
                            <xsl:value-of select="reference_lat"/>
                        </td>
                        <td class="value">
                            <xsl:value-of select="reference_lon"/>
                        </td>

                        <xsl:for-each select="property">
                            <td><xsl:value-of select="value"/></td>
                        </xsl:for-each>

                    </tr>
                    </xsl:for-each>

                </table>

                <h3>Taylor Diagram</h3>

                <img>
                    <xsl:attribute name="src"><xsl:value-of select="analysisSummary/taylor"/></xsl:attribute>
                </img>

            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
