---
layout: post
title: Setting up OpenVPN Client in Ubuntu 14.04
tags: linux systems
category: notes
icon: beer #weaselpipe.com/icons
year: 2016
month: 12
day: 21
published: true
summary: Configuring Network Manager to use  OpenVPN connections.
---

This guide is for setting up an OpenVPN client on Ubuntu 14.04 using Network Manager.

**Step 1:** Install the network manager openvpn plugin.

```
$ sudo apt-get install network-manager-openvpn
```

**Step 2:** Acquire the openvpn documents required: User Certificate (.cer), CA Certificate (.crt), and Private Key (.key).


**Step 3:** Click on the network-manager icon in the upper right hand corner of the screen; you should see a new menu item titled "VPN Connections".

 - Under this item, click on "Configure VPN..."
 - Select "Add"
 - Choose Connection Type "OpenVPN"
 - Under gateway, put in your IP Address or domain name.
 - Set authentication type to "Certificates (TLS)"
 - Set the .cer file for "User Certificate"
 - Set the .crt file for "CA Certificate"
 - Set the .key file for "Private Key"

Next, click on the "Advanced" button. Under the "General" tab:
 
 - Select "Use a TCP connection" if you use TCP instead of UDP.
 - Optionally, you can change the gateway port here.

And that's it!

