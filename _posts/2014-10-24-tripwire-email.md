---
layout: post
title: Sending email with tripwire
tags: linux apt
category: programming
year: 2014
month: 10
day: 24
published: true
summary: How to send email with tripwire.
---

I've been trying to setup tripwire, well, I _did_ setup tripwire. 
That was the easy part. The hard part has been getting it to email me reports.
The problem is that I have comcast internet... and they do shitty things, like block port 25.
I know they are well intentioned, trying to block spamers and all - but they are still a bunch of bitches. 
(Steve Jenkins)[http://www.stevejenkins.com/blog/2013/06/howto-get-around-comcast-port-25-block-with-a-postfix-server/] wrote an article about how to get past the port 25 block with a postfix server.
He suggested adding the following lines to your **/etc/postfix/main.cf** file:

```
relayhost = [smtp.comcast.net]:587
smtp_sasl_auth_enable = yes
smtp_sasl_password_maps = hash:/etc/postfix/sasl_passwd
smtp_sasl_security_options =
```

and creating a **/etc/postfix/sasl_passwd** file with the following line

```
smtp.comcast.net    USERNAME:PASSWORD
```

where USERNAME and PASSWORD is your comcast email username and the corresponding password. Since you have sensitive info in that file, it is best to lock it down.

```
chown root:root /etc/postfix/sasl_passwd
chmod 600 /etc/postfix/sasl_passwd
```

Finally, convert the text file to a databse format for postfix:

```
postmap /etc/postfix/sasl_passwd
postfix reload
```

Alternatively, he specifies that you could use google instead by adding these two lines

```
smtp_use_tls=yes
smtp_tls_CAfile = /etc/ssl/certs/ca-certificates.crt
```

Anyways, this is all great except that comcast seems to be checking that the sender is real - first by seeing if there is a mail server at the domain.
Since tripwire uses the hostname of the machine as the domain of the from address, I had to set my hostname to be a fully qualified domain.
But then they somehow knew that "tripwire" was not a real user, since I could send mail as my real username but not as "tripwire".
FAIL.

Apparently, tripwire is only able to either use an SMTP server or sendmail, which is also annoying. 
Fortunately, there seems to be another way using ssmtp.

```
sudo apt-get install ssmtp
```

This automatically removed postfix, but amazingly did not also uninstall tripwire. 
This may come back to haunt me in the future - so I might need to invoke (equivs)[http://shallowsky.com/blog/linux/install/blocking-deb-dependencies.html], a tool that can be used to build "fake" deb files to be used to "satisfy" debian dependencies...

For now though, the trick is that ssmtp can __act__ like sendmail. 
In fact, if you don't have **libmail-sendmail-perl** or sendmail itself installed, /usr/sbin/sendmail will get automatically symlinked to ssmtp.
That means, in theory, that now tripwire will try to use ssmtp!

We can configure ssmtp by editing **/etc/ssmtp/ssmtp.conf**:

```
sudo vim /etc/ssmtp/ssmtp.conf
```

and updating the file with the following settings recommended by this (website)[https://wiki.archlinux.org/index.php/SSMTP]:

```
# The user that gets all the mails (UID < 1000, usually the admin)
root=username@gmail.com

# The mail server (where the mail is sent to), both port 465 or 587 should be acceptable
# See also http://mail.google.com/support/bin/answer.py?answer=78799
mailhub=smtp.gmail.com:587

# The address where the mail appears to come from for user authentication.
rewriteDomain=gmail.com

# The full hostname
hostname=localhost

# Use SSL/TLS before starting negotiation
UseTLS=Yes
UseSTARTTLS=Yes

# Username/Password
AuthUser=username
AuthPass=password

# Email 'From header's can override the default domain?
FromLineOverride=yes
```

Protect the file

```
chmod 640 /etc/ssmtp/ssmtp.conf
```

And test it with tripwire

``` 
tripwire --test --email you@yourtestemail.com
```
