#!/user/bin/env python
#coding=utf-8

# @project : rearend
# @author  : kalifun
# @file   : hello.py
# @ide    : PyCharm
# @time   : 2019/7/2 19:56
from one.config.config import Config
from flask_mail import Message,Mail
mail = Mail()

def sedmail(recipient):
    msg = Message("One订阅",sender=Config.MAIL_USERNAME,recipients=[recipient])
    msg.body = "邮件内容"
    msg.html = """
<!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
<!--[if gte mso 9]>
<xml>
  <o:OfficeDocumentSettings>
    <o:AllowPNG/>
    <o:PixelsPerInch>96</o:PixelsPerInch>
  </o:OfficeDocumentSettings>
</xml>
<![endif]-->
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="x-apple-disable-message-reformatting">
  <!--[if !mso]><!--><meta http-equiv="X-UA-Compatible" content="IE=edge"><!--<![endif]-->
  <title></title>
  <style type="text/css">
    body {
  margin: 0;
  padding: 0;
}

table, tr, td {
  vertical-align: top;
  border-collapse: collapse;
}

p, ul {
  margin: 0;
}

.ie-container table, .mso-container table {
  table-layout: fixed;
}

* {
  line-height: inherit;
}

a[x-apple-data-detectors=true] {
  color: inherit !important;
  text-decoration: none !important;
}

.ExternalClass, .ExternalClass p, .ExternalClass span, .ExternalClass font, .ExternalClass td, .ExternalClass div {
  line-height: 100%;
}

[owa] .email-row .email-col {
  display: table-cell;
  float: none !important;
  vertical-align: top;
}

.ie-container .email-col-100, .ie-container .email-row, [owa] .email-col-100, [owa] .email-row { width: 600px !important; }
.ie-container .email-col-17, [owa] .email-col-17 { width: 102.00000000000001px !important; }
.ie-container .email-col-25, [owa] .email-col-25 { width: 150px !important; }
.ie-container .email-col-33, [owa] .email-col-33 { width: 198px !important; }
.ie-container .email-col-50, [owa] .email-col-50 { width: 300px !important; }
.ie-container .email-col-67, [owa] .email-col-67 { width: 402px !important; }

@media only screen and (min-width: 620px) {
  .email-row { width: 600px !important; }
  .email-row .email-col { vertical-align: top; }
  .email-row .email-col-100 { width: 600px !important; }
  .email-row .email-col-67 { width: 402px !important; }
  .email-row .email-col-50 { width: 300px !important; }
  .email-row .email-col-33 { width: 198px !important; }
  .email-row .email-col-25 { width: 150px !important; }
  .email-row .email-col-17 { width: 102.00000000000001px !important; }
}

@media (max-width: 620px) {
  .hide-mobile { display: none !important; }
  .email-row-container {
    padding-left: 0px !important;
    padding-right: 0px !important;
  }
  .email-row .email-col {
    min-width: 320px !important;
    max-width: 100% !important;
    display: block !important;
  }
  .email-row { width: calc(100% - 40px) !important; }
  .email-col { width: 100% !important; }
  .email-col > div { margin: 0 auto; }
  .no-stack .email-col { min-width: 0 !important; display: table-cell !important; }
  .no-stack .email-col-50 { width: 50% !important; }
  .no-stack .email-col-33 { width: 33% !important; }
  .no-stack .email-col-67 { width: 67% !important; }
  .no-stack .email-col-25 { width: 25% !important; }
  .no-stack .email-col-17 { width: 17% !important; }
}

  </style>
  
<!--[if mso]>
<style type="text/css">
  ul li {
    list-style:disc inside;
    mso-special-format:bullet;
  }
</style>
<![endif]-->

<!--[if !mso]><!--><link href="https://fonts.googleapis.com/css?family=Open+Sans:400,700" rel="stylesheet" type="text/css">
<style type="text/css">
  @import url('https://fonts.googleapis.com/css?family=Open+Sans:400,700');
</style><!--<![endif]-->

</head>

<body class="clean-body" style="margin: 0;padding: 0;-webkit-text-size-adjust: 100%;background-color: #f0f0f0">
  <!--[if IE]><div class="ie-container"><![endif]-->
  <!--[if mso]><div class="mso-container"><![endif]-->
  <table class="nl-container" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;min-width: 320px;Margin: 0 auto;background-color: #f0f0f0;width:100%" cellpadding="0" cellspacing="0">
  <tbody>
  <tr style="vertical-align: top">
    <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
    <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" style="background-color: #f0f0f0;"><![endif]-->
    
<div class="email-row-container" style="padding: 10px;background-color: #ffffff">
  <div style="Margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;" class="email-row">
    <div style="border-collapse: collapse;display: table;width: 100%;background-color: transparent;">
      <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 10px;background-color: #ffffff;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:600px;"><tr style="background-color: transparent;"><![endif]-->
      
<!--[if (mso)|(IE)]><td align="center" width="600" style="width: 600px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
<div class="email-col email-col-100" style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
  <div style="width: 100% !important;">
  <!--[if (!mso)&(!IE)]><!--><div style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;"><!--<![endif]-->
  
<table id="u_content_text_5" class="u_content_text" style="font-family:'Open Sans',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
  <tbody>
    <tr>
      <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Open Sans',sans-serif;" align="left">
        
  <div style="color: #000; line-height: 140%; text-align: left; word-wrap: break-word;">
    <p style="font-size: 14px; line-height: 140%; text-align: center;"><span style="font-size: 30px; line-height: 42px; color: #ff9900;"><strong><span style="font-family: 'arial black', 'avant garde', arial; line-height: 42px; font-size: 30px;">One 一个</span></strong></span></p>
  </div>

      </td>
    </tr>
  </tbody>
</table>

  <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
  </div>
</div>
<!--[if (mso)|(IE)]></td><![endif]-->
      <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
    </div>
  </div>
</div>

<div class="email-row-container" style="padding: 15px;background-image: url('https://a.mailmunch.co/user_data/landing_pages/1500505617483-background.png');background-repeat: repeat;background-position: left top;background-color: #0e3a52">
  <div style="Margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;" class="email-row">
    <div style="border-collapse: collapse;display: table;width: 100%;background-color: transparent;">
      <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 15px;background-image: url('https://a.mailmunch.co/user_data/landing_pages/1500505617483-background.png');background-repeat: repeat;background-position: left top;background-color: #0e3a52;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:600px;"><tr style="background-color: transparent;"><![endif]-->
      
<!--[if (mso)|(IE)]><td align="center" width="600" style="width: 600px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
<div class="email-col email-col-100" style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
  <div style="width: 100% !important;">
  <!--[if (!mso)&(!IE)]><!--><div style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;"><!--<![endif]-->
  
<table id="u_content_button_1" class="u_content_button" style="font-family:'Open Sans',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
  <tbody>
    <tr>
      <td style="overflow-wrap:break-word;word-break:break-word;padding:20px 20px 10px;font-family:'Open Sans',sans-serif;" align="left">
        
<div align="center">
  <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="border-spacing: 0; border-collapse: collapse; mso-table-lspace:0pt; mso-table-rspace:0pt;font-family:'Open Sans',sans-serif;"><tr><td style="font-family:'Open Sans',sans-serif;" align="center"><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="" style="height:83px; v-text-anchor:middle; width:204px;" arcsize="50.5%" stroke="f" fillcolor="#42b195"><w:anchorlock/><center style="color:#42636c;font-family:'Open Sans',sans-serif;"><![endif]-->
    <a href="" target="_blank" style="display: inline-block;font-family:'Open Sans',sans-serif;text-decoration: none;-webkit-text-size-adjust: none;text-align: center;color: #42636c; background-color: #42b195; border-radius: 42px; -webkit-border-radius: 42px; -moz-border-radius: 42px; width: auto; padding: 20px 30px; mso-border-alt: none;">
      <span style="line-height:120%;"><span style="font-size: 36px; line-height: 43.2px;">订阅成功<br /></span></span>
    </a>
  <!--[if mso]></center></v:roundrect></td></tr></table><![endif]-->
</div>

      </td>
    </tr>
  </tbody>
</table>

<table id="u_content_text_3" class="u_content_text" style="font-family:'Open Sans',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
  <tbody>
    <tr>
      <td style="overflow-wrap:break-word;word-break:break-word;padding:10px 20px;font-family:'Open Sans',sans-serif;" align="left">
        
  <div style="color: #ffffff; line-height: 150%; text-align: center; word-wrap: break-word;">
    <p style="line-height: 150%; font-size: 14px;"><span style="font-size: 16px; line-height: 24px;">kalifun.top</span></p>
  </div>

      </td>
    </tr>
  </tbody>
</table>

  <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
  </div>
</div>
<!--[if (mso)|(IE)]></td><![endif]-->
      <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
    </div>
  </div>
</div>

<div class="email-row-container" style="padding: 30px;background-color: #f0f0f0">
  <div style="Margin: 0 auto;min-width: 320px;max-width: 600px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;" class="email-row">
    <div style="border-collapse: collapse;display: table;width: 100%;background-color: transparent;">
      <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 30px;background-color: #f0f0f0;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:600px;"><tr style="background-color: transparent;"><![endif]-->
      
<!--[if (mso)|(IE)]><td align="center" width="600" style="width: 600px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
<div class="email-col email-col-100" style="max-width: 320px;min-width: 600px;display: table-cell;vertical-align: top;">
  <div style="width: 100% !important;">
  <!--[if (!mso)&(!IE)]><!--><div style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;"><!--<![endif]-->
  
<table id="u_content_text_4" class="u_content_text" style="font-family:'Open Sans',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
  <tbody>
    <tr>
      <td style="overflow-wrap:break-word;word-break:break-word;padding:20px;font-family:'Open Sans',sans-serif;" align="left">
        
  <div style="color: #000; line-height: 120%; text-align: left; word-wrap: break-word;">
    <div style="font-family: arial, helvetica, sans-serif;">
<div><span style="font-size: 12px; color: #999999; line-height: 14.4px;">You received this email because you signed up for My Company, Inc.</span></div>
<div>&nbsp;</div>
<div><span style="font-size: 12px; color: #999999; line-height: 14.4px;">Unsubscribe</span></div>
</div>
  </div>

      </td>
    </tr>
  </tbody>
</table>

  <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
  </div>
</div>
<!--[if (mso)|(IE)]></td><![endif]-->
      <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
    </div>
  </div>
</div>

    <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
    </td>
  </tr>
  </tbody>
  </table>
  <!--[if (mso)|(IE)]></div><![endif]-->
</body>

</html>
    """
    mail.send(msg)
    print("邮件发送")


def everydaysed(msginfo,mailist):
    imgurl = msginfo[0]
    VOL = msginfo[1]
    cita = msginfo[2]
    title = "One " + VOL
    msg = Message(title,sender=Config.MAIL_USERNAME,recipients=mailist)
    msg.body = '邮件内容'
    one = """
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
<!--[if gte mso 9]>
<xml>
  <o:OfficeDocumentSettings>
    <o:AllowPNG/>
    <o:PixelsPerInch>96</o:PixelsPerInch>
  </o:OfficeDocumentSettings>
</xml>
<![endif]-->
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="x-apple-disable-message-reformatting">
  <!--[if !mso]><!--><meta http-equiv="X-UA-Compatible" content="IE=edge"><!--<![endif]-->
  <title></title>
  <style type="text/css">
    body {
  margin: 0;
  padding: 0;
}

table, tr, td {
  vertical-align: top;
  border-collapse: collapse;
}

p, ul {
  margin: 0;
}

.ie-container table, .mso-container table {
  table-layout: fixed;
}

* {
  line-height: inherit;
}

a[x-apple-data-detectors=true] {
  color: inherit !important;
  text-decoration: none !important;
}

.ExternalClass, .ExternalClass p, .ExternalClass span, .ExternalClass font, .ExternalClass td, .ExternalClass div {
  line-height: 100%;
}

[owa] .email-row .email-col {
  display: table-cell;
  float: none !important;
  vertical-align: top;
}

.ie-container .email-col-100, .ie-container .email-row, [owa] .email-col-100, [owa] .email-row { width: 650px !important; }
.ie-container .email-col-17, [owa] .email-col-17 { width: 110.50000000000001px !important; }
.ie-container .email-col-25, [owa] .email-col-25 { width: 162.5px !important; }
.ie-container .email-col-33, [owa] .email-col-33 { width: 214.5px !important; }
.ie-container .email-col-50, [owa] .email-col-50 { width: 325px !important; }
.ie-container .email-col-67, [owa] .email-col-67 { width: 435.5px !important; }

@media only screen and (min-width: 670px) {
  .email-row { width: 650px !important; }
  .email-row .email-col { vertical-align: top; }
  .email-row .email-col-100 { width: 650px !important; }
  .email-row .email-col-67 { width: 435.5px !important; }
  .email-row .email-col-50 { width: 325px !important; }
  .email-row .email-col-33 { width: 214.5px !important; }
  .email-row .email-col-25 { width: 162.5px !important; }
  .email-row .email-col-17 { width: 110.50000000000001px !important; }
}

@media (max-width: 670px) {
  .hide-mobile { display: none !important; }
  .email-row-container {
    padding-left: 0px !important;
    padding-right: 0px !important;
  }
  .email-row .email-col {
    min-width: 320px !important;
    max-width: 100% !important;
    display: block !important;
  }
  .email-row { width: calc(100% - 40px) !important; }
  .email-col { width: 100% !important; }
  .email-col > div { margin: 0 auto; }
  .no-stack .email-col { min-width: 0 !important; display: table-cell !important; }
  .no-stack .email-col-50 { width: 50% !important; }
  .no-stack .email-col-33 { width: 33% !important; }
  .no-stack .email-col-67 { width: 67% !important; }
  .no-stack .email-col-25 { width: 25% !important; }
  .no-stack .email-col-17 { width: 17% !important; }
}

  </style>
  
<!--[if mso]>
<style type="text/css">
  ul li {
    list-style:disc inside;
    mso-special-format:bullet;
  }
</style>
<![endif]-->

<!--[if !mso]><!--><link href="https://fonts.googleapis.com/css?family=Lato:400,700" rel="stylesheet" type="text/css">
<style type="text/css">
  @import url('https://fonts.googleapis.com/css?family=Lato:400,700');
</style><!--<![endif]-->

</head>

<body class="clean-body" style="margin: 0;padding: 0;-webkit-text-size-adjust: 100%;background-color: #f2f2f2">
  <!--[if IE]><div class="ie-container"><![endif]-->
  <!--[if mso]><div class="mso-container"><![endif]-->
  <table class="nl-container" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;min-width: 320px;Margin: 0 auto;background-color: #f2f2f2;width:100%" cellpadding="0" cellspacing="0">
  <tbody>
  <tr style="vertical-align: top">
    <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
    <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" style="background-color: #f2f2f2;"><![endif]-->
    
<div class="email-row-container" style="padding: 0px;background-color: transparent">
  <div style="Margin: 0 auto;min-width: 320px;max-width: 650px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;" class="email-row">
    <div style="border-collapse: collapse;display: table;width: 100%;background-color: transparent;">
      <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:650px;"><tr style="background-color: transparent;"><![endif]-->
      
<!--[if (mso)|(IE)]><td align="center" width="650" style="width: 650px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
<div class="email-col email-col-100" style="max-width: 320px;min-width: 650px;display: table-cell;vertical-align: top;">
  <div style="width: 100% !important;">
  <!--[if (!mso)&(!IE)]><!--><div style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;"><!--<![endif]-->
  
<table id="u_content_text_18" class="u_content_text" style="font-family:'Lato',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
  <tbody>
    <tr>
      <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Lato',sans-serif;" align="left">
        
  <div style="color: #000; line-height: 140%; text-align: left; word-wrap: break-word;">
    <p style="font-size: 14px; line-height: 140%; text-align: center;"><span style="font-size: 14px; line-height: 19.6px; color: #f28713;"><strong><span style="font-size: 30px; line-height: 42px; font-family: 'arial black', 'avant garde', arial;">One 一个</span></strong></span></p>
  </div>

      </td>
    </tr>
  </tbody>
</table>

  <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
  </div>
</div>
<!--[if (mso)|(IE)]></td><![endif]-->
      <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
    </div>
  </div>
</div>

<div class="email-row-container" style="padding: 10px;background-color: rgba(255,255,255,0)">
  <div style="Margin: 0 auto;min-width: 320px;max-width: 650px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;" class="email-row">
    <div style="border-collapse: collapse;display: table;width: 100%;background-color: transparent;">
      <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 10px;background-color: rgba(255,255,255,0);" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:650px;"><tr style="background-color: transparent;"><![endif]-->
      
<!--[if (mso)|(IE)]><td align="center" width="650" style="width: 650px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
<div class="email-col email-col-100" style="max-width: 320px;min-width: 650px;display: table-cell;vertical-align: top;">
  <div style="width: 100% !important;">
  <!--[if (!mso)&(!IE)]><!--><div style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;"><!--<![endif]-->
  
<table id="u_content_image_8" class="u_content_image" style="font-family:'Lato',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
  <tbody>
    <tr>
      <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Lato',sans-serif;" align="left">
        
<table width="100%" cellpadding="0" cellspacing="0" border="0">
  <tr>
    <td style="padding-right: 0px; padding-left: 0px;" align="center">
    """
    two = '<img align="center" border="0" src='
    twoadd = ' alt="Image" title="Image" style="outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;clear: both;display: block !important;border: none;height: auto;float: none;width: 100%;max-width: 630px;" width="630">'
    three = """   </td>
  </tr>
</table>

      </td>
    </tr>
  </tbody>
</table>

<table id="u_content_divider_1" class="u_content_divider" style="font-family:'Lato',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
  <tbody>
    <tr>
      <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Lato',sans-serif;" align="left">
        
  <table height="0px" align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #BBBBBB;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
    <tbody>
      <tr style="vertical-align: top">
        <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;font-size: 0px;line-height: 0px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
          <span>&#160;</span>
        </td>
      </tr>
    </tbody>
  </table>

      </td>
    </tr>
  </tbody>
</table>

<table id="u_content_text_19" class="u_content_text" style="font-family:'Lato',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
  <tbody>
    <tr>
      <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Lato',sans-serif;" align="left">
        
  <div style="color: #000; line-height: 140%; text-align: center; word-wrap: break-word;">
    <p style="font-size: 14px; line-height: 140%;"><span style="font-size: 20px; line-height: 28px; font-family: 'arial black', 'avant garde', arial; color: #0ac4f7;">
    """
    four = VOL
    five = """
    </span></p>
  </div>

      </td>
    </tr>
  </tbody>
</table>

<table id="u_content_divider_2" class="u_content_divider" style="font-family:'Lato',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
  <tbody>
    <tr>
      <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Lato',sans-serif;" align="left">
        
  <table height="0px" align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #BBBBBB;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
    <tbody>
      <tr style="vertical-align: top">
        <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;font-size: 0px;line-height: 0px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
          <span>&#160;</span>
        </td>
      </tr>
    </tbody>
  </table>

      </td>
    </tr>
  </tbody>
</table>

  <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
  </div>
</div>
<!--[if (mso)|(IE)]></td><![endif]-->
      <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
    </div>
  </div>
</div>

<div class="email-row-container" style="padding: 0px;background-color: transparent">
  <div style="Margin: 0 auto;min-width: 320px;max-width: 650px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;" class="email-row">
    <div style="border-collapse: collapse;display: table;width: 100%;background-color: transparent;">
      <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:650px;"><tr style="background-color: transparent;"><![endif]-->
      
<!--[if (mso)|(IE)]><td align="center" width="650" style="width: 650px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
<div class="email-col email-col-100" style="max-width: 320px;min-width: 650px;display: table-cell;vertical-align: top;">
  <div style="width: 100% !important;">
  <!--[if (!mso)&(!IE)]><!--><div style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;"><!--<![endif]-->
  
<table id="u_content_text_20" class="u_content_text" style="font-family:'Lato',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
  <tbody>
    <tr>
      <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Lato',sans-serif;" align="left">
        
  <div style="color: #000; line-height: 140%; text-align: left; word-wrap: break-word;">
    <p style="font-size: 14px; line-height: 140%;"><span style="font-size: 18px; line-height: 25.2px;"><strong><span style="line-height: 25.2px; font-family: impact, chicago; font-size: 18px;">
    """
    six = cita
    seven = """
    </div>

      </td>
    </tr>
  </tbody>
</table>

  <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
  </div>
</div>
<!--[if (mso)|(IE)]></td><![endif]-->
      <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
    </div>
  </div>
</div>

<div class="email-row-container" style="padding: 30px;background-color: #f0f0f0">
  <div style="Margin: 0 auto;min-width: 320px;max-width: 650px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;" class="email-row">
    <div style="border-collapse: collapse;display: table;width: 100%;background-color: transparent;">
      <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 30px;background-color: #f0f0f0;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:650px;"><tr style="background-color: transparent;"><![endif]-->
      
<!--[if (mso)|(IE)]><td align="center" width="650" style="width: 650px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
<div class="email-col email-col-100" style="max-width: 320px;min-width: 650px;display: table-cell;vertical-align: top;">
  <div style="width: 100% !important;">
  <!--[if (!mso)&(!IE)]><!--><div style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;"><!--<![endif]-->
  
<table id="u_content_button_4" class="u_content_button" style="font-family:'Lato',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
  <tbody>
    <tr>
      <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Lato',sans-serif;" align="left">
        
<div align="center">
  <!--[if mso]><table width="100%" cellpadding="0" cellspacing="0" border="0" style="border-spacing: 0; border-collapse: collapse; mso-table-lspace:0pt; mso-table-rspace:0pt;font-family:'Lato',sans-serif;"><tr><td style="font-family:'Lato',sans-serif;" align="center"><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="" style="height:36px; v-text-anchor:middle; width:70px;" arcsize="11%" stroke="f" fillcolor="#3AAEE0"><w:anchorlock/><center style="color:#FFFFFF;font-family:'Lato',sans-serif;"><![endif]-->
    <a href="" target="_blank" style="display: inline-block;font-family:'Lato',sans-serif;text-decoration: none;-webkit-text-size-adjust: none;text-align: center;color: #FFFFFF; background-color: #3AAEE0; border-radius: 4px; -webkit-border-radius: 4px; -moz-border-radius: 4px; width: auto; padding: 10px 20px; mso-border-alt: none;">
      <span style="line-height:120%;">ONE</span>
    </a>
  <!--[if mso]></center></v:roundrect></td></tr></table><![endif]-->
</div>

      </td>
    </tr>
  </tbody>
</table>

<table id="u_content_text_17" class="u_content_text" style="font-family:'Lato',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
  <tbody>
    <tr>
      <td style="overflow-wrap:break-word;word-break:break-word;padding:20px;font-family:'Lato',sans-serif;" align="left">
        
  <div style="color: #000; line-height: 120%; text-align: left; word-wrap: break-word;">
    <div style="font-family: arial, helvetica, sans-serif;"><span style="font-size: 12px; color: #999999; line-height: 14.4px;">You received this email because you signed up for My Company Inc.</span></div>
<div style="font-family: arial, helvetica, sans-serif;">&nbsp;</div>
<div style="font-family: arial, helvetica, sans-serif;"><span style="font-size: 12px; color: #999999; line-height: 14.4px;">kalifun@163.com</span></div>
  </div>

      </td>
    </tr>
  </tbody>
</table>

  <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
  </div>
</div>
<!--[if (mso)|(IE)]></td><![endif]-->
      <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
    </div>
  </div>
</div>

    <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
    </td>
  </tr>
  </tbody>
  </table>
  <!--[if (mso)|(IE)]></div><![endif]-->
</body>

</html>
    """
    msg.html = one + two + imgurl + twoadd + three + four + five + six + seven
    mail.send(msg)