$bytes = [System.IO.File]::ReadAllBytes("C:\Program Files (x86)\Common Files\Adobe\Adobe Desktop Common\AppsPanel\AppsPanelBL.dll")  
$bytes[1116554] = 0xfe  
$bytes[1216383] = 0xfe  
$bytes[1987439] = 0xfe  
$bytes[2150557] = 0xfe  
$bytes[2151982] = 0xfe  
$bytes[2152497] = 0xfe  
$bytes[2153297] = 0xfe  
$bytes[2279801] = 0xc6  
$bytes[2279802] = 0x40  
$bytes[2279811] = 0xc6  
$bytes[2279812] = 0x40  
$bytes[2279821] = 0xc6  
$bytes[2279822] = 0x40  
[System.IO.File]::WriteAllBytes("C:\Program Files (x86)\Common Files\Adobe\Adobe Desktop Common\AppsPanel\AppsPanelBL.dll", $bytes)

---

```
$bytes = [System.IO.File]::ReadAllBytes("C:\Program Files (x86)\Common Files\Adobe\Adobe Desktop Common\AppsPanel\AppsPanelBL.dll")  
$bytes[1116554] = 0xfe  
$bytes[1216383] = 0xfe  
$bytes[1987439] = 0xfe  
$bytes[2150557] = 0xfe  
$bytes[2151982] = 0xfe  
$bytes[2152497] = 0xfe  
$bytes[2153297] = 0xfe  
$bytes[2279801] = 0xc6  
$bytes[2279802] = 0x40  
$bytes[2279811] = 0xc6  
$bytes[2279812] = 0x40  
$bytes[2279821] = 0xc6  
$bytes[2279822] = 0x40  
[System.IO.File]::WriteAllBytes("C:\Program Files (x86)\Common Files\Adobe\Adobe Desktop Common\AppsPanel\AppsPanelBL.dll", $bytes)
```