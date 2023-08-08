***Updated: 08-August-2023***

|[WIKI](https://www.reddit.com/r/GenP/wiki/index/)|[FAQ](https://www.reddit.com/r/GenP/wiki/faq)|[RULES](https://www.reddit.com/r/GenP/wiki/rules/)|[Issues FIX](https://www.reddit.com/r/GenP/comments/ue47y6/possible_solution_to_unlicensed_app_popup_no/)|[Patching Methods](https://www.reddit.com/r/GenP/wiki/patchmethods)|[Compatibility List](https://www.reddit.com/r/GenP/comments/yao439/update_compatibility_list_2023_creative_suite/)|[Guides + Links](https://www.reddit.com/r/GenP/wiki/redditgenpguides)|
|:-|:-|:-|:-|:-|:-|:-|


*- Special thanks to eaaasun, dev/null and many other members!*

&amp;#x200B;

* 1️⃣ **Option - Avoid Credit Card popups on Creative Cloud and allow installation of apps;**
* 2️⃣ **Option MOST COMMON - Deal with individual apps acting up / stop working due to unlicensed popups;**
* **3️⃣ Option - Fix CC not loading / loading continuously; (Reverse of option 1 basically)**

&amp;#x200B;

❗ **𝗣𝗘𝗢𝗣𝗟𝗘 𝗥𝗘𝗔𝗗 𝗧𝗛𝗜𝗦 𝗣𝗟𝗘𝗔𝗦𝗘, 𝗔𝗡𝗗 𝗦𝗧𝗢𝗣 𝗔𝗦𝗞𝗜𝗡𝗚 𝗧𝗛𝗜𝗦 𝗦𝗛\_𝗧 𝗢𝗩𝗘𝗥 𝗔𝗡𝗗 𝗢𝗩𝗘𝗥 𝗔𝗚𝗔𝗜𝗡 ❗**

⚠️ If your windows firewall is being managed by your antivirus *(should say "firewall is being managed by thirdparty" or something similar)* **then all the changes below must be applied in said Antivirus firewall** *(thats on you to figure out all of them have different menus and places, however the paths to block are the same)* **- Also whichever is "the boss" it must remain ON.**

\- If you get popups, Block with firewall Creative Cloud, Licensing services.

\- If you still get popups, Block with firewall the app.exe (ex. photoshop.exe)

\- If you still get popups after all that, Host file edit.

\- If you  still getting after all those without any mistake, honestly Run guide 4 completely and try again. Otherwise, out of options.

&amp;#x200B;

\------------------------------------------------------------------------------------------------------------------

# 1️⃣ OPTION - CCStopper / Host File

*(for genp method only)*

[CCStopper](https://github.com/eaaasun/CCStopper/releases)

[DevNull .bat file](https://cdn.discordapp.com/attachments/971037438648668190/984805878395969626/adobehostpatch_by_devnull.bat)

*(CCStopper.rar all files must be extracted, and either .bats options above must be run as Administrator)*

&amp;#x200B;

* **CCStopper selection (2) for Internet Patch &gt; (1) for Firewall Block.**
   * Basically will create a firewall rule on the following services, located in:

&amp;#x200B;

&gt;Path of ADS - `C:\Program Files (x86)\Common Files\Adobe\Adobe Desktop Common\ADS\Adobe Desktop Service.exe`  
&gt;  
&gt;Path of Licensing - `C:\ProgramFiles\Common Files\Adobe\Adobe Desktop Common\NGL\adobe_licensing_wf.exe`  
&gt;  
&gt;Path of Licensing helper - `C:\ProgramFiles\Common Files\Adobe\Adobe Desktop Common\NGL\adobe_licensing_wf_helper.exe`  
&gt;  
&gt;[Thanks to u/Kaitsu](https://www.reddit.com/r/GenP/comments/svehws/method_to_avoid_credit_card_requirement_via/)

&amp;#x200B;

* **CCStopper selection (2) for Internet Patch &gt; (2) for Host File / DevNull.bat:.**

Will basically try to edit the Host file located in:

&gt;`C:\Windows\System32\drivers\etc`  
&gt;  
&gt;And will add the list of IP code blocks from this post below.

The same can be done manually by going to the same location above, Right-click "hosts" file, "Open with" notepad, add the same lines under everything that already exists in the file to it, then just save the file and reboot your system:

    # BLOCK ADOBE COMPLETE #
    0.0.0.0 ic.adobe.io
    0.0.0.0 adobeereg.com
    0.0.0.0 wip.adobe.com
    0.0.0.0 wip1.adobe.com
    0.0.0.0 wip2.adobe.com
    0.0.0.0 wip3.adobe.com
    0.0.0.0 wip4.adobe.com
    0.0.0.0 www.wip.adobe.com
    0.0.0.0 www.wip1.adobe.com
    0.0.0.0 www.wip2.adobe.com
    0.0.0.0 www.wip3.adobe.com
    0.0.0.0 www.wip4.adobe.com
    0.0.0.0 ereg.wip.adobe.com
    0.0.0.0 ereg.wip1.adobe.com
    0.0.0.0 ereg.wip2.adobe.com
    0.0.0.0 ereg.wip3.adobe.com
    0.0.0.0 ereg.wip4.adobe.com
    0.0.0.0 activate.adobe.com
    0.0.0.0 activate.wip.adobe.com
    0.0.0.0 activate-sea.adobe.com
    0.0.0.0 activate-sjc0.adobe.com
    0.0.0.0 activate.wip1.adobe.com
    0.0.0.0 activate.wip2.adobe.com
    0.0.0.0 activate.wip3.adobe.com
    0.0.0.0 activate.wip4.adobe.com
    0.0.0.0 3dns.adobe.com
    0.0.0.0 ereg.adobe.com
    0.0.0.0 bam.nr-data.net
    0.0.0.0 ood.opsource.net
    0.0.0.0 crl.verisign.net
    0.0.0.0 hl2rcv.adobe.com
    0.0.0.0 genuine.adobe.com
    0.0.0.0 www.adobeereg.com
    0.0.0.0 3dns-1.adobe.com
    0.0.0.0 3dns-2.adobe.com
    0.0.0.0 3dns-3.adobe.com
    0.0.0.0 3dns-4.adobe.com
    0.0.0.0 adobe-dns.adobe.com
    0.0.0.0 adobe-dns-1.adobe.com
    0.0.0.0 adobe-dns-2.adobe.com
    0.0.0.0 adobe-dns-3.adobe.com
    0.0.0.0 adobe-dns-4.adobe.com
    0.0.0.0 practivate.adobe
    0.0.0.0 practivate.adobe.ntp
    0.0.0.0 practivate.adobe.ipp
    0.0.0.0 practivate.adobe.com
    0.0.0.0 practivate.adobe.newoa
    0.0.0.0 lm.licenses.adobe.com
    0.0.0.0 hlrcv.stage.adobe.com
    0.0.0.0 prod.adobegenuine.com
    0.0.0.0 uds.licenses.adobe.com
    0.0.0.0 k.sni.global.fastly.net
    0.0.0.0 na1r.services.adobe.com
    0.0.0.0 lmlicenses.wip4.adobe.com
    0.0.0.0 na2m-pr.licenses.adobe.com
    0.0.0.0 wwis-dubc1-vip60.adobe.com
    0.0.0.0 workflow-ui-prod.licensingstack.com
    # THIS SHORTLIST PROBABLY ENOUGH TO BLOCK ADOBE WITHOUT ISSUES HOPEFULLY #
    0.0.0.0 ic.adobe.io
    0.0.0.0 0mo5a70cqa.adobe.io    
    0.0.0.0 1b9khekel6.adobe.io    
    0.0.0.0 23ynjitwt5.adobe.io    
    0.0.0.0 2ftem87osk.adobe.io    
    0.0.0.0 3ca52znvmj.adobe.io    
    0.0.0.0 3d3wqt96ht.adobe.io    
    0.0.0.0 4vzokhpsbs.adobe.io    
    0.0.0.0 5zgzzv92gn.adobe.io    
    0.0.0.0 69tu0xswvq.adobe.io    
    0.0.0.0 7g2gzgk9g1.adobe.io    
    0.0.0.0 7m31guub0q.adobe.io    
    0.0.0.0 7sj9n87sls.adobe.io    
    0.0.0.0 8ncdzpmmrg.adobe.io
    # HIT OR MISS BELOW BUT HAVE BEEN MENTIONED A LOT RECENTLY
    0.0.0.0 cc-api-data.adobe.io
    0.0.0.0 jc95y2v12r.adobe.io
    0.0.0.0 ph0f2h2csf.adobe.io
    0.0.0.0 b5kbg2ggog.adobe.io
    0.0.0.0 guzg78logz.adobe.io

# ---------------------

# 2️⃣ OPTION - FIREWALL RULE on App-in-question.exe

*(for genp or monkrus methods)*

Example will be for "Photoshop" but the method is the same across programs.

&gt;`Windows &gt; Windows Firewall &gt; Advanced Settings`

[⚠️ If you see this, All firewall rules must be done in your antivirus firewall settings, and not on windows defender firewall \(otherwise they will have no effect\) - But just in case, have in both lol](https://preview.redd.it/9dkbvchw7b2a1.png?width=666&amp;format=png&amp;auto=webp&amp;s=3125a3bd2aa17875c94a657a9793f808a73daa03)

[Outbound Rules should be more than enough. Only do both if the first doesn't work.](https://preview.redd.it/urxwddgq8b2a1.png?width=934&amp;format=png&amp;auto=webp&amp;s=44fc398cdcbca9112a3927f7e4b7315817324fb0)

[When looking for the program path, we want the Actual Program \\".exe\\" and not the shortcuts. How to distinct them - LEFT: SHORTCUT \\".EXE\\" | RIGHT: ACTUAL \\".EXE\\"](https://preview.redd.it/qt76zlp3vb2a1.png?width=221&amp;format=png&amp;auto=webp&amp;s=a00255900a139043adaed0216bb1aaf14794d334)

On **Outbound** section:

* **Create a New Rule**

&gt;**Rule Type:** Program  
&gt;  
&gt;**Program Path:**  
&gt;  
&gt;Window Key &gt; search for "photoshop" and on the shortcut  
&gt;  
&gt;RIGHT CLICK `open file location`  
&gt;  
&gt;RIGHT CLICK `open file location` again  
&gt;  
&gt;When no longer a *"shortcut"*, RIGHT CLICK `Copy as Path`  
&gt;  
&gt;Should be located in: `C:\Program Files\Adobe\Adobe Photoshop 2023\Photoshop.exe`  
&gt;  
&gt;REMOVE THE **" "** AT THE ENDS IF YOU HAVE THEM  
&gt;  
&gt;**Block the connection**  
&gt;  
&gt;**Select all Domains**  
&gt;  
&gt;Give whatever name you want - **That's it**

You will lose internet access going out from the application, at the same time, the license also wont be able to check if good or bad.

&gt;Outside of that, unplug internet problem solved lol

&amp;#x200B;

\---------------------

&amp;#x200B;

# 3️⃣ OPTION - CC LOADING CONTINUOUSLY / LOOP (CLEAN)

Most probably because of CCStopper OR other firewall rules created / Host file that are working against each other completely blocking internet. - *(reverse of Option 1)*

&amp;#x200B;

**Reverse CCStopper Rule:**

&gt;`Windows &gt; Windows Firewall &gt; Advanced Settings`  
&gt;  
&gt;Check both **Inbound and Outbound**  
&gt;  
&gt;**Disable** or remove the rule "CCStopper" or other firewall rules you created asked in the guides.

&amp;#x200B;

**Reverse Hosts File edit:**

&gt;`C:\Windows\System32\drivers\etc`  
&gt;  
&gt;Right-click on "hosts" file, "Open with notepad" and remove all the lines related to  
&gt;  
&gt;`# BLOCK ADOBE #` in this post, save the file and reboot your system:

This should fix the looping bring CC to its default behavior, but at the same time will be open  internet - which may cause issues for the apps currently installed.

If it happens, do **Option 2 and create an Outbound rule** for the programs " .exe " malfunctioning.

&amp;#x200B;

**If neither of these have fixed the issue, let us know - but please be specific on:**

&gt;What method you have (genp or monkrus);  
&gt;  
&gt;Which of these fixes didnt work;  
&gt;  
&gt;What problem still happens;

&amp;#x200B;

**Cheers!**

*Update: IP List has been cleaned up.*