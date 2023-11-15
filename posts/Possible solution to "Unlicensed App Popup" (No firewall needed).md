***Updated: 14-November-2023***

\------------------------------------------------------------------------------------------------------------------

**All following options are towards avoiding either credit card / unlicensed or disabled pop-ups.**

* 1️⃣ **Option -** ***PowerShell Cmd / Manual Host File;***
* 2️⃣ **Option -** ***Firewall Rules (disconnecting access to or from internet);***
* **3️⃣ Option -** ***Fix CC not loading / loading continuously; (Reverse of option 1 and 2)***

&amp;#x200B;

❗ **𝗣𝗘𝗢𝗣𝗟𝗘 𝗥𝗘𝗔𝗗 𝗧𝗛𝗜𝗦 𝗣𝗟𝗘𝗔𝗦𝗘, 𝗔𝗡𝗗 𝗦𝗧𝗢𝗣 𝗔𝗦𝗞𝗜𝗡𝗚 𝗧𝗛𝗜𝗦 𝗦𝗛\_𝗧 𝗢𝗩𝗘𝗥 𝗔𝗡𝗗 𝗢𝗩𝗘𝗥 𝗔𝗚𝗔𝗜𝗡 ❗**

🔖 **This page has been a bit left out for a while which may have caused confusion among several people. For the moment this will be updated with just the bare minimum until we figure out a better way to help about. Apologies 🥹**

⚠️ If your windows firewall is being managed by your antivirus *(should say "firewall is being managed by third-party" or something similar)* **then all the changes below must be applied in said Antivirus firewall** *(that's on you to figure out all of them have different menus and places, however the paths to block are the same)* **- Also whichever is "the boss" it must remain ON.**

\- If you  still getting after all those without any mistake, honestly Run guide 4 completely and try again. Otherwise, out of options.

&amp;#x200B;

\------------------------------------------------------------------------------------------------------------------

# 1️⃣ OPTION - PowerShell Cmd / Manual Host File

*(for genp method mainly / possibly useful on monkrus as last resort)*

Use the following two commands in **PowerShell (admin)** if your apps are warning you of unlicensed or non-genuine usage:

First run:

    Stop-Process -Name "Adobe Desktop Service" -force

Then

    Add-Content -Path $env:windir\System32\drivers\etc\hosts -Value "`n0.0.0.0`tm59b4msyph.adobe.io" -Force
    
    Add-Content -Path $env:windir\System32\drivers\etc\hosts -Value "`n0.0.0.0`tic.adobe.io" -Force

Basically it will edit the Host file located in:

&gt;`C:\Windows\System32\drivers\etc`  
&gt;  
&gt;And will add the list of IP code blocks above to it.

&amp;#x200B;

If you prefer to do this manually, you can add the following two lines to the system hosts file, using a text editor of your choice. - Then just save the file and reboot your system.

    # BLOCK AD0BE (current as of 08/11/2023) #
    0.0.0.0 m59b4msyph.adobe.io
    0.0.0.0 ic.adobe.io

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

Most probably because of Host file edits or Firewall rules (including outdated ones) that are either working against each other or blocking something that shouldnt be blocked. - *(reverse of Option 1 and 2)*

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

**Reverse Firewall Rule:**

&gt;`Windows &gt; Windows Firewall &gt; Advanced Settings`  
&gt;  
&gt;Check both **Inbound and Outbound**  
&gt;  
&gt;**Disable** or remove any rules that are applied to AD0BE or other firewall rules you created or asked in the guides.

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

🛟 ❮ Return to [**r/Genp**](https://www.reddit.com/r/GenP/)

☠️ ❮ Return to [**Wiki**](https://www.reddit.com/r/GenP/wiki/index/)