

__author__ = "Charlie Taylor (charlietaylor@sourceforge.net)"
__version__ = " 1.0 "
__date__ = "Jan 1, 2009"
__copyright__ = "Copyright (c) 2009 Charlie Taylor"
__license__ = "BSD"

my_css = '' # place-holder... my_css initialization is at bottom

def getHead(title='Parametric Solution', task='generic study', author='C Taylor',
    date='', version=''):
                
    return '''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
        "http://www.w3.org/TR/html4/loose.dtd">
<html lang="en">
<head>
    <meta http-equiv="content-type" content="text/html; charset=iso-8859-1">
    <title>%s</title>
%s

</head>
<body>
<center><table bgcolor="#FFFFFF" width="680"><tr><td colspan="2" nowrap align="center">
<h3 class="header">%s</h3></td></tr>
<tr>
<td align="left"><span class="header"> %s</span></td>
<td align="right"><span class="header"> %s</span></td></tr>
<tr>
<td align="left"><span class="header">by: %s</span></td>
<td align="right"><span class="header">%s</span></td>
</tr></table></center>
'''%(title,my_css,title,task,version,author,date)


def getFooter():
    return '''</body>
</html>
'''

# use this static style
my_css = '''<style type="text/css">
BODY{ 
    background-color: #55607B;  
    
    margin-bottom: 0px;  
    margin-top: 0px; 
    font-family: Verdana, Arial, Helvetica, sans-serif;  
}
.mytable{ 
    page-break-inside: avoid;
    background-color: #FFFFFF;  
    margin-bottom: 0px;  
    margin-top: 0px; 
    font-size : 12px;
    font-family: Verdana, Arial, Helvetica, sans-serif;  
}

td, p, .p{
    font-family: Verdana, Arial, Helvetica, sans-serif;
    font-size : 12px;
}

.header {
    font-size: 14px;
    color: #A62F24;
    font-weight: bold;
    line-height: 18px;
    margin-bottom: 8px;
}

.subhead  {
 font-size : 12px;
 line-height: 125%;
 font-weight: bold;
 color: #A62F24;
} 
  
.hometext  {
    font-size: 12px;
    line-height: 140%;
    font-weight: bold;
    color: #666666;
} 
 
.topnav{
 font-family: Verdana, Arial, Helvetica, sans-serif;
 font-size : 10px;
 font-weight : bold;
 color: #FFFFFF;
 text-decoration: none;
 padding-bottom: 1px;
}
a.topnav:hover{
 color: #D0D0D0;
}
a.p  {
 color:#666666;
}
a.p:hover  {
 color: #A62F24;
}
a.p:visited  {
 color: #999999;
}

.small  {
 font-family: Verdana, Arial, Helvetica, sans-serif;
 font-size : 10px;
 line-height: 110%;
}
a.small  {
 color:#666666;
}
a.small:hover  {
 color: #A62F24;
}
a.small:visited  {
 color: #999999;
}

a.formlink  {
 color:#333333;
 text-decoration: none;
}
a.formlink:hover  {
 color: #A62F24;
 text-decoration: underline;
}
a.formlink:visited  {
 color: #999999;
 text-decoration: underline;
}

.breadcrumb  {
 font-family: Verdana, Arial, Helvetica, sans-serif;
 font-size : 10px;
 color:#999999;
 text-decoration: none;
}
.breadcrumb:hover  {
 color: #A62F24;
 text-decoration: underline;
}

.supplierlink  {
 font-family: Verdana, Arial, Helvetica, sans-serif;
 font-size : 10px;
 line-height: 140%;
 color:#A62F24;
 text-decoration: none;
}
.supplierlink:hover  {
 color: #333333;
 text-decoration: underline;
}

a.loclink{
    font-family: Verdana, Arial, Helvetica, sans-serif;
    font-size : 12px;
    line-height: 125%;
 color: #A62F24;
}
a.loclink:hover  {
 color: #666666;
}


.red  {
 color: #A62F24;
}

.x  {
 font-family: Verdana, Arial, Helvetica, sans-serif;
 font-size : 14px;
 font-weight: bold;
 color: #008000;
}

.footer{
 font-size : 10px;
 color: #CDCCCC;
 text-decoration: none;
 padding-top: 8px;
 padding-bottom: 0px;
}
.footer:hover  {
 color: #FFFFFF;
} 

form, input, select, option{
    margin-bottom : 0px;
    margin-left : 0px;
    margin-right : 0px;
    margin-top : 0px;
    padding-bottom : 0px;
    padding-left : 0px;
    padding-right : 0px;
    padding-top : 0px;
    font-family : Verdana, Arial, Helvetica, sans-serif;
    font-size : 10px;
    height : 14px;
    border-bottom: 1px;
    border-color: #CCCCCC;
}


</style>

'''